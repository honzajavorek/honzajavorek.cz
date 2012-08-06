# -*- coding: utf-8 -*- #


import re
import json
import requests
from datetime import date, datetime
from jinja2 import Markup


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
def to_datetime(dt):
    if not isinstance(dt, datetime):
        dt = str(dt)
        try:
            return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return datetime.strptime(dt, '%Y-%m-%d')
    return dt


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


def format_date(dt, format, strip_zeros=True):
    formatted = to_datetime(dt).strftime(format)
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


class CountryResolver(object):

    wiki_url = 'https://cs.wikipedia.org/wiki/ISO_3166-1'

    _wiki = None
    _cache = {}

    @property
    def wiki(self):
        if not self._wiki:
            r = requests.get(self.wiki_url)
            r.raise_for_status()
            self._wiki = r.text
        return self._wiki

    def __call__(self, code):
        if not code in self._cache:
            re_parse = re.compile(r'<td[^>]*><a[^>]*>' + re.escape(code) + r'</a></td>\s*' +\
                r'<td[^>]*><a[^>]*>([^<]+)</a></td>', re.I)
            match = re_parse.search(self.wiki)
            self._cache[code] = match.group(1) if match else ''
        return self._cache[code]


country_name = CountryResolver()


def split(string, separator):
    return re.split(
        re.escape(unicode(separator)) + r'\s*',
        unicode(string)
    )


def country_flag(code):
    return Markup(
        '<img src="{}/static/images/flags/{}.png" alt="{}">'\
        .format(SITEURL, code, country_name(code))
    )


def filter_expeditions(pages):
    expeditions = [p for p in pages if p.template == 'expedition']
    return sorted(expeditions,
        reverse=True,
        key=lambda x: getattr(x, 'begindate', str(date.today()))
    )


def isoformat(dt):
    return to_datetime(dt).isoformat()


JINJA_FILTERS = {
    'figure': figure,
    'code': code,
    'month_name': month_name,
    'format_date': format_date,
    'copyright': copyright,
    'tojson': tojson,
    'has_images': has_images,
    'to_css_class': to_css_class,
    'split': split,
    'country_name': country_name,
    'country_flag': country_flag,
    'filter_expeditions': filter_expeditions,
    'isoformat': isoformat,
}
