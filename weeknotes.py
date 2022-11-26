import re
import itertools
from operator import itemgetter
import os
import random
import sys
import csv
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlparse

from slugify import slugify
import requests
from telethon.sync import TelegramClient

sys.path.append(os.curdir)
import pelicanconf
import strava


DEBUG = os.getenv('DEBUG')
TITLE_PREFIX = 'Týdenní poznámky'
CONTENT_PATH = Path(pelicanconf.PATH)
TELEGRAM_CHANNEL_NAME = 'honzajavorekcz'
TELEGRAM_APP_API_ID = int(os.environ['TELEGRAM_APP_API_ID'])
TELEGRAM_APP_API_HASH = os.environ['TELEGRAM_APP_API_HASH']


today = date.today()
today_cz = f'{today:%d}. '.lstrip('0') + f'{today:%m}.'.lstrip('0')
today_iso = today.isoformat()

is_weeknotes = lambda path: slugify(TITLE_PREFIX) in path.name
weeknotes_paths = sorted(filter(is_weeknotes, CONTENT_PATH.glob('*.md')))
last_weeknotes_path = weeknotes_paths[-1]
last_weeknotes_date = date.fromisoformat(last_weeknotes_path.stem[:10])
last_weeknotes_slug = last_weeknotes_path.stem[11:]

start_date = last_weeknotes_date + timedelta(days=1)
start_date_cz = f'{start_date:%d}. '.lstrip('0') + f'{start_date:%m}.'.lstrip('0')

number = len(weeknotes_paths) + 1
prefix = f'{TITLE_PREFIX} #{number}: '

res = requests.get('https://junior.guru/api/jobs.csv', stream=True)
res.raise_for_status()
jobs = [job for job in csv.DictReader(res.iter_lines(decode_unicode=True))
        if job['url'].startswith('https://junior.guru')]
jobs = sorted(jobs, key=itemgetter('company_name'))
jobs = {company_name: random.choice(list(company_jobs))
        for company_name, company_jobs
        in itertools.groupby(jobs, key=itemgetter('company_name'))}
jobs_text = "Nabídky práce pro juniory teď inzerují: "
jobs_text += ', '.join([f"[{job['company_name']}]({job['url']})" for job in jobs.values()])

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

def get_title(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        match = re.search(r'<title>([^<]+)', str(line), re.I)
        if match:
            return match.group(1).strip()
    return '(bez titulku)'

articles = []
with TelegramClient('weeknotes', TELEGRAM_APP_API_ID, TELEGRAM_APP_API_HASH) as telegram:
    channel = telegram.get_entity(TELEGRAM_CHANNEL_NAME)
    for message in telegram.iter_messages(channel):
        if last_weeknotes_slug in message.message:
            break
        else:
            try:
                article_url = message.media.webpage.url
                article_title = message.media.webpage.title
            except AttributeError:
                article_url = re.search(r'https?://\S+', message.message).group(0)
                article_title = get_title(article_url)
            if 'overcast.fm' in article_url:
                article_url = get_canonical_overcast_url(article_url)
            article_comment = message.message.strip().rstrip(article_url).strip()
            articles.append(dict(title=article_title,
                                 url=article_url,
                                 comment=article_comment))


activities = strava.get_activities(strava.get_access_token())
activities_stats = strava.calc_stats(strava.filter_by_dates(activities, start_date, today))
activities_text = strava.stats_to_text(start_date, today, activities_stats)

if len(sys.argv) > 1:
    highlights = ' '.join(sys.argv[1:])
else:
    highlights = input(prefix)

title = f'{prefix}{highlights}'
path = CONTENT_PATH / f'{today_iso}_{slugify(title)}.md'
last_weeknotes_path = '{filename}/' + str(last_weeknotes_path.relative_to(CONTENT_PATH))
content = f'''
Title: {title}
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Tags: {pelicanconf.WEEKNOTES_TAG}


Utekl zase nějaký ten týden ({start_date_cz} až {today_cz}) a tak [stejně jako minule]({last_weeknotes_path}) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [klub](https://junior.guru/club/), a členy by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase konec týdne a já jsem přitom nestihl nic udělat.

![Poznámky]({{static}}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Další poznámky

- Odpovídání v klubu, maily, Pyvec Slack, a tak dále. Upgradování závislostí na vlastních i Pyvec projektech (zpracovávání Pull Requestů, které průběžně posílá Dependabot).
- {activities_text}
- Aktuální finanční výsledky, návštěvnost a další čísla k JG [mám přímo na webu](https://junior.guru/open/). {jobs_text}


## Co plánuji

Tři věci, které bych chtěl zvládnout udělat příště:

1.
2.
3.


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({{filename}}2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Telegramu](https://t.me/honzajavorekcz). Není to vše, co jsem přečetl, slyšel nebo viděl, ale jen zlomek, který mě zaujal. Od posledních poznámek jsem sdílel toto:

'''.lstrip()
for article in articles:
    content += f"- [{article['title']}]({article['url']})"
    content += f"<br>{article['comment']}" if article['comment'] else ''
    content += '\n'

if DEBUG:
    print('-' * 80)
    print(path.name)
    print('-' * 80)
    print(content)
    print('-' * 80)
else:
    path.write_text(content)
