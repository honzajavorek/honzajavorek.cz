import time
import re
import json
import shlex
import subprocess
import multiprocessing
from pathlib import Path
import importlib

import click
import pytest
from strava_offline.cli import cli as strava

from blog.telegram import main as telegram
from blog.weeknotes import main as weeknotes
from blog.media import main as media
from blog.kocarkino import main as kocarkino


@click.group()
def main():
    pass


main.add_command(telegram, 'telegram')
main.add_command(weeknotes, 'weeknotes')
main.add_command(media, 'media')
main.add_command(strava, 'strava')
main.add_command(kocarkino, 'kocarkino')


@main.command()
@click.option('--path', 'content_path', default='content', type=click.Path(exists=True))
@click.option('--settings-module', default='publishconf', type=importlib.import_module)
@click.option('--debug/--no-debug', default=True)
def build(content_path, settings_module, debug):
    extra_args = []

    if debug:
        extra_args.append('--debug')

    args = ['pelican', content_path, f'--settings={settings_module.__file__}', '--fatal=warnings']
    args += extra_args
    click.secho(shlex.join(args), fg='green', bold=True)
    click.echo('')
    subprocess.run(args, check=True)


@main.command()
@click.option('--path', 'content_path', default='content', type=click.Path(exists=True))
@click.option('--articles', 'articles_count', default=1, type=int)
@click.option('--settings-module', default='pelicanconf', type=importlib.import_module)
@click.option('--wait', 'wait_sec', default=10, type=int)
@click.option('--open/--no-open', 'open_browser', default=True)
@click.option('--cache/--no-cache', default=True)
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def dev(context, content_path, articles_count, settings_module,
        wait_sec, open_browser, cache, debug):
    context.invoke(media)

    extra_args = []

    if debug:
        extra_args.append('--debug')
    if not cache:
        extra_args.append('--ignore-cache')

    paths = sorted(Path(content_path).glob('*.md'), reverse=True)
    if len(paths) > articles_count:
        paths_json = json.dumps([str(article.relative_to(content_path))
                                 for article in paths[:articles_count]])
        extra_args.extend(['-e', f'ARTICLE_PATHS={paths_json}'])

    proc = None
    if open_browser:
        path = paths[0]
        slug = re.search(settings_module.FILENAME_METADATA, path.stem).group('slug')
        output_path = settings_module.ARTICLE_URL.format(slug=slug)
        proc = multiprocessing.Process(target=dev_open,
                                       args=(output_path, wait_sec))
        proc.start()

    args = ['pelican', content_path, '--fatal=errors',
            '--listen', '--autoreload', '--bind=localhost']
    args += extra_args
    click.secho(shlex.join(args), fg='green', bold=True)
    click.echo('')
    try:
        subprocess.run(args, check=True)
    finally:
        if proc:
            proc.join()


def dev_open(path, wait_sec):
    time.sleep(wait_sec)
    click.launch(f"http://localhost:8000/{path}")


@main.command(context_settings={'ignore_unknown_options': True})
@click.argument('pytest_args', nargs=-1, type=click.UNPROCESSED)
def test(pytest_args):
    code = pytest.main(list(pytest_args))
    if code:
        raise click.Abort()
