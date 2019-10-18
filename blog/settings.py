from danube_delta.settings import *  # NOQA


AUTHOR = 'Honza Javorek'
SITENAME = 'Javorové lístky'


ABOUT_HEADING = AUTHOR
ABOUT = '''
[Honza](http://honzajavorek.cz) je programátor. Založil
[junior.guru](https://junior.guru), projekt pomáhající lidem naučit se
programovat a získat svou první práci v IT. Od roku 2011 pomáhá budovat
českou komunitu kolem jazyka [Python](http://python.cz/).
'''
ABOUT_IMAGE = 'images/honza.jpg'


OUTDATED_ARTICLE_YEARS = 3
OUTDATED_ARTICLE_WARNING = '''
**Upozornění!** Tento článek vyšel před více než {} lety. Můžete si
jej přečíst v rámci zkoumání minulosti, ale přepokládejte, že dnes se
Honza již nemusí s obsahem ztotožňovat.
'''.format(OUTDATED_ARTICLE_YEARS)


if PRODUCTION:  # NOQA
    SITEURL = 'http://honzajavorek.cz'


OUTPUT_PATH = '../_output'


# URL and save paths settings
URL_PREFIX = 'blog/'
ARTICLE_URL = URL_PREFIX + ARTICLE_URL  # NOQA
ARTICLE_SAVE_AS = URL_PREFIX + ARTICLE_SAVE_AS  # NOQA
ARTICLE_LANG_URL = URL_PREFIX + ARTICLE_LANG_URL  # NOQA
ARTICLE_LANG_SAVE_AS = URL_PREFIX + ARTICLE_LANG_SAVE_AS  # NOQA
INDEX_URL = SITEURL + '/' + URL_PREFIX
INDEX_SAVE_AS = URL_PREFIX + 'index.html'


# Theming
DISQUS_SITENAME = 'javorove-listky'
GOOGLE_ANALYTICS = 'UA-1316071-6'
