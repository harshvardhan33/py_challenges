# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:46:51 2019

@author: hp
"""

file=open("absentee.txt",mode="wt")
for i in range(0,5):
        x=input("Enter Name : ")
        if(x==""):
            break
        file.write(x +"\n")
                       
file.close()
file=open("absentee.txt",mode="rt")
for j in file:
    print(j)
