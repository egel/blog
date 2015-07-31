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

DEFAULT_METADATA = {
  'status': 'draft',
}

DEFAULT_DATE_FORMAT = '%d %B %Y'

THEME = "theme/egelance"

PLUGIN_PATHS = [ 'plugins' ]
PLUGINS = [ 'tipue_search' ]

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))


PYGMENTS_RST_OPTIONS = {
    'classprefix': 'pgcss',
    'linenos': 'table'
}


SUMMARY_MAX_LENGTH = 50

# path-specific metadata
# EXTRA_PATH_METADATA = {
#   'extra/favicon.ico': {'path': 'favicon.ico'},
# }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM           = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM      = None
TRANSLATION_FEED_ATOM   = 'feeds/all-%s.atom.xml'
AUTHOR_FEED_ATOM        = None
AUTHOR_FEED_RSS         = None


NEWEST_FIRST_ARCHIVES   = True
REVERSE_CATEGORY_ORDER  = False


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/MaciejSypien'),
          ('Github', 'https://github.com/egel'),
          ('LinkedIn', 'https://www.linkedin.com/in/maciejsypien'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
