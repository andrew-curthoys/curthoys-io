#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Generic Site Info
AUTHOR = 'Andrew Curthoys'
SITENAME = "The Wide Weird World of Toy"
SITESUBHEADER = "A playground for all my beep boopin"
SITEURL = 'curthoys.io'

# Traveler Info
TRAVELERSITENAME = "Uncle Andy's Traveler"
TRAVELERSUBHEADER = "Musings of a panhandlin manhandlin highrollin dustbowlin daddy"

PATH = 'content'
STATIC_PATHS = ['traveler']
ARTICLE_PATHS = STATIC_PATHS
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
USE_FOLDER_AS_CATEGORY = True
DIRECT_TEMPLATES = ['index', 'traveler/index']
DELETE_OUTPUT_DIRECTORY = True

THEME = 'custom_theme'
CSS_FILE = '/theme/css/test.css'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True