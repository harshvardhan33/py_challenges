# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 13:39:54 2019

@author: hp
"""
filelist=[]
with open("romeo.txt","rt") as file:
    for i in file:
        filelist.extend(i.split())

print(filelist)
dict1={}
for item in filelist:
    if item not in dict1:
        dict1[item]=1
    else:
        dict1[item]=dict1[item] + 1
        
print(dict1)
