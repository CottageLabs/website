import datetime

AUTHOR = 'us@cottagelabs.com'
SITENAME = 'Cottage Labs'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'GB'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
DEFAULT_DATE = 'fs'

THEME = 'themes/simple'
THEME_STATIC_PATHS = ['static']

STATIC_DIR = 'content/images'

INDEX_SAVE_AS = 'index.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
CSS_FILE = "scss/main.css"

USE_FOLDER_AS_CATEGORY = True

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_TEMPLATE = 'page'

ARTICLE_PATHS = ['projects']
ARTICLE_URL = 'projects/{slug}/'
ARTICLE_SAVE_AS = 'projects/{slug}/index.html'
ARTICLE_TEMPLATE = 'project'

TAGS_SAVE_AS = 'projects/index.html'
TAG_SAVE_AS = 'projects/{slug}/index.html'
TAG_URL = 'projects/{slug}'

PLUGINS = [
    'yaml_metadata',
    'css_cache_bust'
]

JINJA_CONTEXTS = {
    'now': datetime.datetime.now(datetime.UTC),
}

NOW = datetime.datetime.now()
