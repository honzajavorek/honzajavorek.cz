import subprocess
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date
from typing import Literal

from githubkit import GitHub
from githubkit_schemas.latest.models import (
    Event,
    IssuesEvent,
    PullRequest,
    PullRequestEvent,
    PullRequestReviewEvent,
    SimpleUser,
)


@dataclass(frozen=True)
class WorkItem:
    owner: str
    repo: str
    number: int
    url: str
    title: str
    kind: Literal["pr", "issue"]
    color: Literal["green", "orange"]


def get_github_token(token: str | None) -> str | None:
    if token:
        return token
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip() or None


def format_upgrades(count: int) -> str:
    if count == 0:
        return ""
    if count == 1:
        noun = "upgrade"
    elif 2 <= count <= 4:
        noun = "upgrady"
    else:
        noun = "upgradů"
    return f"-   {count} {noun} závislostí na všech projektech."


def get_closed_dependabot_prs_count(
    events: Iterable[Event],
    pull_requests: dict[tuple[str, str, int], PullRequest],
) -> int:
    count = 0
    for event in events:
        if (
            event.type == "PullRequestEvent"
            and isinstance(event.payload, PullRequestEvent)
            and event.payload.action == "closed"
        ):
            owner, repo = event.repo.name.split("/", maxsplit=1)
            key = (owner, repo, event.payload.pull_request.number)
            pull_request = pull_requests[key]
            if is_bot(pull_request.user):
                count += 1
    return count


def get_work_items(
    username: str,
    events: Iterable[Event],
    pull_requests: dict[tuple[str, str, int], PullRequest],
) -> list[WorkItem]:
    items: dict[tuple[str, str, int], WorkItem] = {}
    for event in events:
        repo_name = event.repo.name
        owner, repo = repo_name.split("/", maxsplit=1)
        item = get_work_item(event, owner, repo, username, pull_requests)
        if item is None:
            continue

        key = (item.kind, repo_name, item.number)
        current_item = items.get(key)
        if current_item is None or item.color == "green":
            items[key] = item
    return list(items.values())


def get_events(
    github: GitHub, username: str, since_date: date, today: date
) -> list[Event]:
    def fetch_page(page: int) -> list[Event]:
        return github.rest.activity.list_public_events_for_user(
            username, per_page=100, page=page
        ).parsed_data

    with ThreadPoolExecutor(max_workers=3) as executor:
        pages = executor.map(fetch_page, range(1, 4))
        events = [event for page in pages for event in page]

    relevant_events = []
    for event in events:
        if event.created_at is None:
            continue
        event_date = event.created_at.date()
        if event_date < since_date:
            break
        if event_date <= today:
            relevant_events.append(event)
    return relevant_events


def get_pull_requests(
    github: GitHub, events: Iterable[Event]
) -> dict[tuple[str, str, int], PullRequest]:
    keys = set()
    for event in events:
        payload = event.payload
        if isinstance(payload, (PullRequestEvent, PullRequestReviewEvent)):
            owner, repo = event.repo.name.split("/", maxsplit=1)
            keys.add((owner, repo, payload.pull_request.number))
    if not keys:
        return {}

    def fetch(key: tuple[str, str, int]) -> tuple[tuple[str, str, int], PullRequest]:
        owner, repo, number = key
        pull_request = github.rest.pulls.get(owner, repo, number).parsed_data
        return key, pull_request

    with ThreadPoolExecutor(max_workers=min(16, len(keys))) as executor:
        return dict(executor.map(fetch, sorted(keys)))


def get_work_item(
    event: Event,
    owner: str,
    repo: str,
    username: str,
    pull_requests: dict[tuple[str, str, int], PullRequest],
) -> WorkItem | None:
    payload = event.payload
    if event.type == "PullRequestEvent" and isinstance(payload, PullRequestEvent):
        if payload.action not in {"opened", "closed"}:
            return None
        if payload.action == "opened":
            pull_request = pull_requests[(owner, repo, payload.pull_request.number)]
            return WorkItem(
                owner,
                repo,
                pull_request.number,
                str(pull_request.html_url),
                pull_request.title,
                "pr",
                "orange",
            )

        pull_request = pull_requests[(owner, repo, payload.pull_request.number)]
        if is_bot(pull_request.user):
            return None
        if payload.action == "closed":
            if not pull_request.merged or pull_request.merged_by is None:
                return None
            if pull_request.merged_by.login != username:
                return None
            color = "green"
        else:
            color = "orange"
        return WorkItem(
            owner,
            repo,
            pull_request.number,
            str(pull_request.html_url),
            pull_request.title,
            "pr",
            color,
        )

    if event.type == "PullRequestReviewEvent" and isinstance(
        payload, PullRequestReviewEvent
    ):
        if payload.action != "created":
            return None
        pull_request = pull_requests[(owner, repo, payload.pull_request.number)]
        if is_bot(pull_request.user):
            return None
        return WorkItem(
            owner,
            repo,
            pull_request.number,
            str(pull_request.html_url),
            pull_request.title,
            "pr",
            "orange",
        )

    if event.type == "IssuesEvent" and isinstance(payload, IssuesEvent):
        if payload.action not in {"opened", "closed"}:
            return None
        issue = payload.issue
        if issue.user is None or is_bot(issue.user):
            return None
        color = "green" if payload.action == "closed" else "orange"
        return WorkItem(
            owner,
            repo,
            issue.number,
            str(issue.html_url),
            issue.title,
            "issue",
            color,
        )

    return None


def is_bot(user: SimpleUser) -> bool:
    return user.type == "Bot"


def format_work_items(items: Iterable[WorkItem]) -> str:
    grouped: dict[str, list[WorkItem]] = {}
    for item in items:
        grouped.setdefault(item.owner, []).append(item)

    sections = []
    for owner, owner_items in sorted(grouped.items()):
        lines = [f"### {owner}", ""]
        for item in sorted(owner_items, key=work_item_sort_key):
            emoji = "🟢" if item.color == "green" else "🟠"
            lines.append(
                f"-   {emoji} [{item.owner}/{item.repo}#{item.number}]({item.url})"
                f" – {item.title}"
            )
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def work_item_sort_key(item: WorkItem) -> tuple[int, int, str, int]:
    return (
        0 if item.kind == "pr" else 1,
        0 if item.color == "green" else 1,
        item.repo,
        item.number,
    )
