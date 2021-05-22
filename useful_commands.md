## Create content
### From main project directory
pelican -s pelicanconf.py -o output content

### If we have a custom theme use this:
pelican -s pelicanconf.py -o output -t theme content

## Run HTTP server
cd output
python -m http.server