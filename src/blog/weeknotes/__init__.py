import json
from datetime import date, datetime
from pathlib import Path
from textwrap import dedent
from types import ModuleType
from zoneinfo import ZoneInfo

import click
from slugify import slugify

from blog.lib import SettingsModuleParam
from blog.toots import main as toots_command
from blog.update import main as update_command
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
@click.option("--debug/--no-debug", default=False)
@click.option("--open/--no-open", default=True)
@click.pass_context
def main(
    context: click.Context,
    title: str,
    content_path: Path,
    title_prefix: str,
    timezone: str,
    settings_module: ModuleType,
    links_path: Path,
    jg_toots_path: Path,
    mastodon_client_id: str | None,
    mastodon_client_secret: str | None,
    mastodon_access_token: str | None,
    debug: bool,
    open: bool,
) -> None:
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

    # mastodon links
    links = get_links(last_weeknotes_date, json.loads(links_path.read_text()))

    # mastodon jg
    jg_toots = get_jg_toots(last_weeknotes_date, json.loads(jg_toots_path.read_text()))
    jg_toots_text = format_toots(jg_toots)

    # generate weeknotes
    title = format_title(title, title_prefix)
    path = get_weeknotes_path(content_path, title, today)
    last_weeknotes_path = format_last_weeknotes_path(last_weeknotes_path, content_path)
    content = dedent(
        f"""
        Title: {title}
        Image: images/markus-spiske-RiSAjGsa0vg-unsplash.jpg
        Lang: cs
        Tags: {settings_module.WEEKNOTES_TAG}, junior.guru

        Jak se mi daří v jednom člověku provozovat a rozvíjet [junior.guru](https://junior.guru/)?
        Od [posledních poznámek]({last_weeknotes_path}) už utekl nějaký ten týden ({last_weeknotes_date_cz} až {today_cz}), tak nastal čas se opět ohlédnout a utřídit si myšlenky.

        ![Poznámky]({{static}}/images/markus-spiske-RiSAjGsa0vg-unsplash.jpg)
        Fotil [Markus Spiske](https://unsplash.com/@markusspiske)

        <div class="alert alert-warning" role="alert" markdown="1">
        **Čísla:** Finanční výsledky, návštěvnost a další čísla k junior.guru [mám přímo na webu](https://junior.guru/about/).
        </div>

        {jg_toots_text}

        ## Další

        -   E-maily, [klubový Discord](https://junior.guru/club/), [Pyvec Slack](https://docs.pyvec.org/operations/support.html#sit-kontaktu), zprávy na LinkedIn, upgrady závislostí na všech projektech.

        ## Plánuji

        1.
        2.
        3.

        ## Zaujalo mě

        Když na něco narazím a líbí se mi to, sdílím to [na Mastodonu](https://mastodonczech.cz/@honzajavorek).
        Od posledních poznámek jsem sdílel:

    """
    ).lstrip()
    content += format_links(links)

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
