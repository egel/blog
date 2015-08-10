#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR          = 'Maciej Sypień'
SITENAME        = "The Egel's Blog"
SITEURL         = 'http://pelican-egel-blog.test'
TIMEZONE        = 'Europe/Warsaw'
DEFAULT_LANG    = 'en'

PATH            = 'content'
OUTPUT_PATH     = 'output/'

STATIC_PATHS        = ['images', 'downloads']
ARTICLE_PATHS       = ['blog']
PAGE_PATHS          = ['pages']

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
DEFAULT_DATE_FORMAT = '%d %B %Y'

THEME = "theme/egelance"

PLUGIN_PATHS = [ 'plugins' ]
PLUGINS = [ 'tipue_search' ]

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))

DISQUS_SITENAME     = "The Egel's Blog"
GOOGLE_ANALYTICS    = 'google-analytics-id'

SUMMARY_MAX_LENGTH      = 50
NEWEST_FIRST_ARCHIVES   = True  # Show most recent posts first
REVERSE_CATEGORY_ORDER  = False

PYGMENTS_STYLE = "tango"

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

FEEDS =  (('All posts', 'feeds/all.atom.xml'),
          ('Category', 'feeds/category'),
          ('OPW', 'feeds/tag/opw.atom.xml'),)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/MaciejSypien'),
          ('Github', 'https://github.com/egel'),
          ('LinkedIn', 'https://www.linkedin.com/in/maciejsypien'),)

HIDE_SIDEBAR = True
ABOUT_ME = """
Hey! I'm Maciej, geek amazed by computers, science, hacking, open source and astrophysics.
"""

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
