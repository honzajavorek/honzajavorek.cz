import re
import os
import sys
from datetime import date, timedelta
from pathlib import Path

from slugify import slugify
import pocket_recommendations
import requests

sys.path.append(os.curdir)
import pelicanconf


DEBUG = os.getenv('DEBUG')
TITLE_PREFIX = 'Týdenní poznámky'
CONTENT_PATH = Path(__file__).parent / pelicanconf.PATH


today = date.today()

is_weeknotes = lambda path: slugify(TITLE_PREFIX) in path.name
weeknotes_paths = sorted(filter(is_weeknotes, CONTENT_PATH.glob('*.md')))
last_weeknotes_path = weeknotes_paths[-1]
last_weeknotes_date = date.fromisoformat(last_weeknotes_path.name[:10])

number = len(weeknotes_paths) + 1
prefix = f'{TITLE_PREFIX} #{number}: '

res = requests.get('https://getpocket.com/@honzajavorek')
res.raise_for_status()
articles = [a for a in pocket_recommendations.parse(res.content, today=today)
            if a['pocket_recommended_at'] >= last_weeknotes_date]
articles.reverse()

if len(sys.argv) > 1:
    highlights = ' '.join(sys.argv[1:])
else:
    highlights = input(prefix)

title = f'{prefix}{highlights}'
slug = slugify(title)

monday = today - timedelta(today.weekday())
monday_cz = f'{monday:%d}.'.lstrip('0') + f'{monday:%m}.'.lstrip('0')
friday = today + timedelta(days=4 - today.weekday())
friday_cz = f'{friday:%d}.'.lstrip('0') + f'{friday:%m}.'.lstrip('0')
friday_iso = friday.isoformat()

path = CONTENT_PATH / f'{friday_iso}_{slug}.md'
last_weeknotes_path = str(last_weeknotes_path).replace('content', '{filename}')
content = f'''
Title: {title}
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs
Home: False


Utekl další týden ({monday_cz} — {friday_cz}) a tak [stejně jako minule]({last_weeknotes_path}) sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({{static}}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)


## Další poznámky

-
-


## A co vy?

Pokud byste čistě náhodou měli dojem, že jste oproti mě za uplynulý týden vůbec nic nestihli, tak mám pro vás skvělou zprávu! V klidu se na ten dojem [můžete vykašlat]({{filename}}/2020-06-04_neni-to-zavod.md). Není zač!


## Co mě zaujalo

Když si něco přečtu nebo poslechnu a líbí se mi to, [sdílím to na Pocketu](https://getpocket.com/@honzajavorek). Od posledních poznámek jsem sdílel toto:

'''.lstrip()
for article in articles:
    content += f"- [{article['title']}]({article['pocket_url']})"
    content += f"<br>{article['pocket_comment']}" if article['pocket_comment'] else ''
    content += '\n'
content += '''
<small>Vygenerováno pomocí <a href="https://pypi.org/project/pocket-recommendations/">pocket-recommendations</a>.</small>
'''

if DEBUG:
    print('-' * 80)
    print(path.name)
    print('-' * 80)
    print(content)
    print('-' * 80)
else:
    path.write_text(content)
