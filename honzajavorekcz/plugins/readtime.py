import re
import math

from pelican import signals

from honzajavorekcz.plugins.utils import parse_html, get_articles


WORDS_PER_MINUTE = 200


def register():
    signals.all_generators_finalized.connect(set_readtime)


def set_readtime(generators):
    for article in get_articles(generators):
        with parse_html(article) as html_tree:
            text_content = html_tree.text_content()
        words_count = len(re.split(r'\s+', text_content))
        readtime = math.ceil(words_count / WORDS_PER_MINUTE)
        article.metadata['readtime'] = readtime
        article.readtime = readtime
