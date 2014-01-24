#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://thesoftjaguar.com'

DELETE_OUTPUT_DIRECTORY = True

RELATIVE_URLS = False

DISQUS_SITENAME = "thesoftjaguar"
GOOGLE_ANALYTICS = "UA-27981742-1"

# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = None
TAG_FEED_RSS = None
