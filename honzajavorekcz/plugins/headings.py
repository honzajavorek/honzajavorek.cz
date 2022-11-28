from lxml import etree
from pelican import signals

from honzajavorekcz.plugins.utils import parse_html, get_articles


TITLES = {
    'en': 'Link to this heading',
    'cs': 'Odkaz na tento nadpis',
}


def register():
    signals.all_generators_finalized.connect(enhance_headings)


def enhance_headings(generators):
    for article in get_articles(generators):
        with parse_html(article, modify=True) as html_tree:
            for query in ['.//h1[@id]', './/h2[@id]', './/h3[@id]', './/h4[@id]']:
                for heading in html_tree.findall(query):
                    add_permalink(heading, TITLES[article.lang])


def add_permalink(heading, title):
    icon = etree.Element('i')
    icon.set('class', 'bi bi-link-45deg')
    a = etree.Element('a')
    a.set('href', '#{}'.format(heading.get('id')))
    a.set('title', title)
    a.append(icon)
    small = etree.Element('small')
    small.set('class', 'permalink')
    small.append(a)
    heading.append(small)
