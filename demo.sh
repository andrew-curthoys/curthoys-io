#!/usr/bin/bash

echo "Starting demo server"
pelican -s pelicanconf.py -o output -t custom_theme -lr content
cd output
python -m http.server
cd ..