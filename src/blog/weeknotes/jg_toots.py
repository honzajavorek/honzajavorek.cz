from collections.abc import Iterable, Iterator
from datetime import date, datetime


def get_jg_toots(
    since_date: date, toots: Iterable[dict[str, str]]
) -> Iterator[dict[str, str]]:
    for toot in toots:
        if datetime.fromisoformat(toot["created_at"]).date() < since_date:
            continue
        yield {"content": toot["content"], "url": toot["url"]}


def format_toots(toots: Iterable[dict[str, str]]) -> str:
    return "\n".join(f"-   {toot['url']}" for toot in toots)
