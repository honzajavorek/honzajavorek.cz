
from danube_delta.settings import *  # NOQA


AUTHOR = 'Honza Javorek'
SITENAME = 'Javorové Lístky'

if PRODUCTION:
    SITEURL = 'http://honzajavorek.cz'


# URL and save paths settings
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}.html'
INDEX_SAVE_AS = 'blog/index.html'


# Feeds
FEEDBURNER_SITENAME = 'javorove-listky'


# Theming
THEME = '../theme'

DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = 'UA-1316071-6'
TWITTER_USERNAME = 'honzajavorek'
