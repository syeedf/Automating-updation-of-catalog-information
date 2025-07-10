#!/usr/bin/env python3


import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

image_location= os.path.expanduser("~/supplier-data/images/")
url = "http://104.197.188.125/upload/"

for filename in os.listdir(image_location):
    if filename[-4:]=="jpeg":
        nameholder= filename.split('.')[0]
        with open(image_location+nameholder+'.jpeg', 'rb') as opened:
            r = requests.post(url, files={'file': opened})