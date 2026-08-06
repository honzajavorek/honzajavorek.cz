import subprocess
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date, datetime, time
from typing import Any, Literal
from zoneinfo import ZoneInfo

from githubkit import GitHub


@dataclass(frozen=True)
class WorkItem:
    owner: str
    repo: str
    number: int
    url: str
    title: str
    kind: Literal["pr", "issue"]
    color: Literal["green", "orange"]


CONTRIBUTIONS_QUERY = """
query($username: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $username) {
    contributionsCollection(from: $from, to: $to) {
      pullRequestContributions(first: 100) {
        nodes { pullRequest { ...pullRequest } }
      }
      pullRequestReviewContributions(first: 100) {
        nodes { pullRequest { ...pullRequest } }
      }
      issueContributions(first: 100) {
        nodes {
          issue {
            number
            title
            url
            author { __typename }
            repository { name owner { login } }
          }
        }
      }
    }
  }
}

fragment pullRequest on PullRequest {
  number
  title
  url
  author { __typename }
  repository { name owner { login } }
}
"""

CONTRIBUTED_OWNERS_QUERY = """
query($username: String!) {
  user(login: $username) {
    repositoriesContributedTo(
      first: 100
      includeUserRepositories: true
      contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, PULL_REQUEST_REVIEW]
    ) {
      nodes { owner { login __typename } }
    }
  }
}
"""

DEPENDABOT_PRS_QUERY = """
query($query: String!, $after: String) {
  search(type: ISSUE, query: $query, first: 100, after: $after) {
    nodes {
      ... on PullRequest {
        timelineItems(last: 1, itemTypes: [CLOSED_EVENT]) {
          nodes { ... on ClosedEvent { actor { login } createdAt } }
        }
      }
    }
    pageInfo { hasNextPage endCursor }
  }
}
"""


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
    except FileNotFoundError, subprocess.CalledProcessError:
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
    github: GitHub,
    username: str,
    since_date: date,
    today: date,
    timezone: str,
) -> int:
    owners = get_contributed_owners(github, username)
    with ThreadPoolExecutor(max_workers=len(owners) or 1) as executor:
        closed_events = executor.map(
            lambda owner: get_dependabot_closed_events(
                github, owner, since_date, today
            ),
            owners,
        )
    tz = ZoneInfo(timezone)
    since = datetime.combine(since_date, time.min, tz)
    until = datetime.combine(today, time.max, tz)
    return sum(
        event["actor"] is not None
        and event["actor"]["login"] == username
        and since <= datetime.fromisoformat(event["createdAt"]) <= until
        for owner_events in closed_events
        for event in owner_events
    )


def get_contributed_owners(github: GitHub, username: str) -> list[str]:
    result = github.graphql.request(CONTRIBUTED_OWNERS_QUERY, {"username": username})
    owners = result["user"]["repositoriesContributedTo"]["nodes"]
    return sorted(
        {
            f"{'org' if owner['owner']['__typename'] == 'Organization' else 'user'}:"
            f"{owner['owner']['login']}"
            for owner in owners
        }
    )


def get_dependabot_closed_events(
    github: GitHub,
    owner: str,
    since_date: date,
    today: date,
) -> list[dict[str, Any]]:
    query = f"is:pr author:app/dependabot closed:{since_date}..{today} {owner}"
    after = None
    events = []
    while True:
        result = github.graphql.request(
            DEPENDABOT_PRS_QUERY,
            {"query": query, "after": after},
        )["search"]
        for pull_request in result["nodes"]:
            events.extend(pull_request["timelineItems"]["nodes"])
        if not result["pageInfo"]["hasNextPage"]:
            return events
        after = result["pageInfo"]["endCursor"]


def get_contributions(
    github: GitHub,
    username: str,
    since_date: date,
    today: date,
    timezone: str,
) -> list[WorkItem]:
    tz = ZoneInfo(timezone)
    result = github.graphql.request(
        CONTRIBUTIONS_QUERY,
        {
            "username": username,
            "from": datetime.combine(since_date, time.min, tz).isoformat(),
            "to": datetime.combine(today, time.max, tz).isoformat(),
        },
    )
    collection = result["user"]["contributionsCollection"]
    items = []
    for contribution in collection["pullRequestContributions"]["nodes"]:
        item = get_contribution_work_item(contribution["pullRequest"], "pr")
        if item is not None:
            items.append(item)
    for contribution in collection["pullRequestReviewContributions"]["nodes"]:
        item = get_contribution_work_item(contribution["pullRequest"], "pr")
        if item is not None:
            items.append(item)
    for contribution in collection["issueContributions"]["nodes"]:
        item = get_contribution_work_item(contribution["issue"], "issue")
        if item is not None:
            items.append(item)
    return list(dict.fromkeys(items))


def get_contribution_work_item(
    contribution: dict[str, Any], kind: Literal["pr", "issue"]
) -> WorkItem | None:
    author = contribution["author"]
    if author is not None and author["__typename"] == "Bot":
        return None
    repository = contribution["repository"]
    return WorkItem(
        repository["owner"]["login"],
        repository["name"],
        contribution["number"],
        contribution["url"],
        contribution["title"],
        kind,
        "orange",
    )


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
        0 if item.color == "green" else 1,
        0 if item.kind == "pr" else 1,
        item.repo,
        item.number,
    )
