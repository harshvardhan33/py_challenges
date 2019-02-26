# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:05:34 2019

@author: harshvardhan
"""


from PIL import Image

img_bw = Image.open("ac.jpg")
img_bw.convert(mode='L').save('acblack.jpg')
img_bw = Image.open("acblack.jpg")
img_bw.show()