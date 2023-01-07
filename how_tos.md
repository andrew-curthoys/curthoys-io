# How To Guides
## Add New Trip
* Create folder for .md files
* Add trip homepage to 'article.html'
* Add trip to 'traveler/index.html'

## Add New Article
* Create & write .md file
* Update 'article.html' with name & alias in the 'dayDict'

## Add New Book
* Update 'index.html' with new book

## Make GIF
ffmpeg -i <video_input_file> -ss <start_time in "00:00:00" format> -to <end_time in "00:00:00" format> -filter_complex "[0:v] fps=12, scale=480:-1, split [a][b]; [a] palettegen=stats_mode=single [p];[b][p] paletteuse=new=1" <output_file>.gif
