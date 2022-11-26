import os
import sys

from lxml import etree
from pelican import signals, contents

sys.path.append(os.path.dirname(__file__))
from utils import modify_html, wrap_element


def register():
    signals.all_generators_finalized.connect(enhance_tables)


def enhance_tables(content):
    if not isinstance(content, contents.Article):
        return

    with modify_html(content) as html_tree:
        for table in html_tree.findall('.//table'):
            div = etree.Element('div')
            div.set('class', 'table')
            wrap_element(table, div)
