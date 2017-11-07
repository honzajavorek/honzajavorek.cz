
from danube_delta.settings import *  # NOQA


AUTHOR = 'Honza Javorek'
SITENAME = 'Javorové lístky'


ABOUT_HEADING = AUTHOR
ABOUT = '''
[Honza](http://honzajavorek.cz) je programátor. Od roku 2011 pomáhá budovat
českou komunitu kolem jazyka [Python](http://python.cz/).
V [Apiary](https://apiary.io/) se stará o [Dredd](https://github.com/apiaryio/dredd),
nástroj na testování webových API.
'''
ABOUT_IMAGE = 'images/honza.jpg'


OUTDATED_ARTICLE_YEARS = 2
OUTDATED_ARTICLE_WARNING = '''
**Upozornění!** Tento článek vyšel před více než {} lety. Můžete si
jej přečíst v rámci zkoumání minulosti, ale přepokládejte, že dnes se
Honza již nemusí s obsahem ztotožňovat.
'''.format(OUTDATED_ARTICLE_YEARS)


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
DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = 'UA-1316071-6'
