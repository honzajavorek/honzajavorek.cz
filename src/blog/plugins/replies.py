from datetime import datetime
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
    for toot in replies:
        toot['created_at'] = datetime.fromisoformat(toot['created_at'])
        for reply in toot['replies']:
            reply['created_at'] = datetime.fromisoformat(reply['created_at'])


def set_replies(article_generator, metadata):
    for article in replies:
        if article['slug'] == metadata['slug']:
            metadata['replies'] = article.get('replies', [])
            metadata['replies_stars'] = article.get('favourites_count', 0)
            metadata['replies_reblogs'] = article.get('reblogs_count', 0)
            metadata['replies_url'] = article['toot_url']
            return
