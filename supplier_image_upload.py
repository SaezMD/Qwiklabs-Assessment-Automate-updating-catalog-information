#!/usr/bin/env python3
import requests, os

folderOrigin = "/supplier-data/images"
courseaIP =  ""
url = "http://" + courseaIP + "/upload/"

files = os.listdir(folderOrigin)
for file in files:
    if file.endswith(".jpeg"):
        with open(os.path.join(folderOrigin,file), 'rb') as opened:
            r = requests.post(url, files={'file': opened})


