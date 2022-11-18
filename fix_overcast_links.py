import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs

import requests


def get_canonical_url(overcast_url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        if 'rel="canonical"' in line:
            canonical_url = re.search(r'rel="canonical"\s+href="([^"]+)"', line).group(1)
            canonical_url_parts = urlparse(canonical_url)
            if (
                canonical_url_parts.query or
                canonical_url_parts.params or
                canonical_url_parts.fragment or
                canonical_url_parts.path != '/'
            ):
                return canonical_url
    return overcast_url



for path in Path('content').glob('*.md'):
    print(path)
    text = path.read_text()
    text_fixed = text
    for match in re.finditer(r'(https?://overcast\.fm/\+[^\)]+)\)', text):
        url = match.group(1)
        print('URL', url)
        url_fixed = get_canonical_url(url)
        print('URL FIXED', url_fixed)
        text_fixed = text_fixed.replace(url, url_fixed)
    path.write_text(text_fixed)
