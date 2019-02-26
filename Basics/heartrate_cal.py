# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:39:17 2019

@author: hp
"""

age=int(input("Enter your age "))
max_heartrate=int(220-age)
print("Max Heartrate is ",max_heartrate)

lthrate=float(0.7*max_heartrate)
hthrate=float(0.85*max_heartrate)

print("Lower end heart rate is ",lthrate)
print("Higher end heart rate is ",hthrate)