#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Maciej Sypie\u0144'
SITENAME = u"The Egel's Blog"
SITEURL = ''

STATIC_PATHS = ['blog', 'images', 'downloads']
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/'
ARTICLE_URL = '{date:%Y}/{slug}/'

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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
