#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Dario Blanco'
SITENAME = u'The soft jaguar'
SITEURL = 'http://thesoftjaguar.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_DATE_FORMAT = '%d %b, %Y'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10

THEME = 'bootstrap-theme'

TEMPLATE_PAGES = {
    'projects.html': 'projects.html',
}

# Urls
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Feeds
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'
