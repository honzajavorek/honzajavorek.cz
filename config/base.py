
import os
import sys

CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))
THEME_DIR = os.path.join(CONFIG_DIR, '..', 'theme')
sys.path.append(THEME_DIR)

from templating import filters, IMAGE_MAX_WIDTH  # NOQA


AUTHOR = 'Honza Javorek'
SITENAME = 'Javorové Lístky'


# Timezone, language
TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.UTF-8'
DEFAULT_LANG = 'cs'
DEFAULT_DATE_FORMAT = '%x'


# Blog settings
PATH = 'content'
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 80
DEFAULT_CATEGORY = 'blog'
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'headerid', 'extra']


# URL and save paths settings
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_LANG_URL = '{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
URL_EXT = ''
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'


# Static paths will be copied under the same name
STATIC_PATHS = (
    'images',
    'files',
    'robots.txt',
    'favicon.ico',
    'CNAME',
)


# Feeds
FEED_ALL_ATOM = 'feed.xml'
FEED_MAX_ITEMS = 50

FEEDBURNER_SITENAME = 'javorove-listky'

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Theming
THEME = '../theme'
THEME_STATIC_PATHS = ('../static',)
JINJA_FILTERS = filters

DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = 'UA-1316071-6'
TWITTER_USERNAME = 'honzajavorek'

MENUITEMS = ()
LINKS = ()
SOCIAL = ()
