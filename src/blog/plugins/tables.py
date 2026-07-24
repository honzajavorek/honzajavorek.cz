from lxml import etree

from blog.plugins.utils import wrap_element


def enhance_tables(html_tree):
    for table in html_tree.findall('.//table'):
        table.classes.add('table')
        div = etree.Element('div')
        div.set('class', 'table-responsive')
        wrap_element(table, div)
