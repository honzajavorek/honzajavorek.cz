import re
from collections.abc import Iterable, Iterator, Mapping
from datetime import date, datetime
from typing import Any
from urllib.parse import urlparse

import httpx
from lxml.html import soupparser as html_soup


FALLBACK_TITLES = {
    "www.facebook.com": "(něco z Facebooku)",
    "facebook.com": "(něco z Facebooku)",
    "twitter.com": "(něco z Twitteru)",
    "mobile.twitter.com": "(něco z Twitteru)",
    "x.com": "(něco z Xka)",
    "medium.com": "(něco z Medium)",
    "instagram.com": "(něco z Instagramu)",
}


def get_links(
    since_date: date, links: Iterable[dict[str, Any]]
) -> Iterator[dict[str, str]]:
    for link in links:
        if datetime.fromisoformat(link["created_at"]).date() < since_date:
            continue

        html_tree = html_soup.fromstring(link["content"])

        if card := link.get("card"):
            link_url = card["url"]
        else:
            link_url = html_tree.cssselect("a")[0].get("href")

        if "overcast.fm" in link_url:
            url = get_canonical_overcast_url(link_url)
        else:
            url = link_url

        title = get_title_from_url(link_url)

        for element in html_tree.cssselect(f'a[href^="{link_url}"]'):
            element.getparent().remove(element)
        for element in html_tree.cssselect('a[href^="https://mastodonczech.cz/tags/"]'):
            element.getparent().remove(element)
        comment = html_tree.text_content().strip()

        yield {"title": title, "comment": comment, "url": url}


def format_links(links: Iterable[Mapping[str, str]]) -> str:
    text = ""
    for link in links:
        text += f"- [{link['title']}]({link['url']})"
        text += f"<br>{link['comment']}" if link["comment"] else ""
        text += "\n"
    return text


def get_title_from_url(url: str) -> str:
    try:
        with httpx.stream(
            "GET",
            url,
            headers={"User-Agent": "HonzaJavorekBot (+https://honzajavorek.cz)"},
            timeout=5,
            follow_redirects=True,
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                match = re.search(r"<title>([^<]+)", str(line), re.IGNORECASE)
                if match:
                    return match.group(1).strip()
    except httpx.HTTPError:
        pass
    return FALLBACK_TITLES.get(urlparse(url).hostname, "(bez titulku)")


def get_canonical_overcast_url(url: str) -> str:
    response = httpx.get(url, follow_redirects=True)
    response.raise_for_status()
    for line in response.iter_lines():
        if 'rel="canonical"' in line:
            canonical_url = re.search(r'rel="canonical"\s+href="([^"]+)"', line).group(
                1
            )
            parts = urlparse(canonical_url)
            if parts.query or parts.params or parts.fragment or parts.path != "/":
                return canonical_url
    return url
