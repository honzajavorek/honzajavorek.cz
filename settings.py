# -*- coding: utf-8 -*- #


# Author & site
AUTHOR = u'Honza Javorek'
SITENAME = u'Javorové lístky'
SITEURL = 'http://www.honzajavorek.cz'
PATH = 'posts'


# Timezone, language
TIMEZONE = 'Europe/Prague'
LOCALE = ('cs_CZ.utf8', 'en_GB.utf8')
DEFAULT_LANG = 'cs'
DEFAULT_DATE_FORMAT = '%x'


# External services
DISQUS_SITENAME = 'javorove-listky'


# Blog settings
DEFAULT_PAGINATION = 5
DEFAULT_CATEGORY = 'blog'
MD_EXTENSIONS = ['codehilite', 'extra', 'headerid']


# URL settings
ARTICLE_URL = '{slug}'
ARTICLE_LANG_URL = '{slug}-{lang}'
PAGE_URL = 'pages/{slug}'
PAGE_LANG_URL = 'pages/{slug}-{lang}'


# Static paths will be copied under the same name
STATIC_PATHS = ('images', 'files')


# A list of files to copy from the source to the destination
FILES_TO_COPY = (
    ('robots.txt', 'robots.txt'),
    ('404.html', '404.html'), # TODO
    ('index.html', 'index.html'), # temporary
    ('CNAME', 'CNAME'),
)


# Feeds
FEED_MAX_ITEMS = 38

