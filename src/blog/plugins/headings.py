from lxml import etree


TITLES = {
    'en': 'Link to this heading',
    'cs': 'Odkaz na tento nadpis',
}


def enhance_headings(html_tree, lang):
    for query in ['.//h1[@id]', './/h2[@id]', './/h3[@id]', './/h4[@id]']:
        for heading in html_tree.findall(query):
            add_permalink(heading, TITLES[lang])


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
