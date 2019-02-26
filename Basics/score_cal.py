# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:17:12 2019

@author: hp
"""

a1=int(input("Enter Assignment 1 marks "))
a2=int(input("Enter Assignment 2 marks "))
a3=int(input("Enter Assignment 3 marks "))
e1=int(input("Enter Exam 1 marks "))
e2=int(input("Enter Exam 2 marks "))


print("Weighted Score is ",float((a1+a2+a3)*0.1+(e1+e2)*0.35))
