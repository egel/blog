#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR          = 'Maciej Sypień'
SITENAME        = "The Egel's Blog"
SITE_SLOGAN     = "Do more in less time"
SITE_SUBSLOGAN  = "Simplicity and clarity of the implementation"
SITEURL         = 'http://pelican-egel-blog.local'
TIMEZONE        = 'Europe/Warsaw'
DEFAULT_LANG    = 'en'

PATH            = 'content'
OUTPUT_PATH     = 'output/'


STATIC_PATHS        = ['extras', 'images', 'downloads']
ARTICLE_PATHS       = ['blog']
PAGE_PATHS          = ['pages']
ARCHIVES_URL        = "archives.html"
FAVICON             = "extras/favicon.png"

# Formatting for URLs
# ARTICLE_URL             = '{date:%Y}/{slug}.html'
# ARTICLE_SAVE_AS         = '{date:%Y}/{slug}.html'
# ARTICLE_LANG_SAVE_AS    = '{date:%Y}/{slug}-{lang}.html'

# DRAFT_URL           = 'drafts/{slug}.html'
# DRAFT_SAVE_AS       = 'drafts/{slug}.html'
# DRAFT_LANG_URL      = 'drafts/{slug}-{lang}.html'
# DRAFT_LANG_SAVE_AS  = 'drafts/{slug}-{lang}.html'

# PAGE_URL            = 'pages/{slug}/'
# PAGE_SAVE_AS        = 'pages/{slug}.html'
# PAGE_LANG_URL       = 'pages/{slug}-{lang}.html'
# PAGE_LANG_SAVE_AS   = 'pages/{slug}-{lang}.html'

# CATEGORY_URL        = 'category/{slug}.html'
# CATEGORY_SAVE_AS    = 'category/{slug}.html'

# TAG_URL             = 'tag/{slug}.html'
# TAG_SAVE_AS         = 'tag/{slug}.html'

# AUTHOR_URL          = 'author/{slug}.html'
# AUTHOR_SAVE_AS      = 'author/{slug}.html'

# YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
# MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'




DEFAULT_METADATA = {'status': 'draft',}
DEFAULT_DATE_FORMAT = '%b %-d, %Y'

# Top nav
DISPLAY_SEARCH_IN_TOP_NAV = True


# Sidebar
DISPLAY_SIDEBAR = False

DISPLAY_ABOUT_ME_ON_SIDEBAR = False
ABOUT_ME = """
Hey!
"""

HIDE_SOCIAL = False
SOCIAL = (('Twitter', 'https://twitter.com/MaciejSypien'),
          ('Github', 'https://github.com/egel'),
          ('LinkedIn', 'https://www.linkedin.com/in/maciejsypien'),)

FEEDS =  (('All posts', 'feeds/all.atom.xml'),
          ('Category', 'feeds/category'),
          ('OPW', 'feeds/tag/opw.atom.xml'),)

# Side bar
DISPLAY_SEARCH_ON_SIDEBAR = False
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True

DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
ADDTHIS_PROFILE = True

# TODO:
DISPLAY_FORK_ME_ON_GITHUB = True
GITHUB_REPO_URL = "sgasdfasdfasdfasdf"

# TODO:
DISPLAY_GITHUB_REPOS_ON_SIDEBAR = False
GITHUB_SHOW_USER_LINK = True
GITHUB_USER = "egel"

# TODO:
DISPLAY_TWITTER_TIMELINE_ON_SIDEBAR = False
TWITTER_USERNAME = "MaciejSypien"
TWITTER_WIDGET_ID = "648150917355843584"


DISPLAY_LINKS_ON_SIDEBAR = False
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Articles
SHOW_DATE_MODIFIED = True
SHOW_ARTICLE_CATEGORY = True
SHOW_ARTICLE_AUTHOR = False
RELATED_POSTS_TEXT = "Few related posts:"

THEME = "theme/egelance"

PLUGIN_PATHS = [ 'plugins' ]
PLUGINS = [  'related_posts', 'tag_cloud' ] # 'better_codeblock_line_numbering', 'tipue_search',

MD_EXTENSIONS = [ 'codehilite(css_class=highlight, linenums=True)', 'extra'] # 'fenced_code',

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))

DISQUS_SITENAME     = "The Egel's Blog"
GOOGLE_ANALYTICS    = 'google-analytics-id'

SUMMARY_MAX_LENGTH      = 50
NEWEST_FIRST_ARCHIVES   = True  # Show most recent posts first
REVERSE_CATEGORY_ORDER  = False

PYGMENTS_STYLE = "monokai"

AUTHOR = "Maciej Sypień"
# path-specific metadata
# EXTRA_PATH_METADATA = {
#   'extra/favicon.ico': {'path': 'favicon.ico'},
# }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM           = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM      = 'feeds/category/%s.atom.xml'
TAG_FEED_ATOM           = 'feeds/tag/%s.atom.xml'
TRANSLATION_FEED_ATOM   = 'feeds/all-%s.atom.xml'
AUTHOR_FEED_ATOM        = None
AUTHOR_FEED_RSS         = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
