from operator import attrgetter
from itertools import islice

from pelican import signals

from blog.plugins.utils import get_articles


SEEALSO_LIMIT = 5


def register():
    signals.all_generators_finalized.connect(set_seealso)


def set_seealso(generators):
    settings = generators[0].settings

    articles = [article for article in get_articles(generators)
                if article.status == 'published']
    articles = sorted(articles, key=attrgetter('date'), reverse=True)
    articles_by_lang = dict(cs=[a for a in articles if a.lang == 'cs'],
                            en=[a for a in articles if a.lang == 'en'])

    for article in articles:
        other_articles = (a for a in articles_by_lang[article.lang]
                          if a != article)
        seealso = list(islice((
            a for i, a
            in enumerate(other_articles)
            if (i == 0 or
                settings['HIGHLIGHT_TAG'] in [t.name for t in getattr(a, 'tags', [])])
        ), SEEALSO_LIMIT))
        article.metadata['seealso'] = seealso
        article.seealso = seealso
