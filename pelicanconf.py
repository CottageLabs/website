AUTHOR = 'Aga'
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

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
CSS_FILE = "main.css"

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_TEMPLATE = 'page'

ARTICLE_PATHS = ['articles']
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_TEMPLATE = 'article'

PLUGINS = [
    'pelican_fontawesome'
]
