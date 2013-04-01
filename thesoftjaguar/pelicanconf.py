#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Dario Blanco'
SITENAME = u'The soft jaguar'
SITEURL = 'http://thesoftjaguar.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Blogroll
LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/darioblanco'),
          ('facebook', 'https://www.facebook.com/dario.blancoit'),
          ('linkedin', 'http://www.linkedin.com/in/darioblancoiturriaga'),
          ('github', 'http://github.com/sharkerz'),)

DEFAULT_PAGINATION = 10

GITHUB_URL = 'http://github.com/sharkerz/'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
THEME = 'bootstrap-theme'
TEMPLATE_PAGES = {
    'projects.html': 'projects.html',
}
