# -*- coding: utf-8 -*- #


import re
import os
import sys
import json
import urllib
from datetime import date, datetime, timedelta

import requests
from PIL import Image
from jinja2 import Markup


is_localhost = any(map(lambda x: x in sys.argv,
                       ['-r', '--autoreload', '-D', '--debug']))


# Author & site
AUTHOR = u'Honza Javorek'
SITENAME = u'Javorové lístky'
SITEURL = ('http://localhost/honzajavorek.cz/output'
           if is_localhost else 'http://honzajavorek.cz')
PATH = 'posts'


# Timezone, language
TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.UTF-8'
DEFAULT_LANG = 'cs'
DEFAULT_DATE_FORMAT = '%x'


# Blog settings
DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 80
DEFAULT_CATEGORY = 'blog'
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid']


# URL and save paths settings
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}'
PAGE_LANG_SAVE_AS = '{slug}-{lang}.html'
INDEX_SAVE_AS = 'blog/index.html'
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2}) (?P<slug>.*)'


# Static paths will be copied under the same name
STATIC_PATHS = ('images', 'files')


# A list of files to copy from the source to the destination
FILES_TO_COPY = (
    ('robots.txt', 'robots.txt'),
    # ('404.html', '404.html'),
    ('favicon.ico', 'favicon.ico'),
    ('CNAME', 'CNAME'),
)


# Feeds
FEED_ATOM = 'feed.xml'
FEED_MAX_ITEMS = 50

FEEDBURNER_SITENAME = 'javorove-listky'


# Theming
THEME = 'theme'
THEME_STATIC_PATHS = ('static',)
IMAGE_MAX_WIDTH = 650

DISQUS_SITENAME = 'javorove-listky'
DISQUS_SITENAME_EXPEDITIONS = 'javorove-expedice'
GOOGLE_ANALYTICS = 'UA-1316071-6'
TWITTER_USERNAME = 'honzajavorek'

MENUITEMS = ()
LINKS = ()
SOCIAL = ()


# Plugins
PLUGIN_PATH = 'plugins'
PLUGINS = []


# API key
with open('google_static_maps_api_key') as f:
    GOOGLE_STATIC_MAPS_API_KEY = f.read().strip()


# Jinja
def to_datetime(dt):
    if not isinstance(dt, datetime):
        dt = str(dt)
        try:
            return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return datetime.strptime(dt, '%Y-%m-%d')
    return dt


class FigureCreator(object):

    dirname = os.path.abspath(os.path.dirname(__file__))

    def iframe_to_figure(self, html):
        return re.sub(ur'(<iframe[^\>]*>[^\<]*</iframe>)',
                      ur'<figure>\1</figure>', html)

    def object_to_figure(self, html):
        return re.sub(ur'(<object[^\>]*>.*</object>)',
                      ur'<figure>\1</figure>', html)

    def _replace_image(self, match):
        figure_attrs = match.group(1)
        img_tag = match.group(2)

        match = re.search(ur'src="([^"]+)', img_tag)
        if match:
            # '(../static/)images/something.png'
            path = match.group(1)

            # get dimensions
            filename = os.path.join(
                self.dirname,
                re.sub('.*images/', 'posts/images/', path)
            )
            width = Image.open(filename).size[0]
            if width > IMAGE_MAX_WIDTH:
                width = IMAGE_MAX_WIDTH
            attr = 'width="{0}"'.format(int(width))

            # fix path
            url_path = os.path.join(
                SITEURL,
                re.sub('.*images/', 'static/images/', path)
            )
            img_tag = img_tag.replace(path, url_path)

            # inject width
            img_tag = re.sub(ur'\s*width="[^"]+"\s*', r' ', img_tag)
            img_tag = re.sub(ur'\s*>', ' {0}>'.format(attr), img_tag)

        return u'<figure{0}>{1}</figure>'.format(figure_attrs, img_tag)

    def image_to_figure(self, html):
        return re.sub(ur'<p([^\>]*)>\s*(<img[^\>]*>)\s*</p>',
                      self._replace_image, html)

    def __call__(self, html):
        html = self.iframe_to_figure(html)
        html = self.object_to_figure(html)
        html = self.image_to_figure(html)
        return html


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


def count_days(dt1, dt2, ignore_weekends=False):
    dt1 = to_datetime(dt1)
    dt2 = to_datetime(dt2)
    if ignore_weekends:
        days = (dt1 + timedelta(d + 1) for d in xrange((dt2 - dt1).days))
        return sum(1 for day in days if day.weekday() < 5)
    return (dt2 - dt1).days


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

    def add_path(self, url, places):
        venues = ''
        for i, place in enumerate(places, 65):  # 65 = ASCII code of 'A'
            place_name = self.quote(place)
            if not self.re_coords.match(place):
                url += self.marker_param.format(label=chr(i),
                                                place=place_name)
            venues += self.path_venue.format(place=place_name)
        return url + self.path_param.format(venues=venues)

    def __call__(self, places, width=IMAGE_MAX_WIDTH, height=400):
        url = self.url.format(
            width=width,
            height=height,
            api_key=self.api_key
        )
        url = self.add_path(url, places)

        places = u' → '.join(places)
        return Markup(
            u'<figure><img src="{src}" alt="mapa" '
            u'title="{title}" with="{width}" height="{height}">'
            u'<figcaption>{title}</figcaption></figure>'.format(
                src=url, title=places, width=width, height=height)
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
    'figure': FigureCreator(),
    'code': code,
    'month_name': month_name,
    'format_date': format_date,
    'count_days': count_days,
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
