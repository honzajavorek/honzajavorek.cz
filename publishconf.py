import os
import sys
from operator import itemgetter
import logging

import requests

sys.path.append(os.curdir)
from pelicanconf import *


DELETE_OUTPUT_DIRECTORY = True
GOOGLE_ANALYTICS = 'UA-1316071-6'

SITEURL = os.getenv('VERCEL_URL', 'https://honzajavorek.cz')
logging.getLogger(__name__).info('SITEURL=%s', SITEURL)
