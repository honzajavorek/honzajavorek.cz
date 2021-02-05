import os
import sys
import re
import logging
from pathlib import Path

from lxml import etree
from pelican import signals, contents
from PIL import Image

sys.path.append(os.path.dirname(__file__))
from utils import modify_html, wrap_element


logger = logging.getLogger(__name__)


VIDEO_SUFFIXES = ['.gif']
VECTOR_SUFFIXES = ['.svg']


def register():
    signals.content_object_init.connect(process_media)


def process_media(content):
    if not isinstance(content, contents.Article):
        return

    content_dir = content.settings['PATH']

    if hasattr(content, 'image'):
        width, height = check_img_src(content.image, content_dir,
                                      max_px=content.settings['IMG_MAX_PX'],
                                      max_mb=content.settings['IMG_MAX_MB'])
        content.image_width, content.image_height = width, height
        content.metadata.update(image_width=width, image_height=height)

    with modify_html(content) as html_tree:
        for iframe in html_tree.xpath('//iframe'):
            iframe_to_figure(iframe)

        for object_ in html_tree.xpath('//object'):
            object_to_figure(object_)

        for blockquote in html_tree.xpath('//blockquote'):
            tweet_to_figure(blockquote)

        for img in html_tree.xpath('//p[count(img) = 1]/img'):
            img_to_figure(img, content_dir)

        for img in html_tree.xpath('//img'):
            check_img_src(img.get('src'), content_dir,
                          max_px=content.settings['IMG_MAX_PX'],
                          max_mb=content.settings['IMG_MAX_MB'])


def iframe_to_figure(iframe):
    wrap_element(iframe, etree.Element('figure'))


def object_to_figure(object_):
    wrap_element(object_, etree.Element('figure'))


def img_to_figure(img, content_dir):
    if 'left' in img.classes or 'right' in img.classes:
        return

    figure = img.getparent()
    figure.tag = 'figure'

    create_figcaption(img, figure)


def tweet_to_figure(blockquote):
    if 'twitter-tweet' not in blockquote.classes:
        return

    wrap_element(blockquote, etree.Element('figure'))


def create_figcaption(img, figure):
    figcaption = etree.Element('figcaption')
    create = False

    if img.tail:
        create = True
        figcaption.text = img.tail
        img.tail = ''

    for sibling in img.itersiblings():
        create = True
        figcaption.append(sibling)

    if not create:
        return

    figure.append(figcaption)


def check_img_src(img_src, content_dir, max_px, max_mb):
    logger.info('Checking %s', img_src)

    if img_src.startswith('http'):
        logger.error('Found remotely linked image: %s', img_src)
        return None, None

    filename = get_image_filename(content_dir, img_src)
    if filename.suffix.lower() in VECTOR_SUFFIXES:
        logger.info('Vector image: %s', img_src)
        return None, None

    try:
        size_mb = filename.stat().st_size / 1024 / 1024
        width, height = Image.open(filename).size
        is_video = filename.suffix.lower() in VIDEO_SUFFIXES
    except IOError:
        logger.error('Image not found: %s', img_src)
        return None, None

    if not is_video and size_mb > max_mb:
        logger.error('Image too large: %s (%dmb, max size: %dmb)', img_src, size_mb, max_mb)
    if width > max_px:
        logger.error('Image too large: %s (%dpx, max width: %dpx)', img_src, width, max_px)
    if height > max_px:
        logger.error('Image too large: %s (%dpx, max height: %dpx)', img_src, height, max_px)
    return width, height


def get_image_filename(content_dir, img_src):
    return Path(content_dir) / re.sub(r'.*/images/', 'images/', img_src)
