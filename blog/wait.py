from operator import itemgetter
from pathlib import Path
import time
from typing import Any

import click
import requests
from sqlite_utils import Database


@click.command()
@click.option('--db', 'db_path', default='blog.db', type=click.Path(exists=True, path_type=Path))
@click.option('--repo', 'repo', default='honzajavorek/honzajavorek.cz')
@click.option('--deployment-polling-interval', default=29, type=int, help='In seconds')
@click.option('--article-check-attempts', default=10, type=int)
def main(db_path: Path, repo: str, deployment_polling_interval: int, article_check_attempts: int):
    click.echo(f"Waiting for the last deployment to finish")
    response = requests.get(f'https://api.github.com/repos/{repo}/deployments')
    response.raise_for_status()
    deployment = sorted(response.json(), key=itemgetter('updated_at'), reverse=True)[0]
    while True:
        response = requests.get(deployment['statuses_url'])
        response.raise_for_status()
        status = sorted(response.json(), key=itemgetter('updated_at'), reverse=True)[0]
        click.echo(f"Deployment status: {status['state']}")
        if status['state'] in ['success', 'error', 'failure', 'inactive']:
            break
        arbitrary_wait(deployment_polling_interval)

    click.echo(f"Waiting for the latest articles to appear online")
    db = Database(db_path)
    articles = db.query('''
        select * from articles
        where status == "published"
        order by date desc limit 5
    ''')
    for article in articles:
        for _ in range(article_check_attempts):
            click.echo(f"Checking {article['url']}")
            response = requests.head(article['url'])
            if response.status_code == 200:
                break
            arbitrary_wait(deployment_polling_interval)


def arbitrary_wait(seconds=60):
    for i in range(seconds):
        click.echo(f'Waiting {seconds - i}s…', err=True)
        time.sleep(1)
