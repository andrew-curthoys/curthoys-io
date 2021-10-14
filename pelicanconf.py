#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Generic Site Info
AUTHOR = 'Andrew Curthoys'
SITENAME = "The Wide Weird World of Toy"
SITESUBHEADER = "A playground for all my beep boopin"
SITEURL = 'curthoys.io'

# Traveler Info
TRAVELERSITENAME = "Uncle Andy's Traveler"
TRAVELERSUBHEADER = "A collection of stories from my jaunts, journeys, excursions, and walkabouts"

# Eater Info
EATERSITENAME = "Eater"
EATERSUBHEADER = "I like to eat and I like to cook. Let's go on some culinary adventures."

# Career Info
CAREERSITENAME = "Career"
CAREERSUBHEADER = "Stuff I've done"

PATH = 'content'
STATIC_PATHS = ['traveler', 'eater']
ARTICLE_PATHS = STATIC_PATHS
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
PAGE_PATHS = ['career']
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
USE_FOLDER_AS_CATEGORY = True
DIRECT_TEMPLATES = ['index', 'traveler/index', 'eater/index', 'career/index']
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