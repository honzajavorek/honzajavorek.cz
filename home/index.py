import os
import time
import shutil
import itertools
import hashlib
from datetime import datetime
from operator import itemgetter
from functools import wraps

import sass
import yaml
import json
import requests
import feedparser
from lxml import html
from flask import Flask, render_template, send_file
from werkzeug.contrib.cache import FileSystemCache


app = Flask(__name__)


dredd_stars_before = 650
dredd_stars_after = 2650

feeds = [
    {
        'title': 'blog',
        'link': 'http://honzajavorek.cz/blog',
        'href': 'http://honzajavorek.cz/feed.xml',
    },
    {
        'title': 'medium.com',
        'link': 'https://medium.com/@honzajavorek',
        'href': 'https://medium.com/feed/@honzajavorek',
    },
    {
        'title': 'dev.to',
        'link': 'https://dev.to/honzajavorek',
        'href': 'https://dev.to/feed/honzajavorek',
    },
    {
        'title': 'zdrojak.cz',
        'link': 'https://www.zdrojak.cz/autori/honza-javorek/',
        'href': 'https://www.zdrojak.cz/autori/honza-javorek/feed/',
    },
]

appearance_icons = {
    'talk': 'comment-o',
    'workshop': 'code',
    'interview': 'microphone',
    'slides': 'television',
    'text': 'file-text-o',
}

appearances = []


cache = FileSystemCache('cache', default_timeout=0)


def cached(fn):
    if app.config.get('ENV') == 'production':
        return fn

    @wraps(fn)
    def wrapper(*args, **kwargs):
        key = fn.__name__ + json.dumps(args) + json.dumps(kwargs)
        value = cache.get(key)
        if value is None:
            value = fn(*args, **kwargs)
            cache.set(key, value)
        return value
    return wrapper


@app.before_first_request
def before_first_request():
    with open('appearances.yml') as f:
        appearances.extend(get_appearances(f))


@app.route('/')
def index():
    return render_template(
        'index.html',
        dredd_stars_raise=round(dredd_stars_after / dredd_stars_before),
        feeds=feeds,
        articles=get_articles(map(parse_feed, feeds)),
        appearances=appearances,
        repos=get_pinned_repos(
            parse_html(request_github_profile('honzajavorek'))),
    )


def get_articles(parsed_feeds):
    entries = itertools.chain.from_iterable(
        (
            # add certain feed-level values to each article
            dict(
                feed_title=parsed_feed['feed']['title'],
                feed_link=parsed_feed['feed']['link'],
                **entry,
            )
            for entry in parsed_feed['entries']
        )
        for parsed_feed in parsed_feeds
    )
    entries = sorted(entries, key=itemgetter('published_parsed'), reverse=True)
    return list(merge_republished_articles(entries))


def merge_republished_articles(articles):
    feeds_order = [feed['link'] for feed in feeds]
    def article_to_sort_key(article):
        return feeds_order.index(article['feed_link'])

    for key, entries in itertools.groupby(articles, key=article_to_group_key):
        entries = list(entries)
        primary_entry = entries[0]
        primary_entry['republished'] = []

        if len(entries) > 1:
            entries = sorted(entries, key=article_to_sort_key)
            primary_entry = entries[0]
            primary_entry['republished'] = entries[1:]

        yield primary_entry


def article_to_group_key(article):
    return (
        article['title'],
        article['published_parsed'].tm_year,
        article['published_parsed'].tm_mon,
    )


@cached
def parse_feed(feed):
    parsed_feed = feedparser.parse(feed['href'])

    # override certain values by custom ones
    parsed_feed['href'] = feed['href']
    parsed_feed['feed']['title'] = feed['title']
    parsed_feed['feed']['link'] = feed['link']

    return parsed_feed


def get_pinned_repos(html_tree):
    for repo_tree in html_tree.cssselect('.pinned-repo-item'):
        try:
            owner = repo_tree.cssselect('.owner')[0].text_content()
        except IndexError:
            owner = 'honzajavorek'

        desc = repo_tree.cssselect('.pinned-repo-desc')[0].text_content()
        desc_en = desc.split(' / ')[0]

        yield dict(
            owner=owner,
            name=repo_tree.cssselect('.repo')[0].text_content(),
            url=repo_tree.cssselect('a')[0].get('href'),
            description=desc_en,
        )


def parse_html(response):
    html_tree = html.fromstring(response.content)
    html_tree.make_links_absolute(response.url)
    return html_tree


@cached
def request_github_profile(username):
    response = requests.get('https://github.com/' + username)
    response.raise_for_status()
    return response


def get_appearances(yaml_load_input):
    appearances = yaml.safe_load(yaml_load_input)
    coerced_appearances = map(coerce_appearance, appearances)
    return sorted(coerced_appearances, key=itemgetter('date'), reverse=True)


def coerce_appearance(appearance):
    date = datetime.strptime(appearance['date'], '%Y-%m-%d').date()
    appearance['date'] = date
    appearance.setdefault('type', 'talk')
    appearance.setdefault('resources_type', 'slides')
    appearance.setdefault('lang', 'cs')
    return appearance


@app.route('/favicon.ico')
def favicon():
    return send_file(f'static/favicon.ico')


@app.route('/static/avatar.png')
def avatar():
    hash = hashlib.md5(b'mail@honzajavorek.cz').hexdigest()
    size = 150
    response = requests.get(f'https://www.gravatar.com/avatar/{hash}?s={size}')
    response.raise_for_status()
    return response.content, 200, {'content-type': 'image/png'}


@app.route('/static/css/main.css')
def css():
    """A poor man's webpack"""

    if not os.path.isdir('static/fonts'):
        shutil.copytree('node_modules/fork-awesome/fonts', 'static/fonts')

    with open('static/css/main.scss') as f:
        source = f.read().strip()
    css = sass.compile(string=source, output_style='compressed')

    return css, 200, {'content-type': 'text/css'}


@app.template_filter('month')
def month_filter(d):
    return d.strftime('%b')


@app.template_filter('struct_time_to_dt')
def struct_time_to_dt(struct_time):
    return datetime.fromtimestamp(time.mktime(struct_time))


@app.template_filter('appearance_icon')
def appearance_icon_filter(t):
    return appearance_icons[t]


if __name__ == '__main__':
    from elsa import cli
    app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
    cli(app, base_url='http://honzajavorek.cz')
