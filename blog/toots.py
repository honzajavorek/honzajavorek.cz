import json
from operator import itemgetter
from pathlib import Path

import click
from mastodon import Mastodon


@click.command()
@click.argument('client_id', envvar='MASTODON_CLIENT_ID')
@click.argument('client_secret', envvar='MASTODON_CLIENT_SECRET')
@click.argument('access_token', envvar='MASTODON_ACCESS_TOKEN')
@click.option('--server-url', default='https://mastodonczech.cz')
@click.option('--path', default='content/data', type=click.Path(path_type=Path))
@click.option('--limit', default=100, type=int)
def main(client_id: str, client_secret: str, access_token: str, server_url: str, path: Path, limit: int):
    click.echo('Connecting to Mastodon')
    mastodon = Mastodon(api_base_url=server_url,
                        client_id=client_id,
                        client_secret=client_secret,
                        access_token=access_token)
    account_id = mastodon.me()['id']

    click.echo("Synchronizing links")
    path_links = path / 'toots-links.json'
    try:
        toots = json.loads(path_links.read_text())
    except FileNotFoundError:
        toot_index = {}
    else:
        toot_index = {toot['id']: toot for toot in toots}
    for toot in mastodon.account_statuses(account_id, limit=limit, tagged='links', exclude_replies=True, exclude_reblogs=True):
        toot_index[toot['id']] = marshall_toot(toot)
    toots = sorted(toot_index.values(), key=itemgetter('created_at'), reverse=True)
    contents = json.dumps(toots, indent=2, ensure_ascii=False)
    path_links.write_text(contents)

    click.echo("Synchronizing junior.guru toots")
    path_jg = path / 'toots-jg.json'
    try:
        toots = json.loads(path_jg.read_text())
    except FileNotFoundError:
        toot_index = {}
    else:
        toot_index = {toot['id']: toot for toot in toots}
    for toot in mastodon.account_statuses(account_id, limit=limit, tagged='juniorguru', exclude_replies=True, exclude_reblogs=True):
        toot_index[toot['id']] = marshall_toot(toot)
    toots = sorted(toot_index.values(), key=itemgetter('created_at'), reverse=True)
    contents = json.dumps(toots, indent=2, ensure_ascii=False)
    path_jg.write_text(contents)

    click.echo("Synchronizing replies")
    path_replies = path / 'toots-replies.json'
    try:
        articles = json.loads(path_replies.read_text())
    except FileNotFoundError:
        article_index = {}
    else:
        article_index = {article['url']: article for article in articles}
    for toot in mastodon.account_statuses(account_id, limit=limit, tagged='blog', exclude_replies=True, exclude_reblogs=True):
        if toot["card"]:
            article_url = toot["card"]["url"]
            replies = article_index.get(article_url, {"replies": []})["replies"]
            reply_index = {reply["id"]: reply for reply in replies}
            context = mastodon.status_context(toot["id"])
            if descendants := context["descendants"]:
                for reply in descendants:
                    reply_index[reply["id"]] = marshall_reply(reply)
            article = dict(
                url=article_url,
                slug=parse_slug(article_url),
                created_at=toot["created_at"].isoformat(),
                toot_url=toot["url"],
                favourites_count=toot["favourites_count"],
                reblogs_count=toot["reblogs_count"],
                replies=sorted(reply_index.values(), key=itemgetter("created_at")),
            )
            article_index[article_url] = article
    articles = sorted(article_index.values(), key=itemgetter('created_at'), reverse=True)
    contents = json.dumps(articles, indent=2, ensure_ascii=False)
    path_replies.write_text(contents)


def marshall_toot(data: dict) -> dict:
    toot = {}
    for key, value in clear_empty_keys(data).items():
        if key in ['application', 'account']:
            continue
        if key == "card" and "authors" in value:
            continue
        if key in ('created_at', 'edited_at'):
            value = value.isoformat()
        if key == 'card' and 'published_at' in value:
            value['published_at'] = value['published_at'].isoformat()
        if key == 'poll' and 'expires_at' in value:
            value['expires_at'] = value['expires_at'].isoformat()
        toot[key] = value
    return toot


def marshall_reply(data: dict) -> dict:
    reply = {}
    for key, value in clear_empty_keys(data).items():
        if key == 'card':
            continue
        if key in ('created_at', "edited_at"):
            value = value.isoformat()
        if key == 'account':
            value = {
                k: v for k, v in value.items()
                if k in (
                    'id',
                    'username',
                    'acct',
                    'display_name',
                    'url',
                    'uri',
                    'avatar',
                    'avatar_static',
                )
            }
        reply[key] = value
    return reply


def clear_empty_keys(data: dict) -> dict:
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            value = clear_empty_keys(value)
        elif isinstance(value, list):
            value = [clear_empty_keys(item) for item in value]
        if value or value is False:
            result[key] = value
    return result


def parse_slug(url: str) -> str:
    url = url.rstrip('/')
    prefix = 'https://honzajavorek.cz/blog/'
    if url.startswith(prefix) and url != prefix:
        return url[len(prefix):]
    raise ValueError(f'Invalid URL: {url}')
