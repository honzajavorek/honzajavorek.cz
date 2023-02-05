from datetime import datetime, timedelta
from urllib.parse import quote
from zoneinfo import ZoneInfo

import click
from icalendar import Calendar, Event
import requests
from lxml import html


HEADING_PREFIX = 'Kočárkino: '


@click.command()
def main():
    response = requests.get('https://kcvozovna.cz/program/')
    response.raise_for_status()
    html_tree = html.fromstring(response.content)

    calendar = Calendar()
    calendar.add('prodid', '-//kocarkino//honzajavorek.cz//')
    calendar.add('version', '2.0')

    for event in html_tree.cssselect('[data-date]'):
        starts_at = datetime \
            .fromisoformat(event.get('data-date')) \
            .replace(tzinfo=ZoneInfo('Europe/Prague'))
        link = event.cssselect('h2 a')[0]
        url = link.get('href')

        heading = link.text_content().strip()
        if heading.startswith(HEADING_PREFIX):
            title = heading.replace(HEADING_PREFIX, '')
            csfd_url = f'https://www.csfd.cz/hledat/?q={quote(title)}'

            event = Event()
            event.add('summary', heading)
            event.add('description', '\n'.join([title, url, csfd_url]))
            event.add('dtstart', starts_at)
            event.add('duration', timedelta(hours=2))
            event.add('location', 'KC VOZOVNA, Koněvova 2687/164, 13000 Praha 3')
            calendar.add_component(event)

    click.echo(calendar.to_ical())
