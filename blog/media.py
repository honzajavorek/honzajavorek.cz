import re
import shutil
from pathlib import Path
from urllib.parse import urlparse
from functools import partial

import click
import requests


MEDIA_RE = re.compile(r'''
(?P<media>
    \!\[
        [^\]]*
    \]
    \(
        (?P<path>
            (?P<static>
                \{static\}
            )?
            \S+
        )
    \)
)
''', re.VERBOSE)


@click.command()
@click.option('--path', 'content_path', default='content', type=click.Path(exists=True, path_type=Path))
@click.option('--images-path', default='content/images', type=click.Path(exists=True, path_type=Path))
@click.option('--overwrite/--no-overwrite', default=False)
def main(content_path, images_path, overwrite):
    for path in content_path.glob('*.md'):
        source_original = path.read_text()
        source_modified = MEDIA_RE.sub(partial(process_match, path, images_path, overwrite=overwrite),
                                       source_original)
        if source_original != source_modified:
            path.write_text(source_modified)


def process_match(source_path, images_path, match, overwrite=False):
    if match.group('static'):
        return match.group('media')

    path = match.group('path')
    click.secho(f'Processing image {path} in {source_path}', bold=True, fg='yellow')

    if path.startswith('http'):
        image_path = images_path / Path(urlparse(path).path).name.lower()
        if not overwrite and image_path.exists():
            raise FileExistsError(str(image_path))
        response = requests.get(path, stream=True)
        response.raise_for_status()
        with image_path.open('wb') as f:
            with click.progressbar(response, label=f'Downloading to {image_path}') as progress:
                for chunk in progress:
                    f.write(chunk)
    else:
        image_path = images_path / Path(path).name.lower()
        if not overwrite and image_path.exists():
            raise FileExistsError(str(image_path))
        click.echo(f'Copying to {image_path}')
        shutil.copy2(source_path.parent / path, image_path)

    assert image_path.exists()
    return match.group('media').replace(path, f'{{static}}/images/{image_path.name}')
