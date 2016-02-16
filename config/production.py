
import os
import sys

CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(CONFIG_DIR)

from base import *  # NOQA


SITEURL = 'http://honzajavorek.cz'
RELATIVE_URLS = False
