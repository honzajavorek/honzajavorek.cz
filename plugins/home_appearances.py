from pathlib import Path
from operator import itemgetter

from pelican import signals
import strictyaml as yaml


SCHEMA = yaml.Seq(
    yaml.Map({
        'date': yaml.Datetime(),
        'title': yaml.Str(),
        'event': yaml.Str(),
        yaml.Optional('lang', default='cs'): yaml.Enum([
            'cs',
            'en',
        ]),
        yaml.Optional('type', default='talk'): yaml.Enum([
            'talk',
            'workshop',
            'interview',
        ]),
        yaml.Optional('url'): yaml.Url(),
        yaml.Optional('resources_type', default='slides'): yaml.Enum([
            'slides',
            'text',
        ]),
        yaml.Optional('resources_url'): yaml.Url(),
    }),
)


def register():
    signals.initialized.connect(load_appearances)


def load_appearances(pelican):
    path = Path('./content/data/appearances.yml')
    appearances = yaml.load(path.read_text(), SCHEMA).data
    appearances = sorted(appearances, key=itemgetter('date'), reverse=True)
    pelican.settings['appearances'] = appearances
