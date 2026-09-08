AUTHOR = 'Colin Shevlin'
SITENAME = "Colin's Blog"
SITEURL = "https://colinshevlin.blog"

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 3

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ALL_FEED_RSS = 'feeds/all.rss.xml'
THEME = './themes/example'
STYLESHEET_URL = '/theme/css/main.css'

# Pelican only copies directories listed here verbatim into output/, and the
# default is ['images'] — which is why content/extra/ was silently never
# deployed. Add 'images' back to this list when there are images to serve;
# naming a directory that doesn't exist logs a warning on every build.
STATIC_PATHS = ['extra']

# Files that belong at the site root rather than under their source directory.
# Without these, extra/favicon.ico would land at output/extra/favicon.ico.
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Blogroll
LINKS = (
)

# Social widget
SOCIAL = (
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
