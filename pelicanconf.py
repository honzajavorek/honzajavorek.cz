from datetime import datetime


# Author
AUTHOR = 'Honza Javorek'

# Site
SITENAME = AUTHOR

# Custom data
BLOGNAME = 'Javorové lístky'
OUTDATED_ARTICLE_YEARS = 3
NOW = datetime.now()
BLOG_FOUNDED_YEAR = 2007
JG_FOUNDED_YEAR = 2019
PYVO_FOUNDED_YEAR = 2011
COPYRIGHT = f'© Copyright {BLOG_FOUNDED_YEAR}—{NOW.year}'
WEEKNOTES_TAG = 'týdenní poznámky'
HIGHLIGHT_TAG = 'highlight'

# Timezone, language
TIMEZONE = 'Europe/Prague'
LOCALE = 'en_US.UTF-8'  # influences the %b below
DEFAULT_LANG = 'cs'
DEFAULT_DATE_FORMAT = '%b\u00A0%-d,\u00A0%Y'
DATE_FORMATS = {'cs': '%-d.\u00A0%-m.\u00A0%Y'}

# Feeds
FEED_ALL_ATOM = 'feed.xml'
FEED_MAX_ITEMS = 50
FEED_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blog
DEFAULT_PAGINATION = False
DEFAULT_CATEGORY = 'blog'
MARKDOWN = {
    'extensions': [
        'markdown_del_ins',
    ],
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'guess_lang': False,
        },
        'markdown.extensions.toc': {},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

# URL and save paths
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = False
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARCHIVES_URL = 'blog/'
ARCHIVES_SAVE_AS = 'blog/index.html'
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Translations
ARTICLE_LANG_URL = 'blog/{slug}/'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_TRANSLATION_ID = 'translation-id'  # comes from custom plugin

# Turning off unused blog features
PAGE_SAVE_AS = ''
PAGE_LANG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
DIRECT_TEMPLATES = ['index', 'archives']

# Generating
OUTPUT_PATH = 'public/'
IGNORE_FILES = [
    '.#*',
    '.DS_Store',
    'drafts',
]
DELETE_OUTPUT_DIRECTORY = False

# Extra static files
STATIC_PATHS = [
    'images',
    'files',
]
EXTRA_PATH_METADATA = {
    'images/extra/favicon.ico': {'path': 'favicon.ico'},
}

# Theme
THEME = './theme'
THEME_STATIC_PATHS = [
    'node_modules',
    'static',
]

# Plugins
PLUGIN_PATHS = ['honzajavorekcz/plugins']
PLUGINS = [
    'appearances',
    'custom_translation_id',
    'custom_feed_meta',
    'code_blocks',
    'alternates',
    'comments',
    'tables',
    'headings',
    'media',
    'readtime',
    'seealso',
]
IMG_MAX_PX = 1024
IMG_MAX_MB = 1
CUSTOM_FEED_META = {
    'title': BLOGNAME,
    'link': f'{SITEURL}/{ARCHIVES_URL}',
    'description': 'Blog Honzy Javorka',
    'author_email': 'mail@honzajavorek.cz',
    'author_name': AUTHOR,
    'author_link': SITEURL,
    'feed_copyright': f'{COPYRIGHT} {AUTHOR} <{SITEURL}>',
}
