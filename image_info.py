import os
import csv
from PIL import Image

img_dir = './custom_theme/static/images'
files = os.listdir(img_dir)
img_data = []

for file in files:
    file = os.path.join(img_dir, file)
    img = Image.open(file)
    name = os.path.basename(file)
    height = img.height
    width = img.width
    asp_rat = height/width
    img_dict = {
        'name': name,
        'height': height,
        'width': width,
        'asp_rat': asp_rat
    } 
    img_data.append(img_dict)

with open('img_info.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'height', 'width', 'asp_rat']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in img_data:
        writer.writerow(row)