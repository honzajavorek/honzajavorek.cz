# -*- coding: utf-8 -*- #


import re
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
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'


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

FEEDBURNER_URL = 'http://feeds.honzajavorek.cz/blog/all'
FEEDBURNER_MAIL_URL = 'http://feedburner.google.com/fb/a/mailverify?uri=blog/all&loc=cs_CZ'


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

JINJA_FILTERS = {
    'figure': figure,
    'code': code,
    'month_name': month_name,
    'format_date': format_date,
    'copyright': copyright,
}
