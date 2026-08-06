import json
from datetime import date, datetime
from pathlib import Path
from string import Template
from types import ModuleType
from zoneinfo import ZoneInfo

import click
from githubkit import GitHub
from githubkit_schemas.latest.models import PullRequest
from slugify import slugify

from blog.lib import SettingsModuleParam
from blog.toots import main as toots_command
from blog.update import main as update_command
from blog.weeknotes.github import (
    format_upgrades,
    format_work_items,
    get_closed_dependabot_prs_count,
    get_events,
    get_github_token,
    get_pull_requests,
    get_work_items,
)
from blog.weeknotes.jg_toots import format_toots, get_jg_toots
from blog.weeknotes.links import format_links, get_links


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument("title")
@click.option(
    "--path",
    "content_path",
    default="content",
    type=click.Path(exists=True, path_type=Path),
)
@click.option("--title-prefix", default="Týdenní poznámky")
@click.option("--timezone", default="Europe/Prague")
@click.option("--github-token", envvar="GITHUB_TOKEN")
@click.option("--github-username", default="honzajavorek")
@click.option("--settings-module", default="pelicanconf.py", type=SettingsModuleParam())
@click.option(
    "--links-path",
    default="content/data/toots-links.json",
    type=click.Path(exists=True, path_type=Path),
)
@click.option(
    "--jg-toots-path",
    default="content/data/toots-jg.json",
    type=click.Path(exists=True, path_type=Path),
)
@click.option("--mastodon-client_id", envvar="MASTODON_CLIENT_ID")
@click.option("--mastodon-client_secret", envvar="MASTODON_CLIENT_SECRET")
@click.option("--mastodon-access_token", envvar="MASTODON_ACCESS_TOKEN")
@click.option("--update/--no-update", default=True)
@click.option("--debug/--no-debug", default=False)
@click.option("--open/--no-open", default=True)
@click.pass_context
def main(
    context: click.Context,
    title: str,
    content_path: Path,
    title_prefix: str,
    timezone: str,
    github_token: str | None,
    github_username: str,
    settings_module: ModuleType,
    links_path: Path,
    jg_toots_path: Path,
    mastodon_client_id: str | None,
    mastodon_client_secret: str | None,
    mastodon_access_token: str | None,
    update: bool,
    debug: bool,
    open: bool,
) -> None:
    if update:
        context.invoke(update_command)
        context.invoke(
            toots_command,
            client_id=mastodon_client_id,
            client_secret=mastodon_client_secret,
            access_token=mastodon_access_token,
        )

    today = datetime.now(ZoneInfo(timezone)).date()
    today_cz = format_weeknotes_date(today)

    last_weeknotes_path = get_last_weeknotes_path(content_path, title_prefix)
    last_weeknotes_date = get_weeknotes_date(last_weeknotes_path)
    last_weeknotes_date_cz = format_weeknotes_date(last_weeknotes_date)
    github = GitHub(get_github_token(github_token))
    events = get_events(github, github_username, last_weeknotes_date, today)
    pull_requests: dict[tuple[str, str, int], PullRequest] = get_pull_requests(
        github, events
    )
    closed_dependabot_prs_count = get_closed_dependabot_prs_count(events, pull_requests)
    github_work = format_work_items(
        get_work_items(github_username, events, pull_requests)
    )

    # mastodon links
    links = get_links(last_weeknotes_date, json.loads(links_path.read_text()))
    links_text = format_links(links)

    # mastodon jg
    jg_toots = get_jg_toots(last_weeknotes_date, json.loads(jg_toots_path.read_text()))
    jg_toots_text = format_toots(jg_toots)

    # generate weeknotes
    title = format_title(title, title_prefix)
    path = get_weeknotes_path(content_path, title, today)
    last_weeknotes_path = format_last_weeknotes_path(last_weeknotes_path, content_path)
    content = format_content(
        title=title,
        weeknotes_tag=settings_module.WEEKNOTES_TAG,
        last_weeknotes_path=last_weeknotes_path,
        last_weeknotes_date=last_weeknotes_date_cz,
        today=today_cz,
        jg_toots=jg_toots_text,
        links=links_text,
        dependabot_upgrades=format_upgrades(closed_dependabot_prs_count),
        github_work=github_work,
    )
    if debug:
        debug_print(path, content)
    else:
        path.write_text(content)
        if open:
            edit(path)


def debug_print(path: Path, content: str) -> None:
    click.secho(path.name, bold=True)
    click.echo("")
    click.echo(content)


def edit(path: Path) -> None:
    click.edit(filename=".")
    click.edit(filename=str(path))


def format_title(title: str, title_prefix: str) -> str:
    return f"{title_prefix}: {title}"


def format_content(
    title: str,
    weeknotes_tag: str,
    last_weeknotes_path: str,
    last_weeknotes_date: str,
    today: str,
    jg_toots: str,
    links: str,
    dependabot_upgrades: str,
    github_work: str,
) -> str:
    template_path = Path(__file__).with_name("template.md")
    return Template(template_path.read_text()).substitute(
        title=title,
        weeknotes_tag=weeknotes_tag,
        last_weeknotes_path=last_weeknotes_path,
        last_weeknotes_date=last_weeknotes_date,
        today=today,
        jg_toots=jg_toots,
        links=links.rstrip("\n"),
        dependabot_upgrades=dependabot_upgrades,
        github_work=github_work,
    )


def format_last_weeknotes_path(last_weeknotes_path: Path, content_path: Path) -> str:
    return "{filename}" + str(last_weeknotes_path.relative_to(content_path))


def get_weeknotes_date(path: Path) -> date:
    return date.fromisoformat(path.stem[:10])


def format_weeknotes_date(weeknotes_date: date) -> str:
    return f"{weeknotes_date:%-d}. {weeknotes_date:%-m}."


def get_weeknotes_path(content_path: Path, title: str, weeknotes_date: date) -> Path:
    return content_path / f"{weeknotes_date.isoformat()}_{slugify(title)}.md"


def get_last_weeknotes_path(content_path: Path, title_prefix: str) -> Path:
    is_weeknotes = lambda path: slugify(title_prefix) in path.name
    weeknotes_paths = sorted(filter(is_weeknotes, content_path.glob("*.md")))
    return weeknotes_paths[-1]
