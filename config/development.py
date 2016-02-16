
import os
import sys

CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(CONFIG_DIR)

from base import *  # NOQA


SITEURL = 'http://localhost:8000'
RELATIVE_URLS = True

URL_EXT = '.html'
ARTICLE_URL += URL_EXT
ARTICLE_LANG_URL += URL_EXT
PAGE_URL += URL_EXT
PAGE_LANG_URL += URL_EXT
