#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Dario Blanco'
SITENAME = u'The soft jaguar'
SITEURL = 'http://thesoftjaguar.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10

THEME = 'bootstrap-theme'

TEMPLATE_PAGES = {
    'projects.html': 'projects.html',
}

# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'
