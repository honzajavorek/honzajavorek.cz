from datetime import datetime, timedelta
from urllib.parse import quote
from zoneinfo import ZoneInfo
from hashlib import sha256

import extruct
import click
from icalendar import Calendar, Event
import requests
from lxml import html


CALENDAR_UID_SEED = '4v6CadZyePtkN*ciL4w*9uVn62vKH8WPPy-44p8V'

HEADING_PREFIX = 'Kočárkino: '


@click.command()
def main():
    calendar = Calendar()
    calendar.add('prodid', '-//kocarkino//honzajavorek.cz//')
    calendar.add('version', '2.0')
    calendar.add('uid', sha256(CALENDAR_UID_SEED.encode('utf-8')).hexdigest())

    response = requests.get('https://kcvozovna.cz/program/')
    response.raise_for_status()
    html_tree = html.fromstring(response.content)
    for row in html_tree.cssselect('[data-date]'):
        starts_at = datetime \
            .fromisoformat(row.get('data-date')) \
            .replace(tzinfo=ZoneInfo('Europe/Prague'))
        link = row.cssselect('h2 a')[0]
        url = link.get('href')

        heading = link.text_content().strip()
        if heading.startswith(HEADING_PREFIX):
            title = heading.replace(HEADING_PREFIX, '')
            csfd_url = f'https://www.csfd.cz/hledat/?q={quote(title)}'

            event = Event()
            event.add('uid', sha256(url.encode('utf-8')).hexdigest())
            event.add('dtstamp', datetime.utcnow())
            event.add('summary', f'Kočárkino: {title}')
            event.add('description', '\n'.join([url, csfd_url]))
            event.add('dtstart', starts_at)
            event.add('duration', timedelta(hours=2))
            event.add('location', 'KC VOZOVNA, Koněvova 2687/164, Praha 3')
            calendar.add_component(event)

    response = requests.post('https://www.biooko.net/api_program', data={
        'cinema[]': 2,
        'cycle[]': 'baby-bio',
        '_locale': 'cs',
    })
    response.raise_for_status()
    for data in extruct.extract(response.text)['json-ld']:
        csfd_url = f"https://www.csfd.cz/hledat/?q={quote(data['name'])}"

        event = Event()
        event.add('uid', sha256(data['url'].encode('utf-8')).hexdigest())
        event.add('dtstamp', datetime.utcnow())
        event.add('summary', f"Baby Bio: {data['name']}")
        event.add('description', '\n'.join([data['url'], csfd_url]))
        event.add('dtstart', datetime \
            .fromisoformat(data['startDate']) \
            .replace(tzinfo=ZoneInfo('Europe/Prague')))
        event.add('duration', timedelta(hours=2))
        event.add('location', 'Bio Oko, Františka Křížka 460/15, Praha 7')
        calendar.add_component(event)

    click.echo(calendar.to_ical())
