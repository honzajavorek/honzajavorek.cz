import json
from pathlib import Path
from pelican import signals


REPLIES_PATH = Path('content/data/toots-replies.json')


replies = None


def register():
    signals.initialized.connect(load_replies)
    signals.article_generator_context.connect(set_replies)


def load_replies(pelican):
    global replies
    replies = json.loads(REPLIES_PATH.read_text())


def set_replies(article_generator, metadata):
    for article in replies:
        if article['slug'] == metadata['slug']:
            metadata['replies'] = article['replies']
            metadata['replies_stars'] = article['favourites_count']
            metadata['replies_url'] = article['toot_url']
            return
