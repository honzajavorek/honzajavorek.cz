
import pytz
import datetime

from danube_delta.settings import *  # NOQA


AUTHOR = 'Honza Javorek'
SITENAME = 'Javorové lístky'


ABOUT_HEADING = AUTHOR
ABOUT = '''
[Honza](http://honzajavorek.cz) je programátor. Od roku 2011 buduje českou
komunitu kolem jazyka [Python](http://python.cz/). V současnosti pomáhá hlavně s
propagací aktivit, jako jsou [PyLadies](http://pyladies.cz/),
[Pyvo](http://pyvo.cz/), nebo [PyCon CZ](https://cz.pycon.org/). Přes den jej
najdete v [Apiary](https://apiary.io/), kde se stará o
[Dredd](https://github.com/apiaryio/dredd), framework na testování API. Sem
tam ho můžete potkat, jak přednáší na srazu nebo na konferenci.
'''
ABOUT_IMAGE = 'images/honza.jpg'


if PRODUCTION:
    SITEURL = 'http://honzajavorek.cz'


# URL and save paths settings
URL_PREFIX = 'blog/'
ARTICLE_URL = URL_PREFIX + ARTICLE_URL
ARTICLE_SAVE_AS = URL_PREFIX + ARTICLE_SAVE_AS
ARTICLE_LANG_URL = URL_PREFIX + ARTICLE_LANG_URL
ARTICLE_LANG_SAVE_AS = URL_PREFIX + ARTICLE_LANG_SAVE_AS
INDEX_URL = SITEURL + '/' + URL_PREFIX
INDEX_SAVE_AS = URL_PREFIX + 'index.html'


# Theming
THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'theme')

OLD_ARTICLE_CLIFF_YEARS = 2
OLD_ARTICLE_CLIFF = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) - datetime.timedelta(days=365 * OLD_ARTICLE_CLIFF_YEARS)

DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = 'UA-1316071-6'
