"""
Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG
Note: The raw images from images subdirectory contains alpha transparency layers. 
So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images. 
Use convert("RGB") method for converting RGBA to RGB image.
"""

#!/usr/bin/env python3
import os
from PIL import Image

#Iterate through each file in the folder
#folderOrigin = "/supplier-data/images"
os.chdir(folderOrigin)
filesToCheck = filter(os.path.isfile, os.listdir(folderOrigin))
filesToCheck = [f for f in filesToCheck if os.path.isfile(folderOrigin + '/' + f)] #Filtering only the files.
print(filesToCheck)
for photo in filesToCheck:
    try:
        im = Image.open(photo)
    except:
        continue

    #Change image resolution from 3000x2000 to 600x400 pixel
    size = (600,400)
    im = im.resize(size)

    # Change image format from .TIFF to .JPEG
    rgb_im  = im.convert("RGB")

    #Save the image to a new folder in .jpeg format
    folderDestination = "D:\Python\practicas\Coursea\OPT"
    #folderDestination = "/supplier-data/images"
    formatImage = "jpeg"
    nameOutput = os.path.join(folderDestination, photo[:-4] + "jpeg")
    rgb_im.save(nameOutput, format=formatImage)
