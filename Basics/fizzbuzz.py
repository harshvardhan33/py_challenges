# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 12:51:22 2019

@author: hp
"""

for i in range(1,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")    
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
   
    else:
        print(i)
        
     