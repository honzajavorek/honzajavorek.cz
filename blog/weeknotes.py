import json
import re
import itertools
from pathlib import Path
import importlib
import math
from datetime import date, datetime
import csv
from operator import itemgetter
import random
from urllib.parse import urlparse
from textwrap import dedent

from lxml.html import soupparser as html_soup
from lxml import html
import requests
import click
import sqlite_utils
from strava_offline.cli import cli_sqlite as strava_to_sqlite
from slugify import slugify

from blog.update import main as update_command
from blog.toots import main as toots_command


STRAVA_ACTIVITY_TYPES = {
    'run': 'naběhal',
    'walk': 'při procházkách nachodil',
    'hike': 'na túrách nachodil',
    'ride': 'ujel na kole',
    'alpineski': 'sjel na lyžích',
}

TITLES = {
    'www.facebook.com': '(něco na Facebooku)',
    'facebook.com': '(něco na Facebooku)',
    'twitter.com': '(něco na Twitteru)',
    'mobile.twitter.com': '(něco na Twitteru)'
}


@click.command(context_settings={'ignore_unknown_options': True})
@click.argument('title')
@click.option('--path', 'content_path', default='content', type=click.Path(exists=True, path_type=Path))
@click.option('--title-prefix', default='Týdenní poznámky')
@click.option('--jobs-api-url', default='https://junior.guru/api/jobs.csv')
@click.option('--settings-module', default='pelicanconf', type=importlib.import_module)
@click.option('--links-path', default='content/data/toots-links.json', type=click.Path(exists=True, path_type=Path))
@click.option('--strava-skip-sync', is_flag=True, default=False)
@click.option('--strava-client-id', envvar='STRAVA_CLIENT_ID', prompt=True, hide_input=True)
@click.option('--strava-client-secret', envvar='STRAVA_CLIENT_SECRET', prompt=True, hide_input=True)
@click.option('--mastodon-client_id', envvar='MASTODON_CLIENT_ID')
@click.option('--mastodon-client_secret', envvar='MASTODON_CLIENT_SECRET')
@click.option('--mastodon-access_token', envvar='MASTODON_ACCESS_TOKEN')
@click.option('--debug/--no-debug', default=False)
@click.option('--open/--no-open', default=True)
@click.pass_context
def main(context, title, content_path, title_prefix, jobs_api_url, settings_module,
         links_path, strava_skip_sync, strava_client_id, strava_client_secret,
         mastodon_client_id, mastodon_client_secret, mastodon_access_token,
         debug, open):
    context.invoke(update_command)
    context.invoke(toots_command, client_id=mastodon_client_id,
                                  client_secret=mastodon_client_secret,
                                  access_token=mastodon_access_token)

    today = date.today()
    today_cz = f'{today:%-d}. {today:%-m}.'
    today_iso = today.isoformat()

    is_weeknotes = lambda path: slugify(title_prefix) in path.name
    weeknotes_paths = sorted(filter(is_weeknotes, content_path.glob('*.md')))
    last_weeknotes_path = weeknotes_paths[-1]
    last_weeknotes_date = date.fromisoformat(last_weeknotes_path.stem[:10])
    last_weeknotes_date_cz = f'{last_weeknotes_date:%-d}. {last_weeknotes_date:%-m}.'
    prefix = f'{title_prefix}: '

    # jobs
    res = requests.get(jobs_api_url, stream=True)
    res.raise_for_status()
    jobs = [job for job in csv.DictReader(res.iter_lines(decode_unicode=True))
            if job['url'].startswith('https://junior.guru')]
    jobs = sorted(jobs, key=itemgetter('company_name'))
    jobs = {company_name: random.choice(list(company_jobs))
            for company_name, company_jobs
            in itertools.groupby(jobs, key=itemgetter('company_name'))}
    jobs_text = "Aktuální nabídky práce pro juniory: "
    jobs_text += ', '.join([f"[{job['company_name']}]({job['url']})" for job in jobs.values()])

    # mastodon links
    links = get_links(last_weeknotes_date, json.loads(links_path.read_text()))

    # strava
    strava_defaults = {param.name: param.default for param
                       in strava_to_sqlite.get_params(context)}
    if not strava_skip_sync:
        context.invoke(strava_to_sqlite,
                       strava_client_id=strava_client_id,
                       strava_client_secret=strava_client_secret)
    strava_activities = get_strava_activities(strava_defaults['strava_sqlite_database'],
                                              last_weeknotes_date, today)
    strava_stats = calc_strava_stats(strava_activities)
    strava_text = strava_stats_to_text(last_weeknotes_date, today, strava_stats)

    # generate weeknotes
    title = f'{prefix}{title}'
    path = content_path / f'{today_iso}_{slugify(title)}.md'
    last_weeknotes_path = '{filename}' + str(last_weeknotes_path.relative_to(content_path))
    content = dedent(f'''
        Title: {title}
        Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
        Lang: cs
        Tags: {settings_module.WEEKNOTES_TAG}, junior.guru

        Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
        Od [posledních poznámek]({last_weeknotes_path}) už utekl nějaký ten týden ({last_weeknotes_date_cz} až {today_cz}), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

        ![Poznámky]({{static}}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
        Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

        <div class="alert alert-warning" role="alert" markdown="1">
        **Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/open/).
        {jobs_text}

        **Plány:** Četli jste, co [teď plánuji]({{filename}}2023-08-07_letni-pit-stop.md)?
        Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/3/).
        </div>

        ## Další

        -   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn.
        -   {strava_text}
            Detaily na [Strava](https://www.strava.com/athletes/31242569), jediné sociální síti, kde si napsání statusu musíte zasloužit.

        <div class="alert alert-warning" role="alert" markdown="1">
        **Okénko duševního zdraví:**
        Máte dojem, že na rozdíl ode mně nic nestíháte?
        Buďte v klidu, [není to závod]({{filename}}2020-06-04_neni-to-zavod.md)!
        </div>

        ## Plánuji

        1.
        2.
        3.

        ## Zaujalo mě

        Když na něco narazím a líbí se mi to, sdílím to na [svém Mastodonu](https://mastodonczech.cz/@honzajavorek).
        Od posledních poznámek jsem sdílel:

    ''').lstrip()
    for link in links:
        content += f"- [{link['title']}]({link['url']})"
        content += f"<br>{link['comment']}" if link['comment'] else ''
        content += '\n'

    if debug:
        click.secho(path.name, bold=True)
        click.echo('')
        click.echo(content)
    else:
        path.write_text(content)
        if open:
            click.edit(filename=path)


def get_links(since_date: date, links: list):
    for link in links:
        if datetime.fromisoformat(link['created_at']).date() < since_date:
            continue

        html_tree = html_soup.fromstring(link['content'])
        title = None

        if card := link['card']:
            link_url = card['url']
            title = card['title']
        else:
            link_url = html_tree.cssselect('a')[0].get('href')

        if 'overcast.fm' in link_url:
            url = get_canonical_overcast_url(link_url)
        else:
            url = link_url

        if title is None:
            title = get_title_from_url(link_url)

        for element in html_tree.cssselect(f'a[href^="{link_url}"]'):
            element.getparent().remove(element)
        for element in html_tree.cssselect('a[href^="https://mastodonczech.cz/tags/"]'):
            element.getparent().remove(element)
        comment = html_tree.text_content().strip()

        yield dict(title=title,
                   comment=comment,
                   url=url)


def get_title_from_webpage(webpage):
    try:
        return TITLES[urlparse(webpage.url).hostname]
    except KeyError:
        return webpage.title


def get_title_from_url(url):
    response = requests.get(url, stream=True, headers={'User-Agent': 'HonzaJavorekBot (+https://honzajavorek.cz)'})
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        pass
    else:
        for line in response.iter_lines(decode_unicode=True):
            match = re.search(r'<title>([^<]+)', str(line), re.I)
            if match:
                return match.group(1).strip()
    return '(bez titulku)'


def get_canonical_overcast_url(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        if 'rel="canonical"' in line:
            canonical_url = re.search(r'rel="canonical"\s+href="([^"]+)"', line).group(1)
            parts = urlparse(canonical_url)
            if (
                parts.query or
                parts.params or
                parts.fragment or
                parts.path != '/'
            ):
                return canonical_url
    return url


def get_strava_activities(sqlite, start_date, end_date):
    db = sqlite_utils.Database(sqlite)
    return db.query('''
        select * from activity
        where start_date >= ? and start_date <= ?
    ''', [start_date, end_date])


def calc_strava_stats(activities):
    stats = {}
    for activity in activities:
        key = activity['type'].lower()
        stats.setdefault(key, dict(count=0, time=0, distance=0))
        stats[key]['count'] += 1
        stats[key]['time'] += (activity['elapsed_time'] / 60 / 60)  # h
        stats[key]['distance'] += (activity['distance'] / 1000)  # km
    for substats in stats.values():
        substats['time'] = math.ceil(substats['time'])
        substats['distance'] = math.ceil(substats['distance'])

    ordering = list(STRAVA_ACTIVITY_TYPES.keys())
    return dict(sorted(stats.items(), key=lambda item: ordering.index(item[0])))


def strava_stats_to_text(start_date, end_date, stats):
    total_days = (end_date - start_date).days + 1
    text = f"Během {total_days} dní "

    if not stats:
        return text + 'jsem se nevěnoval žádné sportovní aktivitě.'

    parts = [
        f"{STRAVA_ACTIVITY_TYPES[activity_type]} {substats['distance']} km"
        for activity_type, substats in stats.items()
    ]

    total_distance = sum(int(substats['distance']) for substats in stats.values())
    total_time = sum(int(substats['time']) for substats in stats.values())

    text += f"jsem {', '.join(parts)}."
    text += f" Celkem jsem se hýbal {total_time} h a zdolal při tom {total_distance} km."
    return text
