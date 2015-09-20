# -*- coding: utf-8 -*- #

import re
import os
import json
from datetime import date, datetime, timedelta

# from tipi import tipi
from PIL import Image


IMAGE_MAX_WIDTH = 1024
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def tipi(html):
    return html


def to_datetime(dt):
    if not isinstance(dt, datetime):
        dt = str(dt)
        try:
            return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return datetime.strptime(dt, '%Y-%m-%d')
    return dt


def iframe_to_figure(html):
    return re.sub(ur'(<iframe[^\>]*>[^\<]*</iframe>)',
                  ur'<figure>\1</figure>', html)


def object_to_figure(html):
    return re.sub(ur'(<object[^\>]*>.*</object>)',
                  ur'<figure>\1</figure>', html)


def image_to_figure(html):
    def replace_image(match):
        figure_attrs, img_tag = match.group(1), match.group(2)

        match = re.search(ur'src="([^"]+)', img_tag)
        if match:
            # '(../static/)images/something.png'
            path = match.group(1)

            # get dimensions
            filename = os.path.join(
                PROJECT_DIR,
                re.sub('.*images/', 'content/images/', path)
            )
            width = Image.open(filename).size[0]
            if width > IMAGE_MAX_WIDTH:
                width = IMAGE_MAX_WIDTH
            attr = 'width="{0}"'.format(int(width))

            # inject width
            img_tag = re.sub(ur'\s*width="[^"]+"\s*', r' ', img_tag)
            img_tag = re.sub(ur'\s*>', ' {0}>'.format(attr), img_tag)

        return u'<figure{0}>{1}</figure>'.format(figure_attrs, img_tag)

    return re.sub(ur'<p([^\>]*)>\s*(<img[^\>]*>)\s*</p>', replace_image, html)


def figure(html):
    html = iframe_to_figure(html)
    html = object_to_figure(html)
    html = image_to_figure(html)
    return html


def code(html):
    html = re.sub(r'<div[^\>]*class="highlight"[^\>]*>\s*<pre[^\>]*>',
                  r'<pre class="highlight"><code>', html)
    html = re.sub(r'</pre>\s*</div>',
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
    return string.replace('_', '-').replace('/', '-')


filters = {
    'figure': figure,
    'code': code,
    'month_name': month_name,
    'format_date': format_date,
    'count_days': count_days,
    'copyright': copyright,
    'tojson': tojson,
    'has_images': has_images,
    'to_css_class': to_css_class,
    'typography': tipi,
}
