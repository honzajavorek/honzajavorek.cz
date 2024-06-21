from itertools import islice
from typing import Iterable
from urllib.parse import urlparse
import click
from notion_client import Client
from notion_client.helpers import iterate_paginated_api

from feedgen.feed import FeedGenerator


NOTION_DATABASE_ID = "6300c201957f499a81ebc9a097950fc8"

NOTION_FEED_ID = "EVVcNQWvn9.QMwn6Z--KMTk4rmJnvNyABKRCcGM@"


@click.group()
def main():
    pass


@main.command()
@click.argument("notion_token", envvar="NOTION_TOKEN")
@click.option("--database-id", default=NOTION_DATABASE_ID)
@click.option("--feed-id", default=NOTION_FEED_ID)
@click.option("--limit", default=100, type=int)
def reading(notion_token: str, database_id: str, feed_id: str, limit: int):
    notion = Client(auth=notion_token)
    items = iterate_paginated_api(notion.databases.query, database_id=database_id)
    feed = FeedGenerator()
    feed.id(feed_id)
    feed.title("HJ's Reading")
    add_feed_items(feed, islice(filter(is_reading_item, items), limit))
    click.echo(feed.atom_str())


@main.command()
@click.argument("notion_token", envvar="NOTION_TOKEN")
@click.option("--database-id", default=NOTION_DATABASE_ID)
@click.option("--feed-id", default=NOTION_FEED_ID)
@click.option("--limit", default=100, type=int)
def watching(notion_token: str, database_id: str, feed_id: str, limit: int):
    notion = Client(auth=notion_token)
    items = iterate_paginated_api(notion.databases.query, database_id=database_id)
    feed = FeedGenerator()
    feed.id(feed_id)
    feed.title("HJ's Watching")
    add_feed_items(feed, islice(filter(is_watching_item, items), limit))
    click.echo(feed.atom_str())


def add_feed_items(feed: FeedGenerator, items: Iterable[dict]):
    for item in items:
        url = get_url(item)
        entry = feed.add_entry()
        entry.id(url)
        entry.title(get_title(item))
        entry.link(href=url)
        entry.published(get_created_at(item))


def is_reading_item(item: dict) -> bool:
    return not is_video_url(item["properties"]["URL"]["url"])


def is_watching_item(item: dict) -> bool:
    return is_video_url(item["properties"]["URL"]["url"])


def is_video_url(url: str) -> bool:
    return (
        "youtube.com" in url
        or "youtu.be" in url
        or "slideslive.com" in url
        or "vimeo.com" in url
    )


def get_url(item: dict) -> str:
    return item["properties"]["URL"]["url"]


def get_title(item: dict) -> str:
    try:
        return item["properties"]["Name"]["title"][0]["plain_text"]
    except IndexError:
        return f"Něco z domény {urlparse(get_url(item)).netloc}"


def get_created_at(item: dict) -> str:
    return item["created_time"]
