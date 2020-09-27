import time
import json
import logging
import itertools
from datetime import datetime, timezone
from pathlib import Path
from operator import attrgetter

from pelican import signals, generators
import feedparser
import strictyaml as yaml


logger = logging.getLogger(__name__)


SCHEMA = yaml.Seq(
    yaml.Map({
        'href': yaml.Url(),
        yaml.Optional('if'): yaml.Str(),
    }),
)


def register():
    signals.get_generators.connect(get_generators)


def get_generators(pelican_object):
    return PocketFeedGenerator


class Item():
    def __init__(self, entry):
        self.title = entry.title
        self.url = entry.link
        self.summary = None

        date = self._parse_datetime(entry, 'published')
        modified = self._parse_datetime(entry, 'updated')
        self.date = date or modified
        self.modified = modified or date

    def _parse_datetime(self, entry, prop_name):
        value = getattr(entry, f'{prop_name}_parsed', None)
        if value:
            return datetime.fromtimestamp(time.mktime(value))
        return None

    def get_content(self, base_url):
        return None


class PocketFeedGenerator(generators.CachingGenerator):
    def generate_output(self, writer):
        if self.settings.get('FEED_POCKET_ATOM'):
            logger.info(f"Generating {self.settings['FEED_POCKET_ATOM']}")

            path = Path('./content/data/pocket_feed_sources.yml')
            feeds = yaml.load(path.read_text(), SCHEMA).data

            items = sorted(filter(attrgetter('date'), [
                Item(entry) for entry
                in itertools.chain.from_iterable(map(parse_feed, feeds))
            ]), key=attrgetter('date'), reverse=True)

            original_urljoiner = writer.urljoiner
            writer.urljoiner = lambda base_url, url: url
            writer.write_feed(
                items,
                self.context,
                self.settings['FEED_POCKET_ATOM'],
                self.settings['FEED_POCKET_ATOM'],
            )
            writer.urljoiner = original_urljoiner


def parse_feed(feed):
    logger.info(f"Parsing {feed['href']}")
    try:
        entries = feedparser.parse(feed['href'])['entries']
    except Exception as e:
        logger.error(f"Couldn't parse {feed['href']}! {e}")
        return []
    else:
        if 'if' in feed:
            return [entry for entry in entries if matches(entry, feed['if'])]
        return entries


def matches(entry, term):
    props = [getattr(entry, prop_name, None)
             for prop_name in ['title', 'author', 'content', 'summary']]
    text = json.dumps([prop for prop in props if prop], ensure_ascii=False)
    return term in text
