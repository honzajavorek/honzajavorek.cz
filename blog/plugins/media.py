import re
import logging
from pathlib import Path
from functools import lru_cache

from lxml import html
from pelican import signals
from PIL import Image

from blog.plugins.utils import parse_html, wrap_element, get_articles


logger = logging.getLogger(__name__)


def register():
    signals.all_generators_finalized.connect(process_media)


def process_media(generators):
    content_dir = Path(generators[0].settings['PATH'])

    for article in get_articles(generators):
        if getattr(article, 'image', None):
            image_path = content_dir / article.image
            width, height = get_dimensions(image_path)
            article.metadata['image_width'] = width
            article.image_width = width
            article.metadata['image_height'] = height
            article.image_height = height

        with parse_html(article, modify=True) as html_tree:
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


@lru_cache
def get_dimensions(image_path):
    with Image.open(image_path) as img:
        return img.size


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


def element(tag, classes=None):
    el = html.HtmlElement()
    el.tag = tag
    el.classes.update(classes or [])
    return el
