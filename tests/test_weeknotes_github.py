import subprocess
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from typing import cast
from unittest.mock import Mock

import pytest
from githubkit import GitHub
from githubkit_schemas.latest.models import Event, SimpleUser
from pydantic import TypeAdapter

from blog.weeknotes.github import (
    WorkItem,
    format_upgrades,
    format_work_items,
    get_closed_dependabot_prs_count,
    get_events,
    get_github_token,
    get_pull_requests,
    is_bot,
)


@pytest.fixture
def github() -> GitHub:
    fixture_path = Path(__file__).parent / "fixtures" / "github_events.json"
    events = TypeAdapter(list[Event]).validate_json(fixture_path.read_text())

    def list_public_events_for_user(
        username: str, *, per_page: int, page: int
    ) -> SimpleNamespace:
        return SimpleNamespace(parsed_data=events if page == 1 else [])

    activity = SimpleNamespace(
        list_public_events_for_user=Mock(side_effect=list_public_events_for_user)
    )
    pull_request = SimpleNamespace(user=SimpleNamespace(type="Bot"))
    pulls = SimpleNamespace(
        get=Mock(return_value=SimpleNamespace(parsed_data=pull_request))
    )
    rest = SimpleNamespace(
        activity=activity,
        pulls=pulls,
    )
    return cast(GitHub, SimpleNamespace(rest=rest))


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
        (3, "-   3 upgrady závislostí na všech projektech."),
        (4, "-   4 upgrady závislostí na všech projektech."),
        (5, "-   5 upgradů závislostí na všech projektech."),
        (21, "-   21 upgradů závislostí na všech projektech."),
    ],
)
def test_format_upgrades(count: int, expected: str) -> None:
    assert format_upgrades(count) == expected


@pytest.mark.parametrize(
    ("account_type", "expected"),
    [
        ("Bot", True),
        ("User", False),
        ("Organization", False),
    ],
)
def test_is_bot(account_type: str, expected: bool) -> None:
    user = cast(SimpleUser, SimpleNamespace(type=account_type))

    assert is_bot(user) is expected


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
        == """### alpha

-   🟢 [alpha/beta#1](https://example.com/alpha/1) – One
-   🟠 [alpha/zeta#2](https://example.com/alpha/2) – Two
-   🟢 [alpha/beta#3](https://example.com/alpha/3) – Three
-   🟠 [alpha/zeta#4](https://example.com/alpha/4) – Four

### beta

-   🟠 [beta/repo#5](https://example.com/beta/5) – Five"""
    )


@pytest.mark.parametrize(
    ("since_date", "expected"),
    [
        (date(2026, 2, 1), 1),
        (date(2026, 2, 17), 0),
    ],
)
def test_get_closed_dependabot_prs_count(
    github: GitHub, since_date: date, expected: int
) -> None:
    events = get_events(github, "honzajavorek", since_date, date(2026, 2, 28))
    pull_requests = get_pull_requests(github, events)

    assert get_closed_dependabot_prs_count(events, pull_requests) == expected


def test_get_closed_dependabot_prs_uses_public_events(github: GitHub) -> None:
    get_events(github, "honzajavorek", date(2026, 2, 1), date(2026, 2, 28))

    assert {
        (call.args, tuple(sorted(call.kwargs.items())))
        for call in github.rest.activity.list_public_events_for_user.call_args_list
    } == {
        (("honzajavorek",), (("page", 1), ("per_page", 100))),
        (("honzajavorek",), (("page", 2), ("per_page", 100))),
        (("honzajavorek",), (("page", 3), ("per_page", 100))),
    }


def test_get_pull_requests_fetches_each_pr_once(github: GitHub) -> None:
    events = get_events(github, "honzajavorek", date(2026, 2, 1), date(2026, 2, 28))

    assert (
        set(get_pull_requests(github, [*events, *events])),
        github.rest.pulls.get.call_count,
    ) == ({("honzajavorek", "film2trello", 297)}, 1)
