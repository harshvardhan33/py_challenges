# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:16:07 2019

@author: harshvardhan
"""


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last) 


    def apply_raise(self):
        self.pay = int ( self.pay * 1.04 ) 

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

print (emp_1.pay)
Employee.apply_raise(emp_1)
print (emp_1.pay)
