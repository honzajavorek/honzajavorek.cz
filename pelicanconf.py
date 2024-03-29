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
TAG_FEED_ATOM = 'tag/{slug}.xml'
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
        'def_list',
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
DRAFT_URL = ARTICLE_URL
DRAFT_SAVE_AS = ARTICLE_SAVE_AS
ARCHIVES_URL = 'blog/'
ARCHIVES_SAVE_AS = 'blog/index.html'
FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Translations
ARTICLE_LANG_URL = 'blog/{slug}/'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}/index.html'
DRAFT_LANG_URL = ARTICLE_LANG_URL
DRAFT_LANG_SAVE_AS = ARTICLE_LANG_SAVE_AS
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
]
DELETE_OUTPUT_DIRECTORY = False

# Extra static files
STATIC_PATHS = [
    'images',
    'files',
]
EXTRA_PATH_METADATA = {
    'images/theme/favicon.ico': {'path': 'favicon.ico'},
    'images/theme/favicon.svg': {'path': 'favicon.svg'},
    'images/theme/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'images/theme/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'images/theme/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'images/theme/site.webmanifest': {'path': 'site.webmanifest'},
}

# Theme
THEME = './theme'
THEME_STATIC_PATHS = [
    'node_modules',
    'static',
]

# Plugins
PLUGIN_PATHS = ['blog/plugins']
PLUGINS = [
    'alternates',
    'appearances',
    'code_blocks',
    'comments',
    'custom_feed_meta',
    'custom_translation_id',
    'database',
    'headings',
    'media',
    'readtime',
    'replies',
    'seealso',
    'tables',
]
CUSTOM_FEED_META = lambda settings: {
    'title': settings['BLOGNAME'],
    'link': f"{settings['SITEURL']}/{settings['ARCHIVES_URL']}",
    'description': 'Blog Honzy Javorka',
    'author_email': 'mail@honzajavorek.cz',
    'author_name': settings['AUTHOR'],
    'author_link': settings['SITEURL'],
    'feed_copyright': f"{settings['COPYRIGHT']} {settings['AUTHOR']} <{settings['SITEURL']}>",
}
DB_PATH = 'blog.db'
