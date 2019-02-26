# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:59:30 2019

@author: hp
"""

name=input("Enter your first and last name ")
""""
name.reverse()
y=" ".join(name)
print(y)
"""


for i in range(0,len(name)):
    if(name[i]==" "):
        c=i
        d=i-1
print(name[c:]+" "+name[:d+1])