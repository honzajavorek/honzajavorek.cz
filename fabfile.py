# -*- coding: utf-8 -*-


from fabric.api import *
from fabric.colors import red as _red, green as _green
import datetime
import os.path
import re


project_dir = os.path.dirname(os.path.realpath(__file__))

def ok(message):
    puts(_green('[ok]: ') + message)

def error(message):
    abort(_red('[error]: ') + message)


# Auxiliary Fabric tasks

@task
def update_requirements():
    """Updates requirements file."""

    with lcd(project_dir):
        local('pip freeze > requirements.txt')
    ok('Requirements up to date.')


@task
def update_license_year():
    """Checks year range in license and updates it if necessary."""

    license_file = os.path.join(project_dir, 'README.md')

    with open(license_file) as license:
        content = unicode(license.read(), 'utf-8')
    license_until_year = re.search(ur'2007–(\d+)', content).group(1)
    current_year = str(datetime.datetime.now().year)

    if license_until_year != current_year:
        warn('Year in license: %s. Updating to %s.'
            % (license_until_year, current_year))

        with open(license_file, 'w') as license:
            license.write(
                content.replace(
                    u'–' + license_until_year,
                    u'–' + current_year
                ).encode('utf-8')
            )

    ok('License up to date.')


@task
def update_styles():
    """Compiles SCSS files to CSS."""

    with lcd(project_dir):
        #local('sass --style compressed --update %(css_dir)s:%(css_dir)s' % dict(css_dir=))
        #local('rm -rf .sass-cache')
        pass


# Main Fabric tasks

@task
def build():
    """Build the blog."""

    execute(update_requirements)
    execute(update_license_year)
    execute(update_styles)

    with lcd(os.path.join(project_dir, 'src')):
        local('blogofile build')

    ok('See http://localhost:3838')


@task
def deploy():
    """Uploads blog to hosting via FTP."""

    with lcd(project_dir):
        # git-ftp https://github.com/ezyang/git-ftp
        pass


