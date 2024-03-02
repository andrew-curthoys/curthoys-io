#!/usr/bin/bash

echo "Starting demo server"
npm run scss --prefix ./custom_theme/static/ &
pelican -s pelicanconf.py -o output -t custom_theme -lr content
cd output
python -m http.server
cd ..