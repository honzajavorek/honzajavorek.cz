from datetime import date

import pytest

from blog.weeknotes.jg_toots import format_toots, get_jg_toots


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
                {"url": "https://example.com/one"},
                {"url": "https://example.com/two"},
            ],
            "-   https://example.com/one\n-   https://example.com/two",
        ),
    ],
)
def test_format_toots(toots: list[dict[str, str]], expected: str) -> None:
    assert format_toots(toots) == expected
