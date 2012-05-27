# -*- coding: utf-8 -*-


from fabric.api import *
from fabric.colors import red, green, yellow
from datetime import datetime
from glob import glob
import unicodedata
import os
import re


# Paths

project_dir = os.path.dirname(os.path.realpath(__file__))
posts_dir = project_dir + '/posts'
output_dir = project_dir + '/output'
deploy_dir = '/tmp/blog-deploy'
css_dir = project_dir + '/theme/static/css'


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
def update_license_year():
    """Checks year range in license and updates it if necessary."""
    pass
#     license_file = os.path.join(project_dir, 'README.markdown')

#     with open(license_file) as license:
#         content = unicode(license.read(), 'utf-8')
#     license_until_year = re.search(ur'2007–(\d+)', content).group(1)
#     current_year = str(datetime.now().year)

#     if license_until_year != current_year:
#         warning('Year in license: %s. Updating to %s.'
#             % (license_until_year, current_year))

#         with open(license_file, 'w') as license:
#             license.write(
#                 content.replace(
#                     u'–' + license_until_year,
#                     u'–' + current_year
#                 ).encode('utf-8')
#             )

#     okay('License up to date.')


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
    execute(update_license_year)
    execute(update_styles)

    with lcd(project_dir):
        local('pelican -s settings.py')
    okay('See http://localhost/blog/output.')


@task
def deploy():
    """Uploads blog to hosting."""
    execute(build)

    local('rm -rf ' + deploy_dir)
    local('mkdir ' + deploy_dir)
    local('git clone git@github.com:honzajavorek/blog.git ' + deploy_dir)

    with lcd(deploy_dir):
        okay('Cloned blog repository.')
        local('git checkout gh-pages')
        okay('GitHub Pages branch.')
        local('cp -r %s/* .' % output_dir)

        # remove unnecessary stuff
        local('rm -rf author category tag feeds')
        local('rm -rf theme/css/code.css theme/css/*.scss')

        local('git add -A')
        with settings(hide('warnings'), warn_only=True):
            local('git commit -m "deploying changes in pages"')
        local('git push origin gh-pages')

    local('rm -rf ' + deploy_dir)
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
