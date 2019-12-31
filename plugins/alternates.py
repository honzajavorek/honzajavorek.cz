import re
from urllib.parse import urlparse

from pelican import signals


def register():
    signals.article_generator_context.connect(set_alternates)


def set_alternates(article_generator, metadata):
    alternates = [
        dict(name=get_name(value), url=value)
        for key, value in metadata.items()
        if key.endswith('-url')
    ]
    metadata.setdefault('alternates', alternates)


def get_name(url):
    return re.sub(r'^www\.', '', urlparse(url).netloc)
