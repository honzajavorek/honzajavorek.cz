import re
from pathlib import Path
from operator import itemgetter

import requests
import click
from sqlite_utils import Database


METADATA_RE = re.compile(r'(?P<metadata>([\w\s\-]+:\s+[^\n]+\n)+)')


@click.command()
@click.argument('bot_token', envvar='TELEGRAM_BOT_TOKEN')
@click.option('--db', default='blog.db', type=click.Path(exists=True, path_type=Database))
@click.option('--preflight-chat-id', default='119318534')  # https://stackoverflow.com/a/37396871/325365
@click.option('--channel', default='honzajavorekcz')
@click.option('--comments-key', default='Telegram-Comments')
def main(bot_token, db, preflight_chat_id, channel, comments_key):
    query = '''
        select * from articles
        where status == "published"
        order by date desc limit 5
    '''
    articles = sorted([
        article for article
        in db.query(query)
        if article['telegram-comments'] is None
    ], key=itemgetter('date'))
    for article in articles:
        if image_url := article['image_url']:
            click.echo(f"Posting {image_url} to Honza's Telegram")
            post_telegram_message(bot_token, preflight_chat_id, image_url)

        click.echo(f"Posting {article['url']} to Honza's Telegram")
        post_telegram_message(bot_token, preflight_chat_id, article['url'])

        click.echo(f"Posting {article['url']} to Telegram group")
        data = post_telegram_message(bot_token, f"@{channel}", f"{article['title']} {article['url']}")
        message_id = data['result']['message_id']
        message_url = f"https://t.me/{channel}/{message_id}"

        click.echo(f"Saving {message_url} to {article['source_path']}")
        source_path = Path(article['source_path'])
        article_text = source_path.read_text()
        article_metadata = METADATA_RE.search(article_text).group('metadata')
        source_path.write_text(article_text.replace(
            article_metadata,
            f"{article_metadata}{comments_key}: {message_url}\n"
        ))


def post_telegram_message(bot_token, chat_id, text):
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        response = requests.get(api_url, params=dict(chat_id=chat_id, text=text))
        response.raise_for_status()
        data = response.json()
        assert data['ok'], data
        return data
    except requests.HTTPError as e:
        click.echo(f'{e.response.json()!r}', err=True)
        raise
