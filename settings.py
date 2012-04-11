# -*- coding: utf-8 -*- #


# Author & site
AUTHOR = u'Honza Javorek'
SITENAME = u'Javorové lístky'
SITEURL = 'http://www.honzajavorek.cz'
PATH = 'posts'


# Timezone, language
TIMEZONE = 'Europe/Prague'
LOCALE = ('cs_CZ.utf8', 'en_GB.utf8')
DEFAULT_LANG='cs'
DEFAULT_DATE_FORMAT = '%x'


# External services
DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = ''


# Blog settings
REVERSE_TAG_ORDER = True
ARTICLE_PERMALINK_STRUCTURE = '/blog/'
DEFAULT_PAGINATION = 5
DEFAULT_CATEGORY = 'blog'
MD_EXTENSIONS = ['codehilite', 'extra']


# Menu
MENUITEMS = (
    (u'Řehoř', 'http://www.example.com'),
)


# Static paths will be copied under the same name
#STATIC_PATHS = ('css', 'images')


# A list of files to copy from the source to the destination
#FILES_TO_COPY = (
#    ('extra/robots.txt', 'robots.txt'),
#)


# Feeds
CATEGORY_FEED = 'feeds/%s.xml'
TAG_FEED = 'feeds/%s.xml'
FEED_MAX_ITEMS = 10


# Tags
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 50


# Blogroll
LINKS =  (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Jinja2', 'http://jinja.pocoo.org'),
    ('You can modify those links in your config file', '#')
)


# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
)
