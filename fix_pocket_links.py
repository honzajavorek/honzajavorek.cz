import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs


for path in Path('content').glob('*.md'):
    print(path)
    text = path.read_text()
    text_fixed = text
    for match in re.finditer(r'(https?://getpocket.com/redirect\??&url=[^\n]+)\)', text):
        url = match.group(1)
        print('URL', url)
        url_fixed = parse_qs(urlparse(url).query)['url'][0]
        print('URL FIXED', url_fixed)
        text_fixed = text_fixed.replace(url, url_fixed)
    path.write_text(text_fixed)
