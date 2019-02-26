# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:06:26 2019

@author: harshvardhan
"""
def fcheck(x):
    return x%2==0

list1=[]
num=int(input("Enter the number of inputs you would like to enter :"))

for i in range(num):
    x=int(input("Number daalo :"))
    list1.append(x)

 
s = filter(fcheck,list1)
for x in s:
    print(x)

