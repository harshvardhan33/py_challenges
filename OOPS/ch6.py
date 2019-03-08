# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:04:30 2019

@author: harshvardhan
"""

class Employee:
    # declare this in the class level 
    raise_amount = 1.04 
    num_of_emps = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"
        # we need to increase the value in the init method
        self.num_of_emps+=1
        

    def fullname(self):
        return "{} {}".format(self.first,self.last) 

    def apply_raise(self) :
        # self.pay = int ( self.pay * 1.04 ) 
        # we need to change this 
        self.pay = int ( self.pay * Employee.raise_amount )
        # or 
        self.pay = int ( self.pay * self.raise_amount )

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)


print ( Employee.num_of_emps )
