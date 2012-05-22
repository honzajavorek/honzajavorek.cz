# -*- coding: utf-8 -*- #


# Author & site
AUTHOR = u'Honza Javorek'
SITENAME = u'Javorové lístky'
SITEURL = 'http://honzajavorek.cz'
PATH = 'posts'


# Timezone, language
TIMEZONE = 'Europe/Prague'
LOCALE = ('cs_CZ.utf8', 'en_GB.utf8')
DEFAULT_LANG = 'cs'
DEFAULT_DATE_FORMAT = '%x'


# Blog settings
DEFAULT_PAGINATION = 5
DEFAULT_CATEGORY = 'blog'
MD_EXTENSIONS = ['codehilite', 'extra', 'headerid']


# URL and save paths settings
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'


# Static paths will be copied under the same name
STATIC_PATHS = ('images', 'files')


# Theming
THEME = 'theme'
THEME_STATIC_PATHS = ('static',)
CSS_FILE = 'main.css'

DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = 'UA-1316071-6'
TWITTER_USERNAME = 'honzajavorek'

MENUITEMS = ()
LINKS = ()
SOCIAL = ()


# A list of files to copy from the source to the destination
FILES_TO_COPY = (
    ('robots.txt', 'robots.txt'),
    ('404.html', '404.html'), # TODO
    ('index.html', 'index.html'), # temporary
    ('CNAME', 'CNAME'),
)


# Feeds
FEED = 'feed.xml'
FEED_MAX_ITEMS = 50

FEEDBURNER_URL = 'http://feeds.honzajavorek.cz/blog/all'

