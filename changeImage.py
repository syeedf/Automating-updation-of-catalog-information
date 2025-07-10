#!/usr/bin/env python3
  
from PIL import Image
import os

image_location= os.path.expanduser("~/supplier-data/images/")

for filename in os.listdir(image_location):
    if filename[0] == '0':

        filepath= os.path.join(image_location,filename)
        image= Image.open(filepath)
        newimage= image.resize((600,400)).convert('RGB')
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}.jpeg"
        new_path = os.path.join(image_location, new_filename)
        newimage.save(new_path)
