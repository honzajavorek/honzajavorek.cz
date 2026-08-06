from datetime import date
from pathlib import Path

import pytest

from blog.weeknotes import (
    format_content,
    format_last_weeknotes_path,
    format_title,
    format_weeknotes_date,
    get_last_weeknotes_path,
    get_weeknotes_date,
    get_weeknotes_path,
)


def test_format_content() -> None:
    content = format_content(
        title="Týdenní poznámky: Test",
        weeknotes_tag="weeknotes",
        last_weeknotes_path="{filename}2026-07-20_test.md",
        last_weeknotes_date="20. 7.",
        today="31. 7.",
        jg_toots="-   https://example.com/toot",
        links="- [Example](https://example.com)\n",
        dependabot_upgrades="-   7 upgradů závislostí na všech projektech.",
        github_work="### example\n\n-   🟢 [example/repo#42](https://example.com/repo/42)",
    )

    assert all(
        value in content
        for value in [
            "Title: Týdenní poznámky: Test",
            "Tags: weeknotes, junior.guru",
            "[posledních poznámek]({filename}2026-07-20_test.md)",
            "(20. 7. až 31. 7.)",
            "-   https://example.com/toot",
            "- [Example](https://example.com)",
            "7 upgradů závislostí na všech projektech.",
            "🟢 [example/repo#42](https://example.com/repo/42)",
            "![Poznámky]({static}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)",
        ]
    )


def test_format_content_without_upgrades() -> None:
    content = format_content(
        title="Týdenní poznámky: Test",
        weeknotes_tag="weeknotes",
        last_weeknotes_path="{filename}2026-07-20_test.md",
        last_weeknotes_date="20. 7.",
        today="31. 7.",
        jg_toots="",
        links="",
        dependabot_upgrades="",
        github_work="",
    )

    assert "upgrad" not in content


@pytest.mark.parametrize(
    ("title", "title_prefix", "expected"),
    [
        ("Dovolená", "Týdenní poznámky", "Týdenní poznámky: Dovolená"),
        ("A week", "Weeknotes", "Weeknotes: A week"),
    ],
)
def test_format_title(title: str, title_prefix: str, expected: str) -> None:
    assert format_title(title, title_prefix) == expected


def test_format_last_weeknotes_path(tmp_path: Path) -> None:
    path = tmp_path / "2026-07-31_tydenni-poznamky.md"

    assert format_last_weeknotes_path(path, tmp_path) == (
        "{filename}2026-07-31_tydenni-poznamky.md"
    )


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        (Path("2026-07-31_tydenni-poznamky.md"), date(2026, 7, 31)),
        (Path("2024-02-29_weeknotes.md"), date(2024, 2, 29)),
    ],
)
def test_get_weeknotes_date(path: Path, expected: date) -> None:
    assert get_weeknotes_date(path) == expected


@pytest.mark.parametrize(
    ("weeknotes_date", "expected"),
    [
        (date(2026, 7, 31), "31. 7."),
        (date(2024, 2, 9), "9. 2."),
    ],
)
def test_format_weeknotes_date(weeknotes_date: date, expected: str) -> None:
    assert format_weeknotes_date(weeknotes_date) == expected


def test_get_weeknotes_path(tmp_path: Path) -> None:
    title = "Weeknotes: A week"
    weeknotes_date = date(2026, 7, 31)

    assert (
        get_weeknotes_path(tmp_path, title, weeknotes_date)
        == tmp_path / "2026-07-31_weeknotes-a-week.md"
    )


def test_get_last_weeknotes_path(tmp_path: Path) -> None:
    older_path = tmp_path / "2026-07-18_tydenni-poznamky-old.md"
    newer_path = tmp_path / "2026-07-31_tydenni-poznamky-new.md"
    older_path.touch()
    newer_path.touch()
    (tmp_path / "2026-08-01_something-else.md").touch()

    assert get_last_weeknotes_path(tmp_path, "Týdenní poznámky") == newer_path
