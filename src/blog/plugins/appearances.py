from pathlib import Path
from operator import itemgetter
from datetime import date
from typing import Annotated, Literal, Optional

import yaml
from pelican import signals
from pydantic import BaseModel, ConfigDict, HttpUrl, PlainSerializer

from blog.plugins.utils import get_articles


class YAMLConfig(BaseModel):
    model_config = ConfigDict(extra='forbid')


class AppearanceConfig(YAMLConfig):
    date: date
    title: str
    medium: str
    type: Literal['talk', 'workshop', 'interview', 'text'] = 'talk'
    url: Optional[Annotated[HttpUrl, PlainSerializer(str)]] = None
    resources_type: Literal['slides', 'text'] = 'slides'
    resources_url: Optional[Annotated[HttpUrl, PlainSerializer(str)]] = None


def register():
    signals.all_generators_finalized.connect(load_appearances)


def load_appearances(generators):
    settings = generators[0].settings
    articles = get_articles(generators)

    # external appearances
    path = Path('./content/data/appearances.yml')
    appearances = [AppearanceConfig(**record).model_dump()
                   for record in yaml.safe_load(path.read_text())]
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
            article.status == 'published' and
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
