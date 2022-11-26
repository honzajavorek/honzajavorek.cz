import os
import sys

from pelican import signals

sys.path.append(os.path.dirname(__file__))
from utils import parse_html, get_articles


def register():
    signals.all_generators_finalized.connect(process_code_blocks)


def process_code_blocks(generators):
    for article in get_articles(generators):
        with parse_html(article, modify=True) as html_tree:
            for pre in html_tree.findall('.//div/pre'):
                pre.getparent().tag = 'pre'
                pre.tag = 'code'
