import logging

import requests
from lxml import html
from pelican import signals


logger = logging.getLogger(__name__)


def register():
    signals.article_generator_finalized.connect(load_projects)


def load_projects(article_generator):
    settings = article_generator.settings
    logger.info(f"Parsing https://github.com/honzajavorek")
    try:
        response = requests.get('https://github.com/honzajavorek')
        response.raise_for_status()

        html_tree = html.fromstring(response.content)
        html_tree.make_links_absolute(response.url)

        article_generator.context['projects'] = list(get_pinned_repos(html_tree))
    except requests.RequestException as e:
        logger.debug(e)
        logger.warning("Seems like you're developing offline, projects won't be available")


def get_pinned_repos(html_tree):
    for repo_tree in html_tree.cssselect('.pinned-item-list-item'):
        try:
            owner = repo_tree.cssselect('.owner')[0].text_content()
        except IndexError:
            owner = 'honzajavorek'

        desc = repo_tree.cssselect('.pinned-item-desc')[0].text_content()
        desc_en = desc.split(' / ')[0]

        yield dict(
            owner=owner,
            name=repo_tree.cssselect('.repo')[0].text_content(),
            url=repo_tree.cssselect('a')[0].get('href'),
            description=desc_en,
        )
