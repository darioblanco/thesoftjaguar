#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Dario Blanco'
SITENAME = u'The soft jaguar'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_DATE_FORMAT = '%d %b, %Y'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 10

THEME = 'bootstrap-theme'

TEMPLATE_PAGES = {
    'projects.html': 'projects.html',
    'presentations.html': 'presentations.html',
    'pres_python-webservers.html': 'pres_python-webservers.html'
}

# Urls
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
