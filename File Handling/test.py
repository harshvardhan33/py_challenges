# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:30:53 2019

@author: harshvardhan
"""

l = []
n = int(input("Enter length of list: "))
for i in range(n):
    x = int(input("Enter %d numbers: "%n))
    l.append(x)






def fcheck(x):
    return x%3==0


s = filter(fcheck,l)
for x in s :
    print(x)