# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:05:26 2019

@author: hp
"""

with open("words.txt","rt") as file:
   file_contents = file.readlines()
   print(type(file_contents))
   print (file_contents)
   """file_contents = file.readline()
   print(type(file_contents))
   print (file_contents)"""

   