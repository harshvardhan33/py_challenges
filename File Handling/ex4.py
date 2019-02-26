# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:26:24 2019

@author: hp
"""

file=open("words.txt","rt")
position = file.tell()
print (position)

file.readlines()
position=file.tell()
print(position)