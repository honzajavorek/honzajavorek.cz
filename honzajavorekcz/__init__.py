import json
import shlex
import subprocess
from pathlib import Path

import click
import pytest
from strava_offline.cli import cli as strava

from honzajavorekcz.telegram import main as telegram
from honzajavorekcz.weeknotes import main as weeknotes


@click.group()
def main():
    pass


main.add_command(telegram, 'telegram')
main.add_command(weeknotes, 'weeknotes')
main.add_command(strava, 'strava')


@main.command()
@click.option('--path', 'content_path', default='content', type=click.Path(exists=True))
@click.option('--debug/--no-debug', default=True)
def build(content_path, debug):
    extra_args = []

    if debug:
        extra_args.append('--debug')

    args = ['pelican', content_path, '--settings=publishconf.py', '--fatal=warnings']
    args += extra_args
    click.secho(shlex.join(args), fg='green', bold=True)
    click.echo('')
    subprocess.run(args)


@main.command()
@click.option('--path', 'content_path', default='content', type=click.Path(exists=True))
@click.option('--articles', 'articles_count', default=1, type=int)
@click.option('--debug/--no-debug', default=False)
def dev(content_path, articles_count, debug):
    extra_args = []

    paths = sorted(Path(content_path).glob('*.md'), reverse=True)
    if len(paths) > articles_count:
        paths_json = json.dumps([str(article.relative_to(content_path))
                                 for article in paths[:articles_count]])
        extra_args.extend(['-e', f'ARTICLE_PATHS={paths_json}'])

    if debug:
        extra_args.append('--debug')

    args = ['pelican', content_path, '--fatal=errors',
            '--listen', '--bind=localhost', '--autoreload', '--ignore-cache']
    args += extra_args
    click.secho(shlex.join(args), fg='green', bold=True)
    click.echo('')
    subprocess.run(args)


@main.command(context_settings={'ignore_unknown_options': True})
@click.argument('pytest_args', nargs=-1, type=click.UNPROCESSED)
def test(pytest_args):
    code = pytest.main(list(pytest_args))
    if code:
        raise click.Abort()
