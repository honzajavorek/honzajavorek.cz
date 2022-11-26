import sys
import os
from pathlib import Path
from operator import itemgetter
import itertools

from pelican import signals
import strictyaml as yaml

sys.path.append(os.path.dirname(__file__))
from utils import get_articles


SCHEMA = yaml.Seq(
    yaml.Map({
        'date': yaml.Datetime(),
        'title': yaml.Str(),
        'medium': yaml.Str(),
        yaml.Optional('type', default='talk'): yaml.Enum([
            'talk',
            'workshop',
            'interview',
            'text',
        ]),
        yaml.Optional('url'): yaml.Url(),
        yaml.Optional('resources_type', default='slides'): yaml.Enum([
            'slides',
            'text',
        ]),
        yaml.Optional('resources_url'): yaml.Url(),
    }),
)


def register():
    signals.all_generators_finalized.connect(load_appearances)


def load_appearances(generators):
    settings = generators[0].settings
    articles = get_articles(generators)

    # external appearances
    path = Path('./content/data/appearances.yml')
    appearances = [entry | dict(date=entry['date'].date())
                   for entry in
                   yaml.load(path.read_text(), SCHEMA).data]
    appearances = sorted(appearances, key=itemgetter('date'), reverse=True)

    # prepare blog articles
    articles = [
        dict(
            date=article.date.date(),
            title=article.title,
            medium='Javorové lístky',
            type='text',
            url=f"{settings['SITEURL']}/{article.url}",
        )
        for article in articles
        if (
            (settings['NOW'].year - article.date.year <= settings['OUTDATED_ARTICLE_YEARS']) and
            (settings['WEEKNOTES_TAG'] not in [tag.name for tag in getattr(article, 'tags', [])])
        ) or (
            settings['HIGHLIGHT_TAG'] in [tag.name for tag in getattr(article, 'tags', [])]
        )
    ]

    # merge & sort
    appearances = sorted(articles + appearances,
                         key=itemgetter('date'),
                         reverse=True)

    # set context
    generators[0].context['appearances'] = appearances
