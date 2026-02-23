import re
import contextlib

from lxml import html, etree
from lxml.html import soupparser as html_soup
from pelican.generators import ArticlesGenerator


@contextlib.contextmanager
def parse_html(content, prop='_content', modify=False):
    html_string = getattr(content, prop)
    try:
        html_tree = html.fragment_fromstring(html_string, create_parent='div')
    except etree.ParserError:
        # https://bugs.launchpad.net/lxml/+bug/1949271
        html_tree = html_soup.fromstring(f'<html>{html_string}</html>')
        html_tree.tag = 'div'

    yield html_tree

    if modify:
        html_string = html.tostring(html_tree, encoding='unicode')
        html_string = re.sub(r'%7B(\w+)%7D', r'{\1}', html_string)
        html_string = re.sub(r'%7C(\w+)%7C', r'|\1|', html_string)
        setattr(content, prop, html_string)


def wrap_element(element, wrapper_element):
    element.addprevious(wrapper_element)
    wrapper_element.insert(0, element)
    return wrapper_element


def get_articles(generators):
    for generator in generators:
        if isinstance(generator, ArticlesGenerator):
            yield from generator.articles
            yield from generator.translations
            yield from generator.hidden_articles
            yield from generator.hidden_translations
            yield from generator.drafts
            yield from generator.drafts_translations
