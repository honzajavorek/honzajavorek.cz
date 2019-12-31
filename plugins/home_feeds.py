import time
import itertools
import logging
from datetime import datetime, timezone
from pathlib import Path
from operator import itemgetter

from pelican import signals
import feedparser
import strictyaml as yaml


logger = logging.getLogger(__name__)


SCHEMA = yaml.Seq(
    yaml.Map({
        'title': yaml.Str(),
        'link': yaml.Url(),
        'href': yaml.Url(),
    }),
)


def register():
    signals.article_generator_finalized.connect(load_feeds)


def load_feeds(article_generator):
    settings = article_generator.settings

    # external feeds
    path = Path('./content/data/feeds.yml')
    feeds = yaml.load(path.read_text(), SCHEMA).data
    entries = itertools.chain.from_iterable(map(parse_feed, feeds))

    # add blog feed and prepare articles using the article_generator
    url = settings.get('FEED_ALL_ATOM_URL', settings['FEED_ALL_ATOM'])
    blog_feed = dict(
        title='blog',
        link=f"{settings['SITEURL']}/blog/",
        href=f"{settings['FEED_DOMAIN']}/{path}",
    )
    feeds = [blog_feed] + feeds
    entries = itertools.chain(entries, (
        dict(
            title=article.title,
            link=f"{settings['SITEURL']}/{article.url}",
            date=article.date.date(),
            feed_title=blog_feed['title'],
            feed_link=blog_feed['link'],
        )
        for article in article_generator.articles
    ))

    # sort entries
    entries = list(sorted(entries, key=itemgetter('date'), reverse=True))

    # set context variables
    article_generator.context['feeds_entries'] = entries
    article_generator.context['feeds'] = feeds


def parse_feed(feed):
    logger.info(f"Parsing {feed['href']}")
    return (
        dict(
            title=entry.title,
            link=entry.link,
            date=datetime.fromtimestamp(time.mktime(entry.published_parsed)).date(),
            feed_title=feed['title'],
            feed_link=feed['link'],
        )
        for entry in feedparser.parse(feed['href'])['entries']
    )
