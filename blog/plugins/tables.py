from lxml import etree
from pelican import signals

from blog.plugins.utils import parse_html, wrap_element, get_articles


def register():
    signals.all_generators_finalized.connect(enhance_tables)


def enhance_tables(generators):
    for article in get_articles(generators):
        with parse_html(article, modify=True) as html_tree:
            for table in html_tree.findall('.//table'):
                table.classes.add('table')
                div = etree.Element('div')
                div.set('class', 'table-responsive')
                wrap_element(table, div)
