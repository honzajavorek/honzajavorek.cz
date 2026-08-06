import subprocess
from datetime import UTC, date, datetime
from importlib import import_module
from types import SimpleNamespace
from typing import Literal, cast
from unittest.mock import Mock

import pytest
from githubkit import GitHub

from blog.weeknotes.github import (
    Contributions,
    LinkedIssue,
    LinkedPullRequest,
    RepoCommits,
    WorkItem,
    format_contribution_counts,
    format_linked_issues,
    format_repo_commits,
    format_section_name,
    format_upgrades,
    format_work_item_label,
    format_work_item_marker,
    format_work_items,
    get_closed_dependabot_prs_count,
    get_contributed_owners,
    get_contribution_work_item,
    get_contributions,
    get_dependabot_closed_events,
    get_github_token,
    is_own_pull_request,
    state_sort_key,
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
            "beta", "repo", 5, "https://example.com/beta/5", "Five", "pr", "pending"
        ),
        WorkItem(
            "alpha",
            "zeta",
            4,
            "https://example.com/alpha/4",
            "Four",
            "issue",
            "pending",
        ),
        WorkItem(
            "alpha",
            "beta",
            3,
            "https://example.com/alpha/3",
            "Three",
            "issue",
            "completed",
            (LinkedPullRequest("alpha", "beta", 1),),
        ),
        WorkItem(
            "alpha", "zeta", 2, "https://example.com/alpha/2", "Two", "pr", "pending"
        ),
        WorkItem(
            "alpha",
            "beta",
            1,
            "https://example.com/alpha/1",
            "One",
            "pr",
            "completed",
        ),
        WorkItem(
            "alpha",
            "beta",
            1,
            "https://example.com/alpha/1",
            "One",
            "review",
            "completed",
        ),
        WorkItem(
            "gamma",
            "docs",
            6,
            "https://example.com/gamma/6",
            "Six",
            "review",
            "review",
        ),
    ]

    assert (
        format_work_items(
            items,
            [RepoCommits("alpha", "beta", "https://example.com/alpha/beta", 8)],
        )
        == """## Ostatní (3 PRs, 2 reviews, 2 issues)

-   🛠️✅ 8 commits do [alpha/beta](https://example.com/alpha/beta/)
-   🛠️✅ [alpha/beta#1](https://example.com/alpha/1) ([#3](https://example.com/alpha/3)) – One
-   🛠️ [alpha/zeta#2](https://example.com/alpha/2) – Two
-   🛠️ [beta/repo#5](https://example.com/beta/5) – Five
-   👀🧠 [gamma/docs#6](https://example.com/gamma/6) – Six
-   📝 [alpha/zeta#4](https://example.com/alpha/4) – Four"""
    )


def test_format_work_items_does_not_link_issue_to_review() -> None:
    items = [
        WorkItem(
            "alpha", "repo", 1, "https://example.com/pr/1", "PR", "review", "review"
        ),
        WorkItem(
            "alpha",
            "repo",
            2,
            "https://example.com/issues/2",
            "Issue",
            "issue",
            "pending",
            (LinkedPullRequest("alpha", "repo", 1),),
        ),
    ]

    assert (
        format_work_items(items)
        == """## Ostatní (1 reviews, 1 issues)

-   👀🧠 [alpha/repo#1](https://example.com/pr/1) – PR
-   📝 [alpha/repo#2](https://example.com/issues/2) – Issue"""
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


@pytest.mark.parametrize(
    ("counts", "expected"),
    [
        ({"pr": 24, "review": 5, "issue": 0}, "24 PRs, 5 reviews"),
        ({"pr": 0, "review": 5, "issue": 2}, "5 reviews, 2 issues"),
        ({"pr": 1, "review": 0, "issue": 0}, "1 PRs"),
    ],
)
def test_format_contribution_counts(counts: dict[str, int], expected: str) -> None:
    assert format_contribution_counts(counts) == expected


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
        datetime(2026, 8, 6, 23, 59, tzinfo=UTC),
    ) == WorkItem(
        "apify",
        "apify-docs",
        2849,
        "https://github.com/apify/apify-docs/pull/2849",
        "Test-driven development",
        "pr",
        "pending",
    )


@pytest.mark.parametrize(
    ("author", "expected"),
    [
        ({"login": "honzajavorek"}, True),
        ({"login": "someone-else"}, False),
        (None, False),
    ],
)
def test_is_own_pull_request(author: dict[str, str] | None, expected: bool) -> None:
    pull_request = {"author": author}

    assert is_own_pull_request(pull_request, "honzajavorek") is expected


def test_get_contribution_work_item_ignores_bot() -> None:
    contribution = {
        "author": {"__typename": "Bot"},
        "repository": {"name": "repo", "owner": {"login": "owner"}},
    }

    assert (
        get_contribution_work_item(
            contribution,
            "pr",
            datetime(2026, 8, 6, 23, 59, tzinfo=UTC),
        )
        is None
    )


def test_get_contribution_work_item_is_completed_when_merged() -> None:
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
        datetime(2026, 8, 6, 23, 59, tzinfo=UTC),
    ) == WorkItem(
        "apify",
        "apify-docs",
        2839,
        "https://github.com/apify/apify-docs/pull/2839",
        "Fix docs",
        "pr",
        "completed",
    )


def test_get_contribution_work_item_is_review() -> None:
    contribution = {
        "number": 2801,
        "title": "Improve docs",
        "url": "https://github.com/apify/apify-docs/pull/2801",
        "author": {"__typename": "User"},
        "mergedAt": "2026-07-29T15:00:00Z",
        "mergedBy": {"login": "someone-else"},
        "repository": {"name": "apify-docs", "owner": {"login": "apify"}},
    }

    assert get_contribution_work_item(
        contribution,
        "review",
        datetime(2026, 8, 6, 23, 59, tzinfo=UTC),
    ) == WorkItem(
        "apify",
        "apify-docs",
        2801,
        "https://github.com/apify/apify-docs/pull/2801",
        "Improve docs",
        "review",
        "review",
    )


def test_get_contribution_work_item_links_pull_requests() -> None:
    contribution = {
        "number": 76,
        "title": "Use object properties",
        "url": "https://github.com/honzajavorek/fiobank/issues/76",
        "author": {"__typename": "User"},
        "closedAt": "2026-08-04T09:02:09Z",
        "repository": {"name": "fiobank", "owner": {"login": "honzajavorek"}},
        "closedByPullRequestsReferences": {
            "nodes": [
                {
                    "number": 77,
                    "repository": {
                        "name": "fiobank",
                        "owner": {"login": "honzajavorek"},
                    },
                },
                {
                    "number": 78,
                    "repository": {
                        "name": "fiobank",
                        "owner": {"login": "honzajavorek"},
                    },
                },
            ]
        },
    }

    assert get_contribution_work_item(
        contribution,
        "issue",
        datetime(2026, 8, 6, 23, 59, tzinfo=UTC),
    ) == WorkItem(
        "honzajavorek",
        "fiobank",
        76,
        "https://github.com/honzajavorek/fiobank/issues/76",
        "Use object properties",
        "issue",
        "completed",
        (
            LinkedPullRequest("honzajavorek", "fiobank", 77),
            LinkedPullRequest("honzajavorek", "fiobank", 78),
        ),
    )


@pytest.mark.parametrize(
    ("state", "expected"),
    [("completed", 0), ("pending", 1), ("review", 2)],
)
def test_state_sort_key(
    state: Literal["completed", "pending", "review"], expected: int
) -> None:
    assert state_sort_key(state) == expected


@pytest.mark.parametrize(
    ("kind", "state", "expected"),
    [
        ("pr", "completed", "🛠️✅"),
        ("issue", "completed", "📝✅"),
        ("review", "review", "👀🧠"),
        ("pr", "pending", "🛠️"),
        ("issue", "pending", "📝"),
    ],
)
def test_format_work_item_marker(
    kind: Literal["pr", "review", "issue"],
    state: Literal["completed", "pending", "review"],
    expected: str,
) -> None:
    item = WorkItem("owner", "repo", 1, "https://example.com", "Title", kind, state)

    assert format_work_item_marker(item) == expected


@pytest.mark.parametrize(
    ("section_name", "expected"),
    [
        ("Osobní projekty", "film2trello#324"),
        ("Ostatní", "honzajavorek/film2trello#324"),
    ],
)
def test_format_work_item_label(section_name: str, expected: str) -> None:
    item = WorkItem(
        "honzajavorek",
        "film2trello",
        324,
        "https://github.com/honzajavorek/film2trello/pull/324",
        "Title",
        "pr",
        "completed",
    )

    assert format_work_item_label(item, section_name) == expected


def test_format_repo_commits() -> None:
    commits = [
        RepoCommits("honzajavorek", "fiobank", "https://github.com/x/fiobank", 7),
        RepoCommits(
            "honzajavorek", "film2trello", "https://github.com/x/film2trello/", 18
        ),
    ]

    assert format_repo_commits(commits, "Osobní projekty") == (
        "-   🛠️✅ 18 commits do [film2trello](https://github.com/x/film2trello/), "
        "7 commits do [fiobank](https://github.com/x/fiobank/)"
    )


def test_format_linked_issues() -> None:
    item = WorkItem(
        "owner",
        "repo",
        1,
        "https://example.com/pr/1",
        "Title",
        "pr",
        "completed",
    )
    linked_issues = (
        LinkedIssue("owner", "repo", 2, "https://example.com/issues/2"),
        LinkedIssue("other", "elsewhere", 3, "https://example.com/issues/3"),
    )

    assert format_linked_issues(item, linked_issues) == (
        " ([#2](https://example.com/issues/2), "
        "[other/elsewhere#3](https://example.com/issues/3))"
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
                "pullRequestReviewContributions": {
                    "nodes": [
                        {
                            "pullRequest": {
                                "number": 2849,
                                "title": "Test-driven development",
                                "url": "https://github.com/apify/apify-docs/pull/2849",
                                "author": {
                                    "__typename": "User",
                                    "login": "honzajavorek",
                                },
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
                "issueContributions": {"nodes": []},
                "commitContributionsByRepository": [
                    {
                        "repository": {
                            "name": "apify-docs",
                            "url": "https://github.com/apify/apify-docs",
                            "owner": {"login": "apify"},
                        },
                        "contributions": {"totalCount": 6},
                    },
                    {
                        "repository": {
                            "name": "small",
                            "url": "https://github.com/apify/small",
                            "owner": {"login": "apify"},
                        },
                        "contributions": {"totalCount": 5},
                    },
                ],
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
    ) == Contributions(
        (
            WorkItem(
                "apify",
                "apify-docs",
                2849,
                "https://github.com/apify/apify-docs/pull/2849",
                "Test-driven development",
                "pr",
                "pending",
            ),
        ),
        (
            RepoCommits(
                "apify",
                "apify-docs",
                "https://github.com/apify/apify-docs",
                6,
            ),
        ),
    )
