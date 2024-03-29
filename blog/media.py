import re
import shutil
from pathlib import Path
from urllib.parse import urlparse, unquote
from functools import partial

import click
from slugify import slugify
import requests
from send2trash import send2trash
from PIL import Image
from pillow_heif import register_heif_opener


IMG_MAX_PX = 1024

IMG_MAX_MB = 1

SKIP_FILES = ['.DS_Store']

SKIP_RESIZE_SUFFIXES = ['.gif', '.svg']

MEDIA_RES = [
    re.compile(r'''
        (?P<media>
            \!\[
                [^\]]*
            \]
            \(
                (?P<path>
                    (?P<static>
                        \{static\}
                    )?
                    [^\s\]\{]+
                )
            \)
        )
    ''', re.VERBOSE | re.IGNORECASE),
    re.compile(r'''
        (?P<media>
            \!\[
                [^\]]*
            \]
            \(
                (?P<path>
                    \<
                    [^\>]+
                    \>
                )
            \)
        )
    ''', re.VERBOSE | re.IGNORECASE),
    re.compile(r'''
        (?P<media>
            <img
                (\s[^>]*)?
                \ssrc=
                    ["\']
                        (?P<path>
                            (?P<static>
                                \{static\}
                            )?
                            [^>]+
                        )
                    ["\']
            >
        )
    ''', re.VERBOSE | re.IGNORECASE)
]

IMAGE_METADATA_RE = re.compile(r'Image: images/(?P<path>\S+)')


register_heif_opener()


@click.command()
@click.option('--path', 'content_path', default='content', type=click.Path(exists=True, path_type=Path))
@click.option('--images-path', default='content/images', type=click.Path(exists=True, path_type=Path))
@click.option('--overwrite/--no-overwrite', default=False)
@click.option('--detect-unused/--no-detect-unused', default=True)
@click.option('--resize/--no-resize', default=True)
def main(content_path, images_path, overwrite, detect_unused, resize):
    images = set()

    for path in content_path.glob('*.md'):
        source = path.read_text()

        # record images linked from metadata
        for match in IMAGE_METADATA_RE.finditer(source):
            images.add(images_path / match.group('path'))

        # find all linked images, copy them to the blog source
        source_modified = source
        for media_re in MEDIA_RES:
            replace = partial(process_match, path, images_path, images, overwrite=overwrite)
            source_modified = media_re.sub(replace, source_modified)
        if source != source_modified:
            path.write_text(source_modified)
            source = source_modified

    # detect unused images
    if detect_unused:
        image_paths = set(image_path for image_path in images_path.glob('*.*')
                          if image_path.name not in SKIP_FILES)
        for unused_image_path in (image_paths - images):
            click.secho(f'Unused: {unused_image_path}', fg='red')
            if click.confirm('Delete?', default=True, prompt_suffix=''):
                send2trash(unused_image_path)

    # resize images
    if resize:
        image_paths = (image_path for image_path in images_path.glob('*.*')
                       if (image_path.suffix.lower() not in SKIP_RESIZE_SUFFIXES
                           and image_path.name not in SKIP_FILES))
        for image_path in image_paths:
            with Image.open(image_path) as img:
                width, height = img.size
                if width > IMG_MAX_PX or height > IMG_MAX_PX:
                    click.secho(f'Too large: {image_path} ({width}x{height}px, max {IMG_MAX_PX}px)', fg='red', err=True)
                    img.thumbnail((IMG_MAX_PX, IMG_MAX_PX), Image.Resampling.LANCZOS)
                    img.save(image_path, img.format)

            size_mb = image_path.stat().st_size / 1024 / 1024
            if size_mb > IMG_MAX_MB:
                click.secho(f'Too large: {image_path} ({size_mb}mb, max size: {IMG_MAX_MB}mb)', fg='red', err=True)
                raise click.Abort()


def process_match(source_path, images_path, images, match, overwrite=False):
    groups = match.groupdict()

    if groups.get('static'):
        image_path = Path(groups['path'].replace(f'{{static}}/{images_path.name}', str(images_path)))
        assert image_path.exists()
        images.add(image_path)
        return groups['media']

    path = groups['path']
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
        unquoted_path = Path(unquote(path.removeprefix('<').removesuffix('>')))
        image_path = images_path / (slugify(unquoted_path.stem) + unquoted_path.suffix.lower())
        if not overwrite and image_path.exists():
            raise FileExistsError(str(image_path))
        click.echo(f'Copying to {image_path}')
        shutil.copy2(source_path.parent / unquoted_path, image_path)

    assert image_path.exists()

    if image_path.suffix in ['.heic', '.webp']:
        click.secho(f'Converting {image_path}', bold=True, fg='yellow')
        converted_image_path = image_path.with_suffix('.jpg')
        with Image.open(image_path) as img:
            img.save(converted_image_path, 'JPEG')
        image_path.unlink()
        image_path = converted_image_path

    images.add(image_path)
    return groups['media'].replace(path, f'{{static}}/images/{image_path.name}')
