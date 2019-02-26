# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:36:11 2019

@author: hp
"""

wt=float(input("Enter your weight in KG\n"))
ht=float(input("Enter your height in MT\n"))

ponderal_index=float(wt/ht**3)
print("YOUR PONDERAL INDEX IS", ponderal_index)