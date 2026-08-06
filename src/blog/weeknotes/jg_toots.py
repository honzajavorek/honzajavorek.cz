from collections.abc import Iterable, Iterator
from datetime import date, datetime

from bs4 import BeautifulSoup


def get_jg_toots(
    since_date: date, toots: Iterable[dict[str, str]]
) -> Iterator[dict[str, str]]:
    for toot in toots:
        if datetime.fromisoformat(toot["created_at"]).date() < since_date:
            continue
        yield {"content": toot["content"], "url": toot["url"]}


def format_toots(toots: Iterable[dict[str, str]]) -> str:
    return "\n\n".join(
        f"{toot['url']}\n<!-- {format_toot_text(toot['content'])} -->" for toot in toots
    )


def format_toot_text(content: str) -> str:
    soup = BeautifulSoup(content, "html.parser")
    paragraphs = [paragraph.get_text().strip() for paragraph in soup.find_all("p")]
    text = "\n\n".join(filter(None, paragraphs)) or soup.get_text().strip()
    return text.replace("--", "—")
