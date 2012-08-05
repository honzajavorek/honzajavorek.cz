# -*- coding: utf-8 -*- #


import re
import json
from datetime import date


# Author & site
AUTHOR = u'Honza Javorek'
SITENAME = u'Javorové lístky'
SITEURL = 'http://honzajavorek.cz'
PATH = 'posts'


# Timezone, language
TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.utf8'
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
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'


# Static paths will be copied under the same name
STATIC_PATHS = ('images', 'files')


# A list of files to copy from the source to the destination
FILES_TO_COPY = (
    ('robots.txt', 'robots.txt'),
    ('404.html', '404.html'),
    ('favicon.ico', 'favicon.ico'),
    ('CNAME', 'CNAME'),
)


# Feeds
FEED = 'feed.xml'
FEED_MAX_ITEMS = 50

FEEDBURNER_SITENAME = 'javorove-listky'


# Theming
THEME = 'theme'
THEME_STATIC_PATHS = ('static',)

DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = 'UA-1316071-6'
TWITTER_USERNAME = 'honzajavorek'

MENUITEMS = ()
LINKS = ()
SOCIAL = ()


# Jinja
def figure(html):
    html = re.sub(r'(<iframe[^\>]*>[^\<]*</iframe>)', r'<figure>\1</figure>', html)
    html = re.sub(r'(<object[^\>]*>.*</object>)', r'<figure>\1</figure>', html)
    return re.sub(r'<p([^\>]*)>\s*(<img[^\>]*>)\s*</p>', r'<figure\1>\2</figure>', html)


def code(html):
    html = re.sub(r'<div[^\>]*class="codehilite"[^\>]*>\s*<pre[^\>]*>', r'<pre class="highlight"><code>', html)
    html = re.sub(r'</pre></div>', r'</code></pre>', html)
    return html


def month_name(month_no):
    return [
        u'leden', u'únor', u'březen',
        u'duben', u'květen', u'červen',
        u'červenec', u'srpen', u'září',
        u'říjen', u'listopad', u'prosinec',
    ][month_no - 1]


def format_date(datetime, format, strip_zeros=True):
    formatted = datetime.strftime(format)
    if strip_zeros:
        return re.sub(r'\b0', '', formatted)
    return formatted


def copyright(year):
    return u'© %s–%s' % (year, date.today().year)


def tojson(*args, **kwargs):
    return json.dumps(*args, **kwargs).replace('/', '\\/')


def has_images(html):
    return re.search(r'<img[^\>]*>', html)


def to_css_class(string):
    return string.replace('-', '_').replace('/', '_')


JINJA_FILTERS = {
    'figure': figure,
    'code': code,
    'month_name': month_name,
    'format_date': format_date,
    'copyright': copyright,
    'tojson': tojson,
    'has_images': has_images,
    'to_css_class': to_css_class,
}
