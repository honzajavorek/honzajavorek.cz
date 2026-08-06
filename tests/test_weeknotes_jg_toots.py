from datetime import date

import pytest

from blog.weeknotes.jg_toots import format_toot_text, format_toots, get_jg_toots


@pytest.mark.parametrize(
    ("since_date", "toots", "expected"),
    [
        (
            date(2026, 7, 20),
            [
                {
                    "created_at": "2026-07-19T23:59:59+02:00",
                    "content": "Old",
                    "url": "https://example.com/old",
                },
                {
                    "created_at": "2026-07-20T00:00:00+02:00",
                    "content": "Boundary",
                    "url": "https://example.com/boundary",
                },
                {
                    "created_at": "2026-07-21T12:00:00+02:00",
                    "content": "New",
                    "url": "https://example.com/new",
                },
            ],
            [
                {"content": "Boundary", "url": "https://example.com/boundary"},
                {"content": "New", "url": "https://example.com/new"},
            ],
        ),
        (date(2026, 7, 20), [], []),
    ],
)
def test_get_jg_toots(
    since_date: date,
    toots: list[dict[str, str]],
    expected: list[dict[str, str]],
) -> None:
    assert list(get_jg_toots(since_date, toots)) == expected


@pytest.mark.parametrize(
    ("toots", "expected"),
    [
        ([], ""),
        (
            [
                {"url": "https://example.com/one", "content": "<p>One</p>"},
                {
                    "url": "https://example.com/two",
                    "content": "<p>Two</p><p>More</p>",
                },
            ],
            """https://example.com/one
<!-- One -->

https://example.com/two
<!-- Two

More -->""",
        ),
    ],
)
def test_format_toots(toots: list[dict[str, str]], expected: str) -> None:
    assert format_toots(toots) == expected


@pytest.mark.parametrize(
    ("content", "expected"),
    [
        (
            (
                '<p>Nový <a href="https://example.com/tag">#'
                "<span>newsletter</span></a> je na "
                '<a href="https://example.com"><span>example.com</span></a>.</p>'
            ),
            "Nový #newsletter je na example.com.",
        ),
        (
            "<p>První odstavec</p><p>Druhý odstavec</p>",
            "První odstavec\n\nDruhý odstavec",
        ),
        ("Plain text -- hint", "Plain text — hint"),
    ],
)
def test_format_toot_text(content: str, expected: str) -> None:
    assert format_toot_text(content) == expected
