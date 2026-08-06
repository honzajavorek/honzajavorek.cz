from datetime import date
from typing import Any

import pytest
import requests

from blog.weeknotes import links as links_module
from blog.weeknotes.links import (
    format_links,
    get_canonical_overcast_url,
    get_links,
    get_title_from_url,
)


class FakeResponse:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines

    def raise_for_status(self) -> None:
        pass

    def iter_lines(self, decode_unicode: bool = False) -> list[str]:
        return self.lines


def test_get_links_filters_old_links() -> None:
    links = [
        {
            "created_at": "2026-07-19T23:59:59+02:00",
            "content": '<a href="https://example.com">Example</a>',
            "card": {"url": "https://example.com", "title": "Example"},
        }
    ]

    assert list(get_links(date(2026, 7, 20), links)) == []


def test_get_links_uses_card_url_and_formats_comment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(links_module, "get_title_from_url", lambda url: "Fetched title")
    links = [
        {
            "created_at": "2026-07-20T00:00:00+02:00",
            "content": (
                '<p>Worth reading <a href="https://example.com">Example</a>'
                '<a href="https://mastodonczech.cz/tags/links">#links</a></p>'
            ),
            "card": {"url": "https://example.com", "title": "Example title"},
        }
    ]

    assert list(get_links(date(2026, 7, 20), links)) == [
        {
            "title": "Fetched title",
            "comment": "Worth reading",
            "url": "https://example.com",
        }
    ]


def test_get_links_fetches_missing_title(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(links_module, "get_title_from_url", lambda url: "Fetched title")
    links = [
        {
            "created_at": "2026-07-20T00:00:00+02:00",
            "content": '<p><a href="https://example.com">Example</a></p>',
        }
    ]

    assert next(get_links(date(2026, 7, 20), links))["title"] == "Fetched title"


def test_get_links_resolves_overcast_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        links_module,
        "get_canonical_overcast_url",
        lambda url: "https://example.com/podcast",
    )
    monkeypatch.setattr(links_module, "get_title_from_url", lambda url: "Episode")
    links = [
        {
            "created_at": "2026-07-20T00:00:00+02:00",
            "content": '<p><a href="https://overcast.fm/+episode">Episode</a></p>',
            "card": {"url": "https://overcast.fm/+episode", "title": "Episode"},
        }
    ]

    assert next(get_links(date(2026, 7, 20), links))["url"] == (
        "https://example.com/podcast"
    )


@pytest.mark.parametrize(
    ("links", "expected"),
    [
        ([], ""),
        (
            [
                {"title": "One", "url": "https://example.com/one", "comment": ""},
                {
                    "title": "Two",
                    "url": "https://example.com/two",
                    "comment": "Comment",
                },
            ],
            (
                "- [One](https://example.com/one)\n"
                "- [Two](https://example.com/two)<br>Comment\n"
            ),
        ),
    ],
)
def test_format_links(links: list[dict[str, str]], expected: str) -> None:
    assert format_links(links) == expected


def test_get_title_from_url(monkeypatch: pytest.MonkeyPatch) -> None:
    response = FakeResponse(["<html>", "<title>  Example title  </title>"])
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: response)

    assert get_title_from_url("https://example.com") == "Example title"


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("https://facebook.com/post", "(něco z Facebooku)"),
        ("https://www.facebook.com/post", "(něco z Facebooku)"),
        ("https://twitter.com/status/123", "(něco z Twitteru)"),
        ("https://mobile.twitter.com/status/123", "(něco z Twitteru)"),
        ("https://example.com", "(bez titulku)"),
    ],
)
def test_get_title_from_url_falls_back(
    monkeypatch: pytest.MonkeyPatch, url: str, expected: str
) -> None:
    def raise_connection_error(*args: Any, **kwargs: Any) -> None:
        raise requests.exceptions.ConnectionError

    monkeypatch.setattr(requests, "get", raise_connection_error)

    assert get_title_from_url(url) == expected


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        (
            ['<link rel="canonical" href="https://example.com/episode">'],
            "https://example.com/episode",
        ),
        (
            ['<link rel="canonical" href="https://example.com/">'],
            "https://overcast.fm/+episode",
        ),
        ([], "https://overcast.fm/+episode"),
    ],
)
def test_get_canonical_overcast_url(
    monkeypatch: pytest.MonkeyPatch, lines: list[str], expected: str
) -> None:
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: FakeResponse(lines))

    assert get_canonical_overcast_url("https://overcast.fm/+episode") == expected
