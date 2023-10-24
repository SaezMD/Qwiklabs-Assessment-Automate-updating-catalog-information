"""
Write a Python script named run.py to process the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. 
The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), 
and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library.
Django application fruit has the following fields: 
name 
weight : if the weight is "500 lbs", you need to drop "lbs" and convert "500" to an integer.
description
image_name. 
"""

#!/usr/bin/env python3
import os, requests, re

folderOrigin = "/supplier-data/descriptions"
courseaIP =  ""
url = "http://" + courseaIP + "/fruits/"

feedbackFiles = os.listdir(folderOrigin)
print(feedbackFiles)

files = os.listdir(folderOrigin)
for file in files:
    dict = {} #Set dict to empty
    with open(os.path.join(folderOrigin, file), 'r') as f:
        dict['name'] = f.readline()
        m = re.findall(r"(?P<numberINT>\d+)",  f.readline()) # take only the number in the line
        dict['weight'] = m[0]
        dict['description'] = f.readline()
        dict['image_name'] = file[:-4] + ".jpeg"

    print(dict)
    
    #Send the JSON and check for failures
    sendData = requests.post(url, data = dict)
    sendData.ok
    print(sendData.request.body)
    print(sendData.raise_for_status())

