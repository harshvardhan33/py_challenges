# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:57:51 2019

@author: harshvardhan
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"


emp_1=Employee('Harsh','Vardhan',10)
print(emp_1.email)
print(emp_1.pay)