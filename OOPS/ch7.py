# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:43:05 2019

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
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first,self.last) 

    def apply_raise(self) :
        # self.pay = int ( self.pay * 1.04 ) 
        # we need to change this 
        self.pay = int ( self.pay * Employee.raise_amount )
        # or 
        self.pay = int ( self.pay * self.raise_amount )

    @classmethod
    def set_raise_amt( cls, amount ) :
        cls.raise_amount = amount

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

print (Employee.raise_amount)
print("Before Raise : {}".format(emp_1.pay))
Employee.apply_raise(emp_1)
print("After Raise : {}".format(emp_1.pay))

print("Before Raise : {}".format(emp_2.pay))
Employee.apply_raise(emp_2)
print("After Raise : {}".format(emp_2.pay))

print("***"*25)
Employee.set_raise_amt(1.05)

print (Employee.raise_amount)
print("Before Raise : {}".format(emp_1.pay))
Employee.apply_raise(emp_1)
print("After Raise : {}".format(emp_1.pay))

print("Before Raise : {}".format(emp_2.pay))
Employee.apply_raise(emp_2)
print("After Raise : {}".format(emp_2.pay))
# or
emp_1.set_raise_amt(1.05)
# you can call this from instance also.. but it doesn’t make sense 

