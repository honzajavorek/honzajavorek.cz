# -*- coding: utf-8 -*-


from fabric.api import *
from fabric.colors import red, green, yellow
from datetime import datetime, timedelta
import unicodedata
import os
import re


# Paths

project_dir = os.path.dirname(os.path.realpath(__file__))
posts_dir = project_dir + '/posts'
output_dir = project_dir + '/output'
deploy_dir = os.path.expanduser('~/.honzajavorek.cz/gh-pages')
css_dir = project_dir + '/theme/static/css'


# Auxiliary functions

def okay(message):
    puts((green(u'✔ ') + message).encode('utf8'))


def error(message):
    cross = red(u'✖')
    abort((cross + ' ' + message + ' ' + cross).encode('utf8'))


def warning(message):
    star = yellow(u'★')
    warn((star + ' ' + message + ' ' + star).encode('utf8'))


def slugify(string, underscore=False):
    if not isinstance(string, unicode):
        string = unicode(string)
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore')
    string = unicode(re.sub(r'[^\w\s-]', '', string).strip().lower())

    re_dash = re.compile(r'[-_\s]+' if underscore else r'[-\s]+')
    return re_dash.sub('-', string)


# Auxiliary Fabric tasks

@task
def update_license_year():
    """Checks year range in license and updates it if necessary."""
    pass
    license_file = os.path.join(project_dir, 'README.md')

    with open(license_file) as license:
        content = unicode(license.read(), 'utf8')
    license_until_year = re.search(ur'2007–(\d+)', content).group(1)
    current_year = str(datetime.now().year)

    if license_until_year != current_year:
        warning('Year in license: {0}. Updating to {1}.'.format(
            license_until_year,
            current_year))

        with open(license_file, 'w') as license:
            license.write(
                content.replace(
                    u'–' + license_until_year,
                    u'–' + current_year
                ).encode('utf8')
            )

    okay('License up to date.')


@task
def update_styles():
    """Compiles SCSS files to CSS."""
    with lcd(css_dir):
        local('rm -rf *.css')
        local('sass --style compressed --update .:.')
        local('rm -rf .sass-cache')
    okay('SCSS compiled.')


# Main Fabric tasks

@task
def build():
    """Build the blog."""
    execute(update_license_year)
    execute(update_styles)

    with lcd(project_dir):
        local('pelican -s settings.py')
    okay('See http://localhost/blog/output.')


@task
def deploy():
    """Uploads blog to hosting."""
    execute(build)

    if os.path.exists(deploy_dir):
        local('git pull origin gh-pages')
        contents = [f for f in os.listdir(deploy_dir) if f != '.git']
        with settings(hide('warnings'), warn_only=True):
            for filename in contents:
                local('rm -rf ' + os.path.join(deploy_dir, filename))
    else:
        os.makedirs(deploy_dir)
        local('git clone -b gh-pages '
              'git@github.com:honzajavorek/honzajavorek.cz.git ' + deploy_dir)

    with lcd(deploy_dir):
        okay('Synchronized blog repository.')
        local('cp -r {0}/* .'.format(output_dir))

        # remove unnecessary stuff
        local('rm -rf author category tag feeds')
        local('rm -rf theme/css/code.css theme/css/*.scss')

        local('git add -A')
        with settings(hide('warnings'), warn_only=True):
            local('git commit -m "deploying changes in pages"')
        local('git push origin gh-pages')

    okay('All deployed.')


@task
def publish():
    """Saves changes in articles."""
    with lcd(posts_dir):
        local('git add -A')
        with settings(hide('warnings'), warn_only=True):
            local('git commit -m "publishing new articles"')
        local('git push origin master')
    okay('All published.')
    execute(deploy)


@task
def new(title=None):
    """Creates new article template"""
    if not title:
        error('Missing title, usage: fab new:"Article title".')
    else:
        title = title.decode('utf8')

    slug = slugify(title)
    pubdate = datetime.now() + timedelta(hours=2)

    filename = '{0} {1}.md'.format(pubdate.strftime('%Y-%m-%d'), slug)
    contents = 'Title: {0}\nDate: {1}\n\n'.format(
        title,
        pubdate.strftime('%Y-%m-%d %H:%M:%S'))

    path = os.path.join(posts_dir, filename)
    with open(path, 'w') as f:
        f.write(contents.encode('utf8'))
        okay('{0} prepared.'.format(filename))
