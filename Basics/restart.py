# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:36:02 2019

@author: hp
"""

str1=list("RESTART")
for i in range(0,len(str1)):
    if(str1[i]=='R'):
        if(i==0):
            pass
        else:
            str1[i]='$'

s="".join(str1)
print(s)