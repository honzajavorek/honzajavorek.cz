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
        'lang': yaml.Enum(['en', 'cs']),
        'link': yaml.Url(),
        'href': yaml.Url(),
    }),
)


def register():
    signals.article_generator_finalized.connect(load_feeds)


def load_feeds(article_generator):
    settings = article_generator.settings
    articles = article_generator.articles

    # prepare blog articles
    blog_feed_path = settings.get('FEED_ALL_ATOM_URL', settings['FEED_ALL_ATOM'])
    blog_feed = dict(
        title='blog',
        lang='en',
        link=f"{settings['SITEURL']}/blog/",
        href=f"{settings['FEED_DOMAIN']}/{blog_feed_path}",
    )
    blog_entries = [
        dict(
            title=article.title,
            lang=article.lang,
            link=f"{settings['SITEURL']}/{article.url}",
            date=article.date.date(),
            feed_title=blog_feed['title'],
            feed_link=blog_feed['link'],
            translations=[
                dict(
                    title=translation.title,
                    lang=translation.lang,
                    link=f"{settings['SITEURL']}/{translation.url}",
                    date=translation.date.date(),
                    feed_title=blog_feed['title'],
                    feed_link=blog_feed['link'],
                )
                for translation in article.translations
            ],
            alternates=[],
        )
        for article in articles
        if 'týdenní poznámky' not in [tag.name for tag in getattr(article, 'tags', [])]
    ]

    # create a lookup mapping of alternate entries
    alternates_mapping = dict(itertools.chain.from_iterable(
        ((alternate['url'], i) for alternate in article.alternates)
        for i, article in enumerate(articles)
    ))

    # external feeds
    path = Path('./content/data/feeds.yml')
    feeds = yaml.load(path.read_text(), SCHEMA).data

    entries = []
    for entry in itertools.chain.from_iterable(map(parse_feed, feeds)):
        try:
            i = alternates_mapping[entry['link']]
        except KeyError:
            entries.append(entry)
        else:
            blog_entries[i]['alternates'].append(entry)

    # merge & sort entries
    feeds_entries = sorted(blog_entries + entries,
                           key=itemgetter('date'),
                           reverse=True)

    # set context variables
    article_generator.context['feeds_entries'] = feeds_entries
    article_generator.context['feeds'] = [blog_feed] + feeds


def parse_feed(feed):
    logger.info(f"Parsing {feed['href']}")
    return (
        dict(
            title=entry.title,
            lang=feed['lang'],
            link=normalize_link(entry.link),
            date=datetime.fromtimestamp(time.mktime(entry.published_parsed)).date(),
            feed_title=feed['title'],
            feed_link=feed['link'],
        )
        for entry in feedparser.parse(feed['href'])['entries']
    )


def normalize_link(link):
    # remove params, because they only contain tracking info (utm_ etc.)
    return link.split('?')[0]
