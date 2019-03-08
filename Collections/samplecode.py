# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:13:44 2019

@author: harshvardhan
"""


from collections import Counter
from collections import defaultdict

list1=[1,1,2,3,4,5,3,2,3,4,2,1,2,3]
cnt =Counter(list1)
print(cnt)

print(Counter(list1).items())
print(Counter(list1).keys())
print(Counter(list1).values())

s = 'Some letters appear several times in this text.'


dd=defaultdict(int)
for i in s:
    dd[i]+=1

print(dd)
