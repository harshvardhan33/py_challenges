# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:43:32 2019

@author: hp
"""

file=open("words.txt","rt")
print(file.name)
print(file.mode)
print(file.closed)

file.close()
print(file.closed)