import re
import math


WORDS_PER_MINUTE = 200


def set_readtime(article, html_tree):
    text_content = html_tree.text_content()
    words_count = len(re.split(r'\s+', text_content))
    readtime = math.ceil(words_count / WORDS_PER_MINUTE)
    article.metadata['readtime'] = readtime
    article.readtime = readtime
