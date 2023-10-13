from datetime import datetime
from pathlib import Path
from pelican import signals
from sqlite_utils import Database


db = None


def register():
    signals.initialized.connect(init)
    signals.content_written.connect(store_content)


def init(pelican):
    db_path = Path(pelican.settings['DB_PATH'])
    db_path.unlink(missing_ok=True)
    global db
    db = Database(db_path)


def store_content(path, context):
    if 'article' in context:
        safe_dt = context['article'].metadata['date']
        dt = datetime.fromtimestamp(safe_dt.timestamp())

        source_path = str(Path(context['article'].source_path).relative_to(Path.cwd()))

        image_path = context['article'].metadata.get('image')
        image_url = f'{context["localsiteurl"]}/{image_path}' if image_path else None

        db['articles'].insert({
            'slug': context['article'].metadata['slug'],
            'date': dt,
            'source_path': source_path,
            'output_path': context['output_file'],
            'url': f'{context["localsiteurl"]}/{context["article"].url}',
            'image_path': image_path,
            'image_url': image_url,
            'title': context['article'].metadata['title'],
            'lang': context['article'].metadata['lang'],
            'tags': [tag.name for tag in context['article'].metadata.get('tags', [])],
            'readtime': context['article'].metadata['readtime'],
            'status': context['article'].status,
            'telegram-comments': context['article'].metadata.get('telegram-comments'),
            'mastodon-comments': context['article'].metadata.get('mastodon-comments'),
        }, pk='slug', replace=True)
