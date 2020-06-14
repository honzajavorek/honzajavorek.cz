import re
import os
import sys
from urllib.parse import urlparse
from pathlib import Path

import requests

sys.path.append(os.curdir)
import pelicanconf


CONTENT_PATH = Path(__file__).parent / pelicanconf.PATH
COMMENTS_API_URL = 'https://hook.integromat.com/z9sxy3t8k6hxp2bxs3b237a5rw1n7yt7'
META_HOST_MAPPING = {
    'twitter.com': 'Twitter-Comments',
    'facebook.com': 'Facebook-Comments',
}


response = requests.get(COMMENTS_API_URL)
response.raise_for_status()
urls = [(item['article_url'], item['post_url']) for item in response.json()]

for article_url, post_url in urls:
    host = urlparse(post_url).hostname.replace('www.', '')
    meta_key = META_HOST_MAPPING[host]

    slug = re.match(r'^https?://honzajavorek.cz/blog/([^/]+)/', article_url).group(1)
    path = next(CONTENT_PATH.glob(f'*{slug}.md'))
    meta, content = path.read_text().split('\n\n', 1)

    meta_lines = [line for line in meta.splitlines() if meta_key in line]
    if not meta_lines:
        print(f'{path.name}: is missing {meta_key}! updating...')
        meta += f'\n{meta_key}: {post_url}'
        path.write_text(meta + '\n\n' + content)
    else:
        print(f'{path.name}: already has {meta_key}')
