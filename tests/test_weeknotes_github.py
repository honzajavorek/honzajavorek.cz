from datetime import date
from pathlib import Path
from types import SimpleNamespace
from typing import cast
from unittest.mock import Mock

import pytest
from githubkit import GitHub
from githubkit_schemas.latest.models import Event
from pydantic import TypeAdapter

from blog.weeknotes.github import format_upgrades, get_closed_dependabot_prs_count


@pytest.fixture
def github() -> GitHub:
    fixture_path = Path(__file__).parent / "fixtures" / "github_events.json"
    events = TypeAdapter(list[Event]).validate_json(fixture_path.read_text())
    activity = SimpleNamespace(list_public_events_for_user=Mock())
    rest = SimpleNamespace(activity=activity, paginate=Mock(return_value=events))
    return cast(GitHub, SimpleNamespace(rest=rest))


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
    ("since_date", "expected"),
    [
        (date(2026, 2, 1), 1),
        (date(2026, 2, 17), 0),
    ],
)
def test_get_closed_dependabot_prs_count(
    github: GitHub, since_date: date, expected: int
) -> None:
    assert (
        get_closed_dependabot_prs_count(github, "honzajavorek", since_date) == expected
    )


def test_get_closed_dependabot_prs_uses_public_events(github: GitHub) -> None:
    get_closed_dependabot_prs_count(github, "honzajavorek", date(2026, 2, 1))

    assert github.rest.paginate.call_args.args == (
        github.rest.activity.list_public_events_for_user,
        "honzajavorek",
    )
