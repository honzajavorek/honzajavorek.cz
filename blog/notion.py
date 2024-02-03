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
def reading(notion_token, database_id, feed_id):
    feed = FeedGenerator()
    feed.id(feed_id)
    feed.title("HJ's Reading")
    notion = Client(auth=notion_token)
    for result in iterate_paginated_api(
        notion.databases.query, database_id=database_id
    ):
        for item in result:
            url = item["properties"]["URL"]["url"]
            if is_video_url(url):
                continue

            title = item["properties"]["Name"]["title"][0]["plain_text"]
            created_at = item["created_time"]
            entry = feed.add_entry()
            entry.id(url)
            entry.title(title)
            entry.link(href=url)
            entry.published(created_at)
    click.echo(feed.atom_str())


@main.command()
@click.argument("notion_token", envvar="NOTION_TOKEN")
@click.option("--database-id", default=NOTION_DATABASE_ID)
@click.option("--feed-id", default=NOTION_FEED_ID)
def watching(notion_token, database_id, feed_id):
    feed = FeedGenerator()
    feed.id(feed_id)
    feed.title("HJ's Watching")
    notion = Client(auth=notion_token)
    for result in iterate_paginated_api(
        notion.databases.query, database_id=database_id
    ):
        for item in result:
            url = item["properties"]["URL"]["url"]
            if not is_video_url(url):
                continue

            title = item["properties"]["Name"]["title"][0]["plain_text"]
            created_at = item["created_time"]
            entry = feed.add_entry()
            entry.id(url)
            entry.title(title)
            entry.link(href=url)
            entry.published(created_at)
    click.echo(feed.atom_str())


def is_video_url(url: str) -> bool:
    return "youtube.com" in url or "youtu.be" in url
