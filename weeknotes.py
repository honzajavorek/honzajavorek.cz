import os
import sys
from datetime import date, timedelta
from pathlib import Path

from slugify import slugify

sys.path.append(os.curdir)
import pelicanconf


TITLE_PREFIX = 'Týdenní poznámky: '


if len(sys.argv) > 1:
    highlights = ' '.join(sys.argv[1:])
else:
    highlights = input(TITLE_PREFIX)

title = TITLE_PREFIX + highlights
slug = slugify(title)

today = date.today()
monday = today - timedelta(today.weekday())
monday_cz = f'{monday:%d}.'.lstrip('0') + f'{monday:%m}.'.lstrip('0')
friday = today + timedelta(days=4 - today.weekday())
friday_cz = f'{friday:%d}.'.lstrip('0') + f'{friday:%m}.'.lstrip('0')
friday_iso = friday.isoformat()

path = Path(__file__).parent / pelicanconf.PATH / f'{friday_iso}_{slug}.md'
path.write_text(f'''
Title: {title}
Image: images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg
Lang: cs


Utekl další týden ({monday_cz} — {friday_cz}) a tak sepisuji, co jsem dělal a co zajímavého jsem se naučil. Především se snažím rozvíjet [junior.guru](https://junior.guru/). Nemám šéfa, kterému bych reportoval každý svůj krok, ale mám [podporovatele](https://junior.guru/donate/), a ty by mohlo zajímat, jestli se neflákám. Taky je to způsob, jak se sám doma nezbláznit a nepropadat pocitu, že je zase pátek a já jsem přitom nestihl nic udělat.

![Poznámky]({{static}}/images/jan-kahanek-g3O5ZtRk2E4-unsplash.jpg)
Fotka od [Honzy Kahánka](https://unsplash.com/@honza_kahanek)

'''.lstrip())
