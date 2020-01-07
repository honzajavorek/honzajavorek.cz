import re
from urllib.parse import urlparse
from operator import itemgetter

from pelican import signals


SOCIAL_NETWORKS = {
    # https://forkaweso.me/Fork-Awesome/icons/#brand
    'facebook.com': dict(name='Facebook', icon='facebook-official'),
    'twitter.com': dict(name='Twitter', icon='twitter'),
    'linkedin.com': dict(name='LinkedIn', icon='linkedin'),
    'reddit.com': dict(name='Reddit', icon='reddit'),
    'news.ycombinator.com': dict(name='Hacker News', icon='hacker-news'),
}


def register():
    signals.article_generator_context.connect(set_comments)


def set_comments(article_generator, metadata):
    comments = list(sorted((
        {**item, **SOCIAL_NETWORKS.get(item['name'])}
        for item in (
            dict(name=get_name(value), url=value, icon='comment-o')
            for key, value in metadata.items()
            if key.endswith('-comments')
        )
    ), key=itemgetter('name')))

    metadata.setdefault('comments', comments)


def get_name(url):
    return re.sub(r'^www\.', '', urlparse(url).netloc)
