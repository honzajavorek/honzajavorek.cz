import os
import sys

from pelican import signals, contents

sys.path.append(os.path.dirname(__file__))
from utils import modify_html


def register():
    signals.all_generators_finalized.connect(process_code_blocks)


def process_code_blocks(content):
    if not isinstance(content, contents.Article):
        return

    with modify_html(content) as html_tree:
        for pre in html_tree.findall('.//div/pre'):
            pre.getparent().tag = 'pre'
            pre.tag = 'code'
