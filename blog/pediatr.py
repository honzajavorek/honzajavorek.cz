from datetime import date, datetime, timedelta, timezone
import re
from urllib.parse import quote
from zoneinfo import ZoneInfo
from hashlib import sha256

import extruct
import click
from icalendar import Calendar, Event
import requests
from lxml import html
from feedgen.feed import FeedGenerator


PEDIATR_FEED_ID = "XJvA2s26HQP8K6wLnjjx.ucnj"

CZECH_MONTHS = [
    "leden",
    "únor",
    "březen",
    "duben",
    "květen",
    "červen",
    "červenec",
    "srpen",
    "září",
    "říjen",
    "listopad",
    "prosinec",
]


@click.command()
@click.option("--feed-id", default=PEDIATR_FEED_ID)
def main(feed_id: str):
    feed = FeedGenerator()
    feed.id(feed_id)
    feed.title("Dětské Baranova")

    response = requests.get("https://www.detske-baranova.cz/novinky/")
    response.raise_for_status()
    html_tree = html.fromstring(response.content)
    html_tree.make_links_absolute(response.url)

    for article in html_tree.cssselect(".blog"):
        date_text = article.cssselect("span")[0].text_content()
        for month in CZECH_MONTHS:
            date_text = date_text.replace(month, f"{CZECH_MONTHS.index(month) + 1}.")
        if match := re.search(r"\d{1,2}\. \d{1,2}\., \d{4}", date_text):
            published_at = (
                datetime.strptime(match.group(), "%d. %m., %Y")
                .replace(hour=9)
                .replace(tzinfo=timezone.utc)
            )
        else:
            raise ValueError(f"Unparseable date: {date_text}")

        link = article.cssselect("h3 a")[0]
        title = link.text_content().strip()
        url = link.get("href")

        entry = feed.add_entry()
        entry.id(url)
        entry.title(title)
        entry.link(href=url)
        entry.published(published_at)

    click.echo(feed.atom_str())
