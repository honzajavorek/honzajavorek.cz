import re
import logging
from pathlib import Path

from lxml import html
from pelican import signals
from PIL import Image

from honzajavorekcz.plugins.utils import parse_html, wrap_element, get_articles


logger = logging.getLogger(__name__)


VIDEO_SUFFIXES = ['.gif']
VECTOR_SUFFIXES = ['.svg']


def register():
    signals.all_generators_finalized.connect(process_media)


def process_media(generators):
    for article in get_articles(generators):
        content_dir = article.settings['PATH']

        if hasattr(article, 'image'):
            attrs = check_img_src(article.image, content_dir,
                                  max_px=article.settings['IMG_MAX_PX'],
                                  max_mb=article.settings['IMG_MAX_MB'])
            for attr_name, attr_value in attrs.items():
                setattr(article, attr_name, attr_value)
            article.metadata.update(attrs)

        with parse_html(article, modify=True) as html_tree:
            for img in html_tree.xpath('//img'):
                check_img_src(img.get('src'), content_dir,
                              max_px=article.settings['IMG_MAX_PX'],
                              max_mb=article.settings['IMG_MAX_MB'])

            for iframe in html_tree.xpath('//iframe'):
                iframe_to_figure(iframe)

            for object_ in html_tree.xpath('//object'):
                object_to_figure(object_)

            for blockquote in html_tree.xpath('//blockquote'):
                blockquote_to_figure(blockquote)

            for img in html_tree.xpath('//p[count(img) = 1]/img'):
                img_to_figure(img)

            for img in html_tree.xpath('//p[count(a) = 1]/a[count(img) = 1]/img'):
                img_to_figure(img)


def iframe_to_figure(iframe):
    wrap_element(iframe, element('figure', ['figure', 'figure-embed']))


def object_to_figure(object_):
    wrap_element(object_, element('figure', ['figure', 'figure-embed']))


def img_to_figure(img):
    if 'left' in img.classes or 'right' in img.classes:
        return
    img.classes.update(['img-fluid', 'figure-img', 'rounded'])

    if img.getparent().tag == 'a':
        img.getparent().classes.add('figure-link')

    figure = next(img.iterancestors(tag='p'))
    figure.tag = 'figure'
    figure.classes.add('figure')

    create_figcaption(img)


def blockquote_to_figure(blockquote):
    figure = element('figure', classes=['figure', 'figure-blockquote'])
    wrap_element(blockquote, figure)

    if 'twitter-tweet' in blockquote.classes:
        figure.classes.add('figure-tweet')
        blockquote.classes.add('blockquote-tweet')
    blockquote.classes.add('blockquote')

    last_p = next(blockquote.iterchildren(tag='p', reversed=True))
    if 'twitter-tweet' in blockquote.classes:
        assert last_p.tail.startswith('—')
        last_a = next(blockquote.iterchildren(tag='a', reversed=True))
        figcaption = element('figcaption', classes=['blockquote-footer'])
        figcaption.text = last_p.tail.lstrip('—')
        figcaption.append(last_a)
        figure.append(figcaption)
        last_p.tail = None
    else:
        last_line = last_p.text_content() or ''
        if last_line.startswith('—'):
            last_p.text = last_p.text.lstrip('—')
            last_p.tag = 'figcaption'
            last_p.classes.add('blockquote-footer')
            figure.append(last_p)


def create_figcaption(img):
    figcaption = element('figcaption', classes=['figure-caption'])
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

    img.getparent().append(figcaption)


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
        with Image.open(filename) as img:
            width, height = img.size
        is_video = filename.suffix.lower() in VIDEO_SUFFIXES
    except IOError:
        logger.error('Image not found: %s', img_src)
        return dict(width=None, height=None, color=None)

    if not is_video and size_mb > max_mb:
        logger.error('Image too large: %s (%dmb, max size: %dmb)', img_src, size_mb, max_mb)
    if width > max_px:
        logger.error('Image too large: %s (%dpx, max width: %dpx)', img_src, width, max_px)
    if height > max_px:
        logger.error('Image too large: %s (%dpx, max height: %dpx)', img_src, height, max_px)
    return dict(image_width=width, image_height=height)


def get_image_filename(content_dir, img_src):
    return Path(content_dir) / re.sub(r'.*/images/', 'images/', img_src)


def element(tag, classes=None):
    el = html.HtmlElement()
    el.tag = tag
    el.classes.update(classes or [])
    return el
