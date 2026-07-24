from pathlib import Path

from pelican import signals

from blog.plugins.utils import parse_html, get_articles
from blog.plugins.code_blocks import process_code_blocks
from blog.plugins.headings import enhance_headings
from blog.plugins.media import process_media, set_image_dimensions
from blog.plugins.readtime import set_readtime
from blog.plugins.tables import enhance_tables


def register():
    signals.all_generators_finalized.connect(enhance_content)


def enhance_content(generators):
    content_dir = Path(generators[0].settings['PATH'])

    for article in get_articles(generators):
        set_image_dimensions(article, content_dir)

        # Single parse+serialize pass; previously each of these transforms
        # re-parsed and re-serialized the article HTML on its own.
        with parse_html(article, modify=True) as html_tree:
            process_code_blocks(html_tree)
            enhance_headings(html_tree, article.lang)
            process_media(html_tree)
            set_readtime(article, html_tree)
            enhance_tables(html_tree)
