# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 13:44:35 2019

@author: hp
"""

file=open("words.txt","rt")

line = file.readline()
print (line) 
       
file.seek(3,0) 
position = file.tell()
print (position)

file_contents = file.read(5)
print (file_contents)

position = file.tell()
print (position)

lines = file.readlines()
print (lines)
