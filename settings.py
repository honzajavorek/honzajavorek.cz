
from danube_delta.settings import *  # NOQA


AUTHOR = 'Honza Javorek'
SITENAME = 'Javorové lístky'

if PRODUCTION:
    SITEURL = 'http://honzajavorek.cz'


# URL and save paths settings
URL_PREFIX = 'blog/'
ARTICLE_URL = URL_PREFIX + ARTICLE_URL
ARTICLE_SAVE_AS = URL_PREFIX + ARTICLE_SAVE_AS
ARTICLE_LANG_URL = URL_PREFIX + ARTICLE_LANG_URL
ARTICLE_LANG_SAVE_AS = URL_PREFIX + ARTICLE_LANG_SAVE_AS
INDEX_SAVE_AS = URL_PREFIX + 'index.html'


# Theming
DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = 'UA-1316071-6'
