from datetime import date

from githubkit import GitHub
from githubkit_schemas.latest.models import PullRequestEvent


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
    github: GitHub, username: str, since_date: date
) -> int:
    events = github.rest.paginate(
        github.rest.activity.list_public_events_for_user,
        username,
    )
    count = 0
    for event in events:
        if event.created_at is None:
            continue
        if event.created_at.date() < since_date:
            break
        if (
            event.type == "PullRequestEvent"
            and isinstance(event.payload, PullRequestEvent)
            and event.payload.action == "closed"
            and event.payload.pull_request.head.ref.startswith("dependabot/")
        ):
            count += 1
    return count
