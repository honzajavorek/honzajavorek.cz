# -*- coding: utf-8 -*- #

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from base import *  # NOQA


SITEURL = 'http://localhost:8000/output'
RELATIVE_URLS = True

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'
URL_EXT = '.html'

DELETE_OUTPUT_DIRECTORY = True
