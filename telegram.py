import re
import os
import sys
from pathlib import Path

import requests

sys.path.append(os.curdir)
import publishconf


CONTENT_PATH = Path(publishconf.PATH)
ARTICLE_TITLE_RE = re.compile(r'Title:\s+(?P<title>[^\n]+)\s*')
METADATA_RE = re.compile(r'(?P<metadata>([\w\s\-]+:\s+[^\n]+\n)+)')
TELEGRAM_COMMENTS_KEY = 'Telegram-Comments'
TELEGRAM_CHANNEL_NAME = 'honzajavorekcz'
TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']


article_path = sorted(CONTENT_PATH.glob('*.md'))[-1]
article_text = article_path.read_text()
article_metadata = METADATA_RE.search(article_text).group('metadata')
print(f"Last article is {article_path}")

if TELEGRAM_COMMENTS_KEY not in article_metadata:
    print(f"Article doesn't seem to have Telegram comments")
    article_slug = article_path.stem[11:]
    article_url = f"{publishconf.SITEURL}/{publishconf.ARTICLE_URL.format(slug=article_slug)}"
    article_title = ARTICLE_TITLE_RE.search(article_text).group('title')

    print(f"Posting {article_url} to Telegram")
    text = f"{article_title} {article_url}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    response = requests.get(url, params=dict(chat_id=f"@{TELEGRAM_CHANNEL_NAME}",
                                             parse_mode='Markdown',
                                             text=text))
    response.raise_for_status()
    data = response.json()
    assert data['ok'], data

    message_id = data['result']['message_id']
    message_url = f"https://t.me/{TELEGRAM_CHANNEL_NAME}/{message_id}"

    print(f"Saving {message_url} to {article_path}")
    article_path.write_text(article_text.replace(article_metadata,
                                                 f"{article_metadata}{TELEGRAM_COMMENTS_KEY}: {message_url}\n"))
