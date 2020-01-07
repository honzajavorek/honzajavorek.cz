from datetime import datetime


# Author
AUTHOR = 'Honza Javorek'
TWITTER_USERNAME = 'honzajavorek'

# Site
SITENAME = AUTHOR

# Custom data
BLOGNAME = "HJ's Blog"
OUTDATED_ARTICLE_YEARS = 3
NOW = datetime.now()
DREDD_STARS_RAISE = round(3200 / 650)  # stars after / stars before
COPYRIGHT = f'© Copyright 2007—{NOW.year}'

# Timezone, language
TIMEZONE = 'Europe/Prague'
LOCALE = 'en_US.UTF-8'  # influences the %b below
DEFAULT_LANG = 'en'
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
PATH = 'content'
DEFAULT_PAGINATION = False
DEFAULT_CATEGORY = 'blog'
MARKDOWN = {
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
ARTICLE_URL = 'blog/{slug}'
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
IGNORE_FILES = ['.#*', '.DS_Store', 'drafts']
DELETE_OUTPUT_DIRECTORY = False
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True

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
    '../node_modules',
    './static',
]

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'home_appearances',
    'home_feeds',
    'home_projects',
    'custom_translation_id',
    'custom_feed_meta',
    'code_blocks',
    'alternates',
    'comments',
    'tables',
    'headings',
    'media',
]
IMG_MAX_PX = 1024
IMG_MAX_MB = 1
CUSTOM_FEED_META = {
    'title': BLOGNAME,
    'link': f'{SITEURL}/{ARCHIVES_URL}',
    'description': "Honza Javorek's Blog",
    'author_email': 'mail@honzajavorek.cz',
    'author_name': AUTHOR,
    'author_link': SITEURL,
    'feed_copyright': f'{COPYRIGHT} {AUTHOR} <{SITEURL}>',
}
