#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Generic Site Info
AUTHOR = 'Andrew Curthoys'
SITENAME = "The Wide Weird World of Toy"
SITESUBHEADER = "A playground for all my beep boopin"
SITEURL = 'curthoys.io'

# Eater Info
EATERSITENAME = "Eater"
EATERSUBHEADER = "I like to eat and I like to cook. Let's go on some culinary adventures."

# Entroper Intro
ENTROPERSITENAME = "Entroper"
ENTROPERSUBHEADER = "An assortment of random things trending towards disorder."

# Rambler Info
RAMBLERSITENAME = "Rambler"
RAMBLERSUBHEADER = "Athletic events, runs, bikes, and the sort."

# Traveler Info
TRAVELERSITENAME = "Uncle Andy's Traveler"
TRAVELERSUBHEADER = "A collection of stories from my jaunts, journeys, excursions, and walkabouts."

# Career Info
CAREERSITENAME = "Career"
CAREERSUBHEADER = "Stuff I've done."

PATH = 'content'
STATIC_PATHS = ['eater', 'entroper', 'rambler', 'traveler', 'misc']
ARTICLE_PATHS = STATIC_PATHS
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
PAGE_PATHS = ['career']
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
JINJA2CONTENT_TEMPLATES = ['content']
USE_FOLDER_AS_CATEGORY = True
DIRECT_TEMPLATES = ['index',
                    'eater/index',
                    'entroper/index',
                    'rambler/index',
                    'traveler/index',
                    'career/index',
                    'misc/index',
                    'traveler/2021_04-ski_trip',
                    'traveler/2021_09-costa_rica',
                    'traveler/2022_01-ski_trip',
                    'traveler/2023_05-scandinavia',
                    'entroper/2023_06-this_land'
]
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

import random
def filter_shuffle(seq):
    try:
        result = list(seq)
        random.shuffle(result)
        return result
    except:
        return seq

JINJA_FILTERS = {'shuffle': filter_shuffle,
                 'zip': zip}