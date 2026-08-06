import re
from datetime import date, datetime
from urllib.parse import urlparse

import requests
from lxml.html import soupparser as html_soup


TITLES = {
    "www.facebook.com": "(něco na Facebooku)",
    "facebook.com": "(něco na Facebooku)",
    "twitter.com": "(něco na Twitteru)",
    "mobile.twitter.com": "(něco na Twitteru)",
}


def get_links(since_date: date, links: list):
    for link in links:
        if datetime.fromisoformat(link["created_at"]).date() < since_date:
            continue

        html_tree = html_soup.fromstring(link["content"])
        title = None

        if card := link.get("card"):
            link_url = card["url"]
            title = card["title"]
        else:
            link_url = html_tree.cssselect("a")[0].get("href")

        if "overcast.fm" in link_url:
            url = get_canonical_overcast_url(link_url)
        else:
            url = link_url

        if title is None:
            title = get_title_from_url(link_url)

        for element in html_tree.cssselect(f'a[href^="{link_url}"]'):
            element.getparent().remove(element)
        for element in html_tree.cssselect('a[href^="https://mastodonczech.cz/tags/"]'):
            element.getparent().remove(element)
        comment = html_tree.text_content().strip()

        yield {"title": title, "comment": comment, "url": url}


def format_links(links):
    text = ""
    for link in links:
        text += f"- [{link['title']}]({link['url']})"
        text += f"<br>{link['comment']}" if link["comment"] else ""
        text += "\n"
    return text


def get_title_from_webpage(webpage):
    try:
        return TITLES[urlparse(webpage.url).hostname]
    except KeyError:
        return webpage.title


def get_title_from_url(url):
    try:
        response = requests.get(
            url,
            stream=True,
            headers={"User-Agent": "HonzaJavorekBot (+https://honzajavorek.cz)"},
            timeout=5,
        )
        response.raise_for_status()
    except (
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
        requests.exceptions.ReadTimeout,
    ):
        pass
    else:
        for line in response.iter_lines(decode_unicode=True):
            match = re.search(r"<title>([^<]+)", str(line), re.IGNORECASE)
            if match:
                return match.group(1).strip()
    return "(bez titulku)"


def get_canonical_overcast_url(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        if 'rel="canonical"' in line:
            canonical_url = re.search(r'rel="canonical"\s+href="([^"]+)"', line).group(
                1
            )
            parts = urlparse(canonical_url)
            if parts.query or parts.params or parts.fragment or parts.path != "/":
                return canonical_url
    return url
