import json
import re
from pathlib import Path
from operator import itemgetter
from typing import Any

import requests
import click
from sqlite_utils import Database
from mastodon import Mastodon


METADATA_RE = re.compile(r'(?P<metadata>([\w\s\-]+:\s+[^\n]+\n)+)')

HASHTAGS_MAPPING = {
    'týdenní poznámky': '#weeknotes',
    'junior.guru': '#juniorguru',
}


@click.command()
@click.argument('bot_token', envvar='TELEGRAM_BOT_TOKEN')
@click.option('--db', default='blog.db', type=click.Path(exists=True, path_type=Database))
@click.option('--preflight-chat-id', default='119318534')  # https://stackoverflow.com/a/37396871/325365
@click.option('--channel', default='honzajavorekcz')
@click.option('--comments-key', default='Telegram-Comments')
@click.option('--debug/--no-debug', default=False)
def telegram(bot_token: str, db: Database, preflight_chat_id: str, channel: str, comments_key: str, debug: bool):
    query = '''
        select * from articles
        where status == "published"
        order by date desc limit 3
    '''
    articles = sorted([
        article for article
        in db.query(query)
        if article[comments_key.lower()] is None
    ], key=itemgetter('date'))

    if not articles:
        click.echo(f"No relevant articles found")
        return

    for article in articles:
        text = prepare_text(article)
        if debug:
            click.echo(text)
        else:
            if image_url := article['image_url']:
                click.echo(f"Posting {image_url} to Honza's Telegram")
                post_telegram_message(bot_token, preflight_chat_id, image_url)

            click.echo(f"Posting {article['url']} to Honza's Telegram")
            post_telegram_message(bot_token, preflight_chat_id, article['url'])

            click.echo(f"Posting {article['url']} to Telegram group")
            data = post_telegram_message(bot_token, f"@{channel}", text)
            message_id = data['result']['message_id']
            message_url = f"https://t.me/{channel}/{message_id}"

            click.echo(f"Saving {message_url} to {article['source_path']}")
            append_metadata(article['source_path'], comments_key, message_url)


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


@click.command()
@click.argument('client_id', envvar='MASTODON_CLIENT_ID')
@click.argument('client_secret', envvar='MASTODON_CLIENT_SECRET')
@click.argument('access_token', envvar='MASTODON_ACCESS_TOKEN')
@click.option('--db', default='blog.db', type=click.Path(exists=True, path_type=Database))
@click.option('--server-url', default='https://mastodonczech.cz')
@click.option('--comments-key', default='Mastodon-Comments')
@click.option('--debug/--no-debug', default=False)
def mastodon(client_id: str, client_secret: str, access_token: str, db: Database, server_url: str, comments_key: str, debug: bool):
    query = '''
        select * from articles
        where status == "published"
        order by date desc limit 3
    '''
    articles = sorted([
        article for article
        in db.query(query)
        if article[comments_key.lower()] is None
    ], key=itemgetter('date'))

    if not articles:
        click.echo(f"No relevant articles found")
        return

    click.echo('Connecting to Mastodon')
    mastodon = Mastodon(api_base_url=server_url,
                        client_id=client_id,
                        client_secret=client_secret,
                        access_token=access_token)
    for article in articles:
        click.echo(f"Posting {article['url']} to Mastodon")
        text = prepare_text(article)
        if debug:
            click.echo(text)
        else:
            data = mastodon.toot(text)
            message_url = data['url']

            click.echo(f"Saving {message_url} to {article['source_path']}")
            append_metadata(article['source_path'], comments_key, message_url)


def prepare_text(article: dict) -> str:
    tags = json.loads(article['tags'])

    if 'týdenní poznámky' in tags:
        text = f"Týdenní poznámky! Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru?"
    elif 'junior.guru' in tags:
        text = f"„{article['title']}” Jak se mi daří v jednom člověku provozovat a rozvíjet junior.guru?"
    else:
        text = f"„{article['title']}”"

    readtime = article['readtime']
    if readtime < 5:
        emoji = "😎"
    elif readtime < 15:
        emoji = "🧐"
    elif readtime < 30:
        emoji = "😅"
    else:
        emoji = "🙈"

    hashtags = set(filter(None, [HASHTAGS_MAPPING.get(tag) for tag in tags])) | {'#blog'}
    hashtags = ' '.join(sorted(hashtags))

    return f"{text} Tentorkát je to na {article['readtime']} min čtení {emoji} {article['url']} {hashtags}"


def append_metadata(source_path: str | Path, key: str, value: Any):
    source_path = Path(source_path)
    article_text = source_path.read_text()
    article_metadata = METADATA_RE.search(article_text).group('metadata')
    source_path.write_text(article_text.replace(
        article_metadata,
        f"{article_metadata}{key}: {value}\n"
    ))
