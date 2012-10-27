# -*- coding: utf-8 -*- #


import re
import json
import requests
from datetime import date, datetime
import urllib
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
SUMMARY_MAX_LENGTH = 80
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


# API key
with open('google_static_maps_api_key') as f:
    GOOGLE_STATIC_MAPS_API_KEY = f.read()


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
    html = re.sub(r'(<iframe[^\>]*>[^\<]*</iframe>)',
                  r'<figure>\1</figure>', html)
    html = re.sub(r'(<object[^\>]*>.*</object>)',
                  r'<figure>\1</figure>', html)
    return re.sub(r'<p([^\>]*)>\s*(<img[^\>]*>)\s*</p>',
                  r'<figure\1>\2</figure>', html)


def code(html):
    html = re.sub(r'<div[^\>]*class="codehilite"[^\>]*>\s*<pre[^\>]*>',
                  r'<pre class="highlight"><code>', html)
    html = re.sub(r'</pre></div>',
                  r'</code></pre>', html)
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
            re_parse = re.compile(
                r'<td[^>]*><a[^>]*>' + re.escape(code) + r'</a></td>\s*'
                r'<td[^>]*><a[^>]*>([^<]+)</a></td>', re.I)
            match = re_parse.search(self.wiki)
            self._cache[code] = match.group(1) if match else ''
        return self._cache[code]


country_name = CountryResolver()


def split(string, separator):
    return re.split(
        r'\s*' + re.escape(unicode(separator)) + r'\s*',
        unicode(string)
    )


def country_flag(code):
    name = country_name(code)
    return Markup(
        u'<img src="{src}/static/images/flags/{code}.png" '
        u'alt="{alt}" title="{title}" with="16" height="11">'.format(
            src=SITEURL, code=code, alt=name, title=name)
    )


def filter_expeditions(pages):
    expeditions = [p for p in pages if p.template == 'expedition']
    return sorted(expeditions, reverse=True,
                  key=lambda x: getattr(x, 'begindate', str(date.today())))


def isoformat(dt):
    return to_datetime(dt).isoformat()


class MapCreator(object):

    api_key = GOOGLE_STATIC_MAPS_API_KEY
    url = 'http://maps.googleapis.com/maps/api/staticmap'\
        '?size={width}x{height}'\
        '&key={api_key}'\
        '&maptype=hybrid'\
        '&sensor=false'
    marker_param = '&markers=color:0xCB0E21%7Clabel:{label}%7C{place}'
    path_param = '&path=color:0xCB0E21%7Cweight:5{venues}'
    path_venue = '%7C{place}'

    re_coords = re.compile(r'\-?\d+(\.\d+)?;\-?\d+(\.\d+)?')
    re_letter = re.compile(r'[A-Z]')

    def quote(self, string):
        return urllib.quote(unicode(string).encode('utf-8'))

    def first_letter(self, string):
        first_letter = string.upper()[0]
        if self.re_letter.match(first_letter):
            return first_letter
        return u'★'

    def add_path(self, url, places):
        venues = ''
        for place in places:
            place_name = self.quote(place)
            if not self.re_coords.match(place):
                first_letter = self.quote(self.first_letter(place))
                url += self.marker_param.format(label=first_letter,
                                                place=place_name)
            venues += self.path_venue.format(place=place_name)
        return url + self.path_param.format(venues=venues)

    def __call__(self, places, width=650, height=400):
        url = self.url.format(
            width=width,
            height=height,
            api_key=self.api_key
        )
        url = self.add_path(url, places)

        places = u' → '.join(places)
        return Markup(
            u'<figure><img src="{src}" alt="{alt}" '
            u'title="{title}" with="{width}" height="{height}">'
            '<figcaption>{title}</figcaption></figure>'.format(
                src=url, alt=places, title=places, width=width, height=height)
        )


class Person:

    fb_link = 'https://www.facebook.com/{id}'
    fb_img = '<img src="https://graph.facebook.com/{id}/picture?type=square"'\
        'width="50" height="50">'
    default_img = '<img src="https://placekitten.com/49/49" '\
        'width="50" height="50">'

    def __init__(self, name, fb_id=None):
        self.name = name
        self.fb_id = fb_id

    @property
    def avatar(self):
        img = self.fb_img if self.fb_id else self.default_img
        return Markup(img.format(id=self.fb_id))

    @property
    def link(self):
        return self.fb_link.format(id=self.fb_id) if self.fb_id else None


def create_person(name):
    parts = re.split(r'\s*\#', name)
    if len(parts) == 2:
        name, fb_id = parts
        return Person(name, fb_id)
    return Person(name)


def split_people(people):
    return sorted(
        map(create_person, split(people, ',')),
        key=lambda x: x.name
    )


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
    'map': MapCreator(),
    'split_people': split_people,
}
