#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://egel.pl'

# Following items are often useful when publishing
# We wants absolute URLs
RELATIVE_URLS = False

FEED_ALL_ATOM           = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM      = 'feeds/category/%s.atom.xml'
TAG_FEED_ATOM           = 'feeds/tag/%s.atom.xml'
TRANSLATION_FEED_ATOM   = 'feeds/all-%s.atom.xml'
AUTHOR_FEED_ATOM        = None
AUTHOR_FEED_RSS         = None

# don't delete our .git submodule dir
DELETE_OUTPUT_DIRECTORY = False

DISQUS_SHORT_NAME = "egel"
GOOGLE_ANALYTICS  = 'UA-26456669-2'


# minify
MINIFY = {
  'remove_comments': True,
  'remove_all_empty_space': True,
  'remove_optional_attribute_quotes': False
}

PLUGINS.append('minify')

