import re
import itertools
from pathlib import Path
import importlib
import math
from datetime import date
import csv
from operator import itemgetter
import random
from urllib.parse import urlparse
from textwrap import dedent

import requests
import click
import sqlite_utils
from strava_offline.cli import cli_sqlite as strava_to_sqlite
from slugify import slugify
from telethon.sync import TelegramClient


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
@click.option('--telegram-channel', default='honzajavorekcz')
@click.option('--telegram-app-api-id', envvar='TELEGRAM_APP_API_ID', prompt=True, hide_input=True, type=int)
@click.option('--telegram-app-api-hash', envvar='TELEGRAM_APP_API_HASH', prompt=True, hide_input=True)
@click.option('--strava-skip-sync', is_flag=True, default=False)
@click.option('--strava-client-id', envvar='STRAVA_CLIENT_ID', prompt=True, hide_input=True)
@click.option('--strava-client-secret', envvar='STRAVA_CLIENT_SECRET', prompt=True, hide_input=True)
@click.option('--debug/--no-debug', default=False)
@click.option('--open/--no-open', default=True)
@click.pass_context
def main(context, title, content_path, title_prefix, jobs_api_url, settings_module,
         telegram_channel, telegram_app_api_id, telegram_app_api_hash,
         strava_skip_sync, strava_client_id, strava_client_secret,
         debug, open):
    today = date.today()
    today_cz = f'{today:%-d}. {today:%-m}.'
    today_iso = today.isoformat()

    is_weeknotes = lambda path: slugify(title_prefix) in path.name
    weeknotes_paths = sorted(filter(is_weeknotes, content_path.glob('*.md')))
    last_weeknotes_path = weeknotes_paths[-1]
    last_weeknotes_date = date.fromisoformat(last_weeknotes_path.stem[:10])
    last_weeknotes_date_cz = f'{last_weeknotes_date:%-d}. {last_weeknotes_date:%-m}.'
    last_weeknotes_slug = last_weeknotes_path.stem[11:]
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

    # telegram articles
    articles = get_articles(last_weeknotes_slug, telegram_channel,
                            telegram_app_api_id, telegram_app_api_hash)

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

        **Plány:** Četli jste, co [letos plánuji]({{filename}}2022-12-26_strategie-na-2023.md)?
        Svůj postup zaznamenávám do [tabulky na GitHubu](https://github.com/orgs/juniorguru/projects/1/).
        </div>

        ## Další

        -   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu).
        -   {strava_text}

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

        Když na něco narazím a líbí se mi to, sdílím to [na Telegramu](https://t.me/honzajavorekcz).
        Od posledních poznámek jsem sdílel:

    ''').lstrip()
    for article in articles:
        content += f"- [{article['title']}]({article['url']})"
        content += f"<br>{article['comment']}" if article['comment'] else ''
        content += '\n'

    if debug:
        click.secho(path.name, bold=True)
        click.echo('')
        click.echo(content)
    else:
        path.write_text(content)
        if open:
            click.edit(filename=path)


def get_articles(last_weeknotes_slug, telegram_channel, telegram_app_api_id, telegram_app_api_hash):
    articles = []
    with TelegramClient('weeknotes', telegram_app_api_id, telegram_app_api_hash) as telegram:
        channel = telegram.get_entity(telegram_channel)
        for message in telegram.iter_messages(channel):
            if not message.message:
                continue
            if last_weeknotes_slug in message.message:
                break
            else:
                try:
                    article_url = message.media.webpage.url
                    article_title = get_title_from_webpage(message.media.webpage)
                except AttributeError:
                    article_url = re.search(r'https?://\S+', message.message).group(0)
                    article_title = get_title_from_url(article_url)
                article_comment = message.message.strip().rstrip(article_url).strip()
                if 'overcast.fm' in article_url:
                    article_url = get_canonical_overcast_url(article_url)
                articles.append(dict(title=article_title,
                                     url=article_url,
                                     comment=article_comment))
    return articles


def get_title_from_webpage(webpage):
    try:
        return TITLES[urlparse(webpage.url).hostname]
    except KeyError:
        return webpage.title


def get_title_from_url(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
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
