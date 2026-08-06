import subprocess
from datetime import UTC, date, datetime
from importlib import import_module
from types import SimpleNamespace
from typing import cast
from unittest.mock import Mock

import pytest
from githubkit import GitHub

from blog.weeknotes.github import (
    WorkItem,
    format_section_name,
    format_upgrades,
    format_work_items,
    get_closed_dependabot_prs_count,
    get_contributed_owners,
    get_contribution_work_item,
    get_contributions,
    get_dependabot_closed_events,
    get_github_token,
)


def test_get_github_token_uses_explicit_token(monkeypatch: pytest.MonkeyPatch) -> None:
    run = Mock()
    monkeypatch.setattr(subprocess, "run", run)

    assert (get_github_token("explicit-token"), run.call_count) == (
        "explicit-token",
        0,
    )


def test_get_github_token_uses_gh(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        subprocess,
        "run",
        Mock(return_value=SimpleNamespace(stdout="gh-token\n")),
    )

    assert get_github_token(None) == "gh-token"


@pytest.mark.parametrize(
    "error",
    [
        FileNotFoundError(),
        subprocess.CalledProcessError(1, ["gh", "auth", "token"]),
    ],
)
def test_get_github_token_falls_back_to_public_api(
    monkeypatch: pytest.MonkeyPatch, error: Exception
) -> None:
    monkeypatch.setattr(subprocess, "run", Mock(side_effect=error))

    assert get_github_token(None) is None


@pytest.mark.parametrize(
    ("count", "expected"),
    [
        (0, ""),
        (1, "-   1 upgrade závislostí na všech projektech."),
        (2, "-   2 upgrady závislostí na všech projektech."),
        (5, "-   5 upgradů závislostí na všech projektech."),
    ],
)
def test_format_upgrades(count: int, expected: str) -> None:
    assert format_upgrades(count) == expected


def test_get_contributed_owners() -> None:
    graphql = Mock()
    graphql.request.return_value = {
        "user": {
            "repositoriesContributedTo": {
                "nodes": [
                    {"owner": {"login": "honzajavorek", "__typename": "User"}},
                    {"owner": {"login": "juniorguru", "__typename": "Organization"}},
                    {"owner": {"login": "juniorguru", "__typename": "Organization"}},
                ]
            }
        }
    }
    github = cast(GitHub, SimpleNamespace(graphql=graphql))

    assert get_contributed_owners(github, "honzajavorek") == [
        "org:juniorguru",
        "user:honzajavorek",
    ]


def test_get_dependabot_closed_events() -> None:
    graphql = Mock()
    graphql.request.return_value = {
        "search": {
            "nodes": [
                {
                    "timelineItems": {
                        "nodes": [
                            {
                                "actor": {"login": "honzajavorek"},
                                "createdAt": "2026-08-04T09:02:09Z",
                            }
                        ]
                    }
                }
            ],
            "pageInfo": {"hasNextPage": False, "endCursor": None},
        }
    }
    github = cast(GitHub, SimpleNamespace(graphql=graphql))

    assert get_dependabot_closed_events(
        github, "user:honzajavorek", date(2026, 7, 24), date(2026, 8, 6)
    ) == [
        {
            "actor": {"login": "honzajavorek"},
            "createdAt": "2026-08-04T09:02:09Z",
        }
    ]


def test_get_closed_dependabot_prs_count(monkeypatch: pytest.MonkeyPatch) -> None:
    github_module = import_module("blog.weeknotes.github")
    monkeypatch.setattr(
        github_module,
        "get_contributed_owners",
        Mock(return_value=["user:honzajavorek"]),
    )
    monkeypatch.setattr(
        github_module,
        "get_dependabot_closed_events",
        Mock(
            return_value=[
                {
                    "actor": {"login": "honzajavorek"},
                    "createdAt": "2026-08-04T09:02:09Z",
                },
                {
                    "actor": {"login": "dependabot"},
                    "createdAt": "2026-08-04T09:02:09+00:00",
                },
            ]
        ),
    )

    assert (
        get_closed_dependabot_prs_count(
            Mock(),
            "honzajavorek",
            date(2026, 7, 24),
            date(2026, 8, 6),
            "Europe/Prague",
        )
        == 1
    )


def test_format_work_items() -> None:
    items = [
        WorkItem(
            "beta", "repo", 5, "https://example.com/beta/5", "Five", "pr", "orange"
        ),
        WorkItem(
            "alpha", "zeta", 4, "https://example.com/alpha/4", "Four", "issue", "orange"
        ),
        WorkItem(
            "alpha", "beta", 3, "https://example.com/alpha/3", "Three", "issue", "green"
        ),
        WorkItem(
            "alpha", "zeta", 2, "https://example.com/alpha/2", "Two", "pr", "orange"
        ),
        WorkItem(
            "alpha", "beta", 1, "https://example.com/alpha/1", "One", "pr", "green"
        ),
    ]

    assert (
        format_work_items(items)
        == """### Ostatní

-   🟢 [alpha/beta#1](https://example.com/alpha/1) – One
-   🟢 [alpha/beta#3](https://example.com/alpha/3) – Three
-   🟠 [alpha/zeta#2](https://example.com/alpha/2) – Two
-   🟠 [beta/repo#5](https://example.com/beta/5) – Five
-   🟠 [alpha/zeta#4](https://example.com/alpha/4) – Four"""
    )


@pytest.mark.parametrize(
    ("owner", "expected"),
    [
        ("juniorguru", "junior.guru"),
        ("apify", "Apify"),
        ("pyvec", "Python komunita"),
        ("honzajavorek", "Osobní projekty"),
        ("someone-else", "Ostatní"),
    ],
)
def test_format_section_name(owner: str, expected: str) -> None:
    assert format_section_name(owner) == expected


def test_get_contribution_work_item() -> None:
    contribution = {
        "number": 2849,
        "title": "Test-driven development",
        "url": "https://github.com/apify/apify-docs/pull/2849",
        "author": {"__typename": "User"},
        "mergedAt": None,
        "mergedBy": None,
        "repository": {"name": "apify-docs", "owner": {"login": "apify"}},
    }

    assert get_contribution_work_item(
        contribution,
        "pr",
        "honzajavorek",
        datetime(2026, 7, 24, tzinfo=UTC),
        datetime(2026, 8, 6, 23, 59, tzinfo=UTC),
    ) == WorkItem(
        "apify",
        "apify-docs",
        2849,
        "https://github.com/apify/apify-docs/pull/2849",
        "Test-driven development",
        "pr",
        "orange",
    )


def test_get_contribution_work_item_ignores_bot() -> None:
    contribution = {
        "author": {"__typename": "Bot"},
        "repository": {"name": "repo", "owner": {"login": "owner"}},
    }

    assert (
        get_contribution_work_item(
            contribution,
            "pr",
            "honzajavorek",
            datetime(2026, 7, 24, tzinfo=UTC),
            datetime(2026, 8, 6, 23, 59, tzinfo=UTC),
        )
        is None
    )


def test_get_contribution_work_item_is_green_when_merged_by_user() -> None:
    contribution = {
        "number": 2839,
        "title": "Fix docs",
        "url": "https://github.com/apify/apify-docs/pull/2839",
        "author": {"__typename": "User"},
        "mergedAt": "2026-07-31T15:00:00Z",
        "mergedBy": {"login": "honzajavorek"},
        "repository": {"name": "apify-docs", "owner": {"login": "apify"}},
    }

    assert get_contribution_work_item(
        contribution,
        "pr",
        "honzajavorek",
        datetime(2026, 7, 24, tzinfo=UTC),
        datetime(2026, 8, 6, 23, 59, tzinfo=UTC),
    ) == WorkItem(
        "apify",
        "apify-docs",
        2839,
        "https://github.com/apify/apify-docs/pull/2839",
        "Fix docs",
        "pr",
        "green",
    )


def test_get_contributions() -> None:
    graphql = Mock()
    graphql.request.return_value = {
        "user": {
            "contributionsCollection": {
                "pullRequestContributions": {
                    "nodes": [
                        {
                            "pullRequest": {
                                "number": 2849,
                                "title": "Test-driven development",
                                "url": "https://github.com/apify/apify-docs/pull/2849",
                                "author": {"__typename": "User"},
                                "mergedAt": None,
                                "mergedBy": None,
                                "repository": {
                                    "name": "apify-docs",
                                    "owner": {"login": "apify"},
                                },
                            }
                        }
                    ]
                },
                "pullRequestReviewContributions": {"nodes": []},
                "issueContributions": {"nodes": []},
            }
        }
    }
    github = cast(GitHub, SimpleNamespace(graphql=graphql))

    assert get_contributions(
        github,
        "honzajavorek",
        date(2026, 7, 24),
        date(2026, 8, 6),
        "Europe/Prague",
    ) == [
        WorkItem(
            "apify",
            "apify-docs",
            2849,
            "https://github.com/apify/apify-docs/pull/2849",
            "Test-driven development",
            "pr",
            "orange",
        )
    ]
