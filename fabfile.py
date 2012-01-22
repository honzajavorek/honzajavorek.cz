# -*- coding: utf-8 -*-


from fabric.api import *
from fabric.colors import red, green, yellow
from datetime import datetime
import unicodedata
import os.path
from glob import glob
import re


# Paths

project_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(project_dir, 'src')
posts_dir = os.path.join(src_dir, '_posts')
output_dir = os.path.join(src_dir, '_site')
css_dir = os.path.join(src_dir, 'css')


# Auxiliary functions

def okay(message):
    puts((green(u'✔ ') + message).encode('utf-8'))

def error(message):
    cross = red(u'✖')
    abort((cross + ' ' + message + ' ' + cross).encode('utf-8'))

def warning(message):
    star = yellow(u'★')
    warn((star + ' ' + message + ' ' + star).encode('utf-8'))

def slugify(string, underscore=False):
    if not isinstance(string, unicode):
        string = unicode(string)
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore')
    string = unicode(re.sub(r'[^\w\s-]', '', string).strip().lower())

    re_dash = re.compile(r'[-_\s]+' if underscore else r'[-\s]+')
    return re_dash.sub('-', string)


# Auxiliary Fabric tasks

@task
def update_requirements():
    """Updates requirements file."""

    with lcd(project_dir):
        local('pip freeze > requirements.txt')
    okay('Requirements up to date.')


@task
def update_license_year():
    """Checks year range in license and updates it if necessary."""

    license_file = os.path.join(project_dir, 'README.markdown')

    with open(license_file) as license:
        content = unicode(license.read(), 'utf-8')
    license_until_year = re.search(ur'2007–(\d+)', content).group(1)
    current_year = str(datetime.now().year)

    if license_until_year != current_year:
        warning('Year in license: %s. Updating to %s.'
            % (license_until_year, current_year))

        with open(license_file, 'w') as license:
            license.write(
                content.replace(
                    u'–' + license_until_year,
                    u'–' + current_year
                ).encode('utf-8')
            )

    okay('License up to date.')


@task
def update_styles():
    """Compiles SCSS files to CSS."""

    with lcd(css_dir):
        local('sass --style compressed --update .:.')
        local('rm -rf .sass-cache')
    okay('SCSS compiled.')


# Main Fabric tasks

@task
def build():
    """Build the blog."""

    execute(update_requirements)
    execute(update_license_year)
    execute(update_styles)

    with lcd(src_dir):
        local('blogofile build')

    okay('See http://localhost:3838')


@task
def deploy():
    """Uploads blog to hosting via FTP."""

    execute(build)

    ftpsync = os.path.join(project_dir, 'ftpsync.py')
    password_file = os.path.join(project_dir, '.ftp_password')

    with open(password_file) as f:
        password = f.read()

    okay('Connecting to FTP and uploading...')
    local('python %(ftpsync)s ftp://javorek.net:%(pwd)s@www.javorek.net/test %(dir)s --upload'
        % dict(ftpsync=ftpsync, dir=output_dir, pwd=password))
    okay('All uploaded.')


@task
def write(title=None):
    """Prepares a new article."""

    if not title:
        title = prompt('Title: ')
    if not isinstance(title, unicode):
        title = unicode(title, 'utf-8')

    now = datetime.now()

    original_slug = slugify(title, True)
    slug = original_slug[:]
    slug_attempt = 1
    while glob('%s/*%s.markdown' % (posts_dir, slug)):
        warning('Article with slug %s already exists.' % slug)
        slug = '%s-%d' % (original_slug, slug_attempt)
        slug_attempt += 1

    data = {
        'title': title,
        'year': now.year,
        'month': format(now.month, '02d'),
        'day': format(now.day, '02d'),
        'hour': format(now.hour + 2, '02d'),
        'minute': format(now.minute, '02d'),
        'second': format(now.second, '02d'),
        'slug': slug,
    }

    template = """---
title: %(title)s
date: %(year)s/%(month)s/%(day)s %(hour)s:%(minute)s:%(second)s
tags:
draft: true
---


"""

    filename = os.path.join(
        posts_dir,
        ('%(year)s-%(month)s-%(day)s ' % data) + slug + '.markdown'
    )

    with open(filename, 'w') as f:
        f.write((template % data).encode('utf-8'))

    okay("Article prepared as '%s'." % os.path.basename(filename))
    local('sublime-text-2 "%s"' % filename)


@task
def publish():
    with lcd(posts_dir):
        local('git add -A')
        local('git commit -m "publishing new articles"')
        local('git push origin master')
    okay("All published.")

    execute(deploy)