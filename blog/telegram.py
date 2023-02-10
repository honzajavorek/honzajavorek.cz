import re
from pathlib import Path
from operator import itemgetter
import time
import importlib

import requests
import click
from lxml import html


ARTICLE_TITLE_RE = re.compile(r'Title:\s+(?P<title>[^\n]+)\s*')

METADATA_RE = re.compile(r'(?P<metadata>([\w\s\-]+:\s+[^\n]+\n)+)')

TELEGRAM_COMMENTS_KEY = 'Telegram-Comments'


@click.command()
@click.argument('bot_token', envvar='TELEGRAM_BOT_TOKEN')
@click.option('--path', 'content_path', default='content', type=click.Path(exists=True, path_type=Path))
@click.option('--preflight-chat-id', default='119318534')  # https://stackoverflow.com/a/37396871/325365
@click.option('--channel', 'channel', default='honzajavorekcz')
@click.option('--repo', 'repo', default='honzajavorek/honzajavorek.cz')
@click.option('--deployment-polling-interval', default=29, type=int, help='In seconds')
@click.option('--settings-module', default='publishconf', type=importlib.import_module)
def main(bot_token, content_path, preflight_chat_id, channel, repo, deployment_polling_interval, settings_module):
    for article_path in sorted(content_path.glob('*.md'), reverse=True):
        article_text = article_path.read_text()
        article_metadata = METADATA_RE.search(article_text).group('metadata')
        try:
            status = [line.split(':')[1].strip()
                      for line in article_metadata.splitlines()
                      if line.lower().startswith('status:')][0]
        except IndexError:
            status = 'published'
        if status == 'published':
            click.echo(f"Last published article is {article_path}")
            break

    if TELEGRAM_COMMENTS_KEY not in article_metadata:
        click.echo(f"Article doesn't seem to have Telegram comments")
        article_slug = article_path.stem[11:]
        article_url = f"{settings_module.SITEURL}/{settings_module.ARTICLE_URL.format(slug=article_slug)}"
        article_title = ARTICLE_TITLE_RE.search(article_text).group('title')

        click.echo(f"Waiting for the last deployment to finish")
        response = requests.get(f'https://api.github.com/repos/{repo}/deployments')
        response.raise_for_status()
        deployment = sorted(response.json(), key=itemgetter('updated_at'), reverse=True)[0]
        while True:
            response = requests.get(deployment['statuses_url'])
            response.raise_for_status()
            status = sorted(response.json(), key=itemgetter('updated_at'), reverse=True)[0]
            click.echo(f"Deployment status: {status['state']}")
            if status['state'] in ['success', 'error', 'failure', 'inactive']:
                break
            arbitrary_wait(deployment_polling_interval)

        click.echo(f"Waiting for the article to appear online")
        while True:
            response = requests.get(article_url)
            if response.status_code == 200:
                break
            arbitrary_wait(deployment_polling_interval)

        click.echo(f"Getting the image URL")
        response.raise_for_status()
        html_tree = html.fromstring(response.content)
        image_url = html_tree.cssselect('meta[property="og:image"]')[0].get('content')
        response = requests.head(image_url)
        response.raise_for_status()

        click.echo(f"Posting {image_url} to Honza's Telegram")
        post_telegram_message(bot_token, preflight_chat_id, image_url)

        click.echo(f"Posting {article_url} to Honza's Telegram")
        post_telegram_message(bot_token, preflight_chat_id, article_url)

        click.echo(f"Posting {article_url} to Telegram group")
        data = post_telegram_message(bot_token, f"@{channel}", f"{article_title} {article_url}")
        message_id = data['result']['message_id']
        message_url = f"https://t.me/{channel}/{message_id}"

        click.echo(f"Saving {message_url} to {article_path}")
        article_path.write_text(article_text.replace(article_metadata,
                                                    f"{article_metadata}{TELEGRAM_COMMENTS_KEY}: {message_url}\n"))


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


def arbitrary_wait(seconds=60):
    for _ in range(seconds):
        time.sleep(1)
        click.echo(f'Waiting {seconds}s…', err=True)
