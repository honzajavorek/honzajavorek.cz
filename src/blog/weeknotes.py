import json
import re
from pathlib import Path
from datetime import date, datetime
from urllib.parse import urlparse
from textwrap import dedent

from lxml.html import soupparser as html_soup
import requests
import click
from slugify import slugify

from blog.lib import SettingsModuleParam
from blog.update import main as update_command
from blog.toots import main as toots_command


TITLES = {
    "www.facebook.com": "(něco na Facebooku)",
    "facebook.com": "(něco na Facebooku)",
    "twitter.com": "(něco na Twitteru)",
    "mobile.twitter.com": "(něco na Twitteru)",
}


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument("title")
@click.option(
    "--path",
    "content_path",
    default="content",
    type=click.Path(exists=True, path_type=Path),
)
@click.option("--title-prefix", default="Týdenní poznámky")
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
    context,
    title,
    content_path,
    title_prefix,
    settings_module,
    links_path,
    jg_toots_path,
    mastodon_client_id,
    mastodon_client_secret,
    mastodon_access_token,
    debug,
    open,
):
    context.invoke(update_command)
    context.invoke(
        toots_command,
        client_id=mastodon_client_id,
        client_secret=mastodon_client_secret,
        access_token=mastodon_access_token,
    )

    today = date.today()
    today_cz = f"{today:%-d}. {today:%-m}."
    today_iso = today.isoformat()

    is_weeknotes = lambda path: slugify(title_prefix) in path.name
    weeknotes_paths = sorted(filter(is_weeknotes, content_path.glob("*.md")))
    last_weeknotes_path = weeknotes_paths[-1]
    last_weeknotes_date = date.fromisoformat(last_weeknotes_path.stem[:10])
    last_weeknotes_date_cz = f"{last_weeknotes_date:%-d}. {last_weeknotes_date:%-m}."
    prefix = f"{title_prefix}: "

    # mastodon links
    links = get_links(last_weeknotes_date, json.loads(links_path.read_text()))

    # mastodon jg
    jg_toots = get_jg_toots(last_weeknotes_date, json.loads(jg_toots_path.read_text()))
    jg_toots_text = "\n        ".join([f"-   {toot['url']}" for toot in jg_toots])

    # generate weeknotes
    title = f"{prefix}{title}"
    path = content_path / f"{today_iso}_{slugify(title)}.md"
    last_weeknotes_path = "{filename}" + str(
        last_weeknotes_path.relative_to(content_path)
    )
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
    for link in links:
        content += f"- [{link['title']}]({link['url']})"
        content += f"<br>{link['comment']}" if link["comment"] else ""
        content += "\n"

    if debug:
        click.secho(path.name, bold=True)
        click.echo("")
        click.echo(content)
    else:
        path.write_text(content)
        if open:
            click.edit(filename=".")
            click.edit(filename=str(path))


def get_jg_toots(since_date: date, toots: list):
    for toot in toots:
        if datetime.fromisoformat(toot["created_at"]).date() < since_date:
            continue
        yield dict(content=toot["content"], url=toot["url"])


def get_links(since_date: date, links: list):
    for link in links:
        if datetime.fromisoformat(link["created_at"]).date() < since_date:
            continue

        html_tree = html_soup.fromstring(link["content"])
        title = None

        if card := link.get("card"):
            link_url = card["url"]
            title = card["title"]
        else:
            link_url = html_tree.cssselect("a")[0].get("href")

        if "overcast.fm" in link_url:
            url = get_canonical_overcast_url(link_url)
        else:
            url = link_url

        if title is None:
            title = get_title_from_url(link_url)

        for element in html_tree.cssselect(f'a[href^="{link_url}"]'):
            element.getparent().remove(element)
        for element in html_tree.cssselect('a[href^="https://mastodonczech.cz/tags/"]'):
            element.getparent().remove(element)
        comment = html_tree.text_content().strip()

        yield dict(title=title, comment=comment, url=url)


def get_title_from_webpage(webpage):
    try:
        return TITLES[urlparse(webpage.url).hostname]
    except KeyError:
        return webpage.title


def get_title_from_url(url):
    try:
        response = requests.get(
            url,
            stream=True,
            headers={"User-Agent": "HonzaJavorekBot (+https://honzajavorek.cz)"},
            timeout=5,
        )
        response.raise_for_status()
    except (
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
        requests.exceptions.ReadTimeout,
    ):
        pass
    else:
        for line in response.iter_lines(decode_unicode=True):
            match = re.search(r"<title>([^<]+)", str(line), re.I)
            if match:
                return match.group(1).strip()
    return "(bez titulku)"


def get_canonical_overcast_url(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    for line in response.iter_lines(decode_unicode=True):
        if 'rel="canonical"' in line:
            canonical_url = re.search(r'rel="canonical"\s+href="([^"]+)"', line).group(
                1
            )
            parts = urlparse(canonical_url)
            if parts.query or parts.params or parts.fragment or parts.path != "/":
                return canonical_url
    return url

