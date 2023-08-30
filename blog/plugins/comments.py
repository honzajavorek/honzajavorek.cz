import re
from urllib.parse import urlparse
from operator import itemgetter

from pelican import signals


# https://icons.getbootstrap.com/
COMMENTS_PLACES = {
    'mastodonczech.cz': dict(priority=1, name='Mastodon', icon='mastodon'),
    't.me': dict(priority=1, name='Telegram', icon='telegram'),
    'linkedin.com': dict(priority=2, name='LinkedIn', icon='linkedin'),
    'reddit.com': dict(priority=3, name='Reddit', icon='reddit'),
    'twitter.com': dict(priority=4, name='Twitter', icon='twitter'),
    'facebook.com': dict(priority=5, name='Facebook', icon='facebook'),
    'news.ycombinator.com': dict(priority=6, name='Hacker News', icon='chat'),
}


def register():
    signals.article_generator_context.connect(set_comments)


def set_comments(article_generator, metadata):
    comments = list(sorted((
        {**item, **COMMENTS_PLACES[item['name']]}
        for item in (
            dict(name=get_name(value), url=value, icon='chat')
            for key, value in metadata.items()
            if key.endswith('-comments')
        )
    ), key=itemgetter('priority')))

    metadata.setdefault('comments', comments)


def get_name(url):
    return re.sub(r'^www\.', '', urlparse(url).netloc)
