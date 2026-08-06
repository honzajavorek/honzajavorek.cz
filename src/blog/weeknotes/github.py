import subprocess
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date, datetime, time
from typing import Any, Literal
from zoneinfo import ZoneInfo

from githubkit import GitHub


@dataclass(frozen=True)
class LinkedIssue:
    owner: str
    repo: str
    number: int
    url: str


@dataclass(frozen=True)
class LinkedPullRequest:
    owner: str
    repo: str
    number: int


@dataclass(frozen=True)
class WorkItem:
    owner: str
    repo: str
    number: int
    url: str
    title: str
    kind: Literal["pr", "review", "issue"]
    state: Literal["completed", "pending", "review"]
    closed_by_pull_requests: tuple[LinkedPullRequest, ...] = ()


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
            closedAt
            repository { name owner { login } }
            closedByPullRequestsReferences(first: 100, includeClosedPrs: true) {
              nodes { number repository { name owner { login } } }
            }
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
  author { __typename login }
  mergedAt
  mergedBy { login }
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

SECTION_NAMES = {
    "juniorguru": "junior.guru",
    "apify": "Apify",
    "pyvec": "Python komunita",
    "honzajavorek": "Osobní projekty",
}


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
    until = datetime.combine(today, time.max, tz)
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
        item = get_contribution_work_item(contribution["pullRequest"], "pr", until)
        if item is not None:
            items.append(item)
    for contribution in collection["pullRequestReviewContributions"]["nodes"]:
        if is_own_pull_request(contribution["pullRequest"], username):
            continue
        item = get_contribution_work_item(contribution["pullRequest"], "review", until)
        if item is not None:
            items.append(item)
    for contribution in collection["issueContributions"]["nodes"]:
        item = get_contribution_work_item(contribution["issue"], "issue", until)
        if item is not None:
            items.append(item)
    return list(dict.fromkeys(items))


def is_own_pull_request(pull_request: dict[str, Any], username: str) -> bool:
    author = pull_request["author"]
    return author is not None and author["login"] == username


def get_contribution_work_item(
    contribution: dict[str, Any],
    kind: Literal["pr", "review", "issue"],
    until: datetime,
) -> WorkItem | None:
    author = contribution["author"]
    if author is not None and author["__typename"] == "Bot":
        return None
    repository = contribution["repository"]
    state = "review" if kind == "review" else "pending"
    is_merged = (
        kind == "pr"
        and contribution["mergedAt"] is not None
        and datetime.fromisoformat(contribution["mergedAt"]) <= until
    )
    if is_merged:
        state = "completed"
    if (
        kind == "issue"
        and contribution["closedAt"] is not None
        and datetime.fromisoformat(contribution["closedAt"]) <= until
    ):
        state = "completed"
    closed_by_pull_requests = ()
    if kind == "issue":
        closed_by_pull_requests = tuple(
            LinkedPullRequest(
                pull_request["repository"]["owner"]["login"],
                pull_request["repository"]["name"],
                pull_request["number"],
            )
            for pull_request in contribution["closedByPullRequestsReferences"]["nodes"]
        )
    return WorkItem(
        repository["owner"]["login"],
        repository["name"],
        contribution["number"],
        contribution["url"],
        contribution["title"],
        kind,
        state,
        closed_by_pull_requests,
    )


def format_work_items(items: Iterable[WorkItem]) -> str:
    items = list(items)
    authored_pr_keys = {
        (item.owner, item.repo, item.number) for item in items if item.kind == "pr"
    }
    linked_issues_by_pr: dict[tuple[str, str, int], list[LinkedIssue]] = {}
    for item in items:
        if item.kind != "issue":
            continue
        for pull_request in item.closed_by_pull_requests:
            key = (pull_request.owner, pull_request.repo, pull_request.number)
            if key not in authored_pr_keys:
                continue
            linked_issues_by_pr.setdefault(key, []).append(
                LinkedIssue(item.owner, item.repo, item.number, item.url)
            )
    linked_issue_keys = {
        (issue.owner, issue.repo, issue.number)
        for linked_issues in linked_issues_by_pr.values()
        for issue in linked_issues
    }
    grouped: dict[str, list[WorkItem]] = {}
    for item in items:
        grouped.setdefault(format_section_name(item.owner), []).append(item)

    sections = []
    section_names = [*SECTION_NAMES.values(), "Ostatní"]
    for section_name in section_names:
        section_items = grouped.get(section_name)
        if section_items is None:
            continue
        counts = {
            kind: sum(item.kind == kind for item in section_items)
            for kind in ("pr", "review", "issue")
        }
        lines = [
            f"## {section_name} ({format_contribution_counts(counts)})",
            "",
        ]
        display_items: dict[tuple[str, str, int], WorkItem] = {}
        for item in section_items:
            key = (item.owner, item.repo, item.number)
            if item.kind == "issue" and key in linked_issue_keys:
                continue
            current_item = display_items.get(key)
            if current_item is None or state_sort_key(item.state) < state_sort_key(
                current_item.state
            ):
                display_items[key] = item
        for item in sorted(display_items.values(), key=work_item_sort_key):
            emoji = format_work_item_marker(item)
            key = (item.owner, item.repo, item.number)
            lines.append(
                f"-   {emoji} [{format_work_item_label(item, section_name)}]({item.url})"
                f"{format_linked_issues(item, linked_issues_by_pr.get(key, []))}"
                f" – {item.title}"
            )
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def format_section_name(owner: str) -> str:
    return SECTION_NAMES.get(owner, "Ostatní")


def format_contribution_counts(counts: dict[str, int]) -> str:
    labels = {"pr": "PRs", "review": "reviews", "issue": "issues"}
    return ", ".join(
        f"{counts[kind]} {labels[kind]}"
        for kind in ("pr", "review", "issue")
        if counts[kind]
    )


def format_work_item_marker(item: WorkItem) -> str:
    if item.kind == "review":
        return "👀🧠"
    if item.kind == "pr":
        return "🛠️✅" if item.state == "completed" else "🛠️"
    return "📝✅" if item.state == "completed" else "📝"


def format_work_item_label(item: WorkItem, section_name: str) -> str:
    if section_name == "Ostatní":
        return f"{item.owner}/{item.repo}#{item.number}"
    return f"{item.repo}#{item.number}"


def format_linked_issues(item: WorkItem, linked_issues: Iterable[LinkedIssue]) -> str:
    linked_issues = list(linked_issues)
    if not linked_issues:
        return ""
    links = []
    for issue in linked_issues:
        label = f"#{issue.number}"
        if (issue.owner, issue.repo) != (item.owner, item.repo):
            label = f"{issue.owner}/{issue.repo}#{issue.number}"
        links.append(f"[{label}]({issue.url})")
    return f" ({', '.join(links)})"


def state_sort_key(state: Literal["completed", "pending", "review"]) -> int:
    return {"completed": 0, "pending": 1, "review": 2}[state]


def work_item_sort_key(item: WorkItem) -> tuple[int, int, str, str, int]:
    if item.state == "completed":
        activity_order = 0 if item.kind == "pr" else 1
    elif item.kind == "review":
        activity_order = 3
    else:
        activity_order = 2 if item.kind == "pr" else 4
    return (
        activity_order,
        0,
        item.owner,
        item.repo,
        item.number,
    )
