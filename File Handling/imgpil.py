# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:01:11 2019

@author: harshvardhan
"""

from PIL import Image

# Open the image and create it's instance
img = Image.open("ac.jpg")

# Gives the dimentions or the size of the image
print (img.size)

# Gives the format of image like JPEG, PNG ...
print (img.format)

# Gives the mode of image like RGB, binary, GreyScale ...
print (img.mode)

# Displays the Image
img.show()

# Rotate the image with the given angle
# Create separate instance for rotated image
img_rotate = img.rotate(90)

# Displays the rotated image
img_rotate.show()  

img_rotate.save("ac.jpg")


# Flip the image
# Create separate instance for flipped image
img_flip = img.transpose(Image.FLIP_TOP_BOTTOM)

# Displays the rotated image
img_flip.show()  
img_flip.save("ac.jpg")