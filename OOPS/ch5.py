# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:43:07 2019

@author: harshvardhan
"""

class Employee:
    # declare this in the class level 
    raise_amount = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last) 

    def apply_raise(self) :
        # self.pay = int ( self.pay * 1.04 ) 
        # we need to change this 
        self.pay = int ( self.pay * Employee.raise_amount )
        # or 
        #self.pay = int ( self.pay * self.raise_amount )

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

# How can we access the class variables using the self object 
print (Employee.raise_amount)
print("Before Raise : {}".format(emp_1.pay))
Employee.apply_raise(emp_1)
print("After Raise : {}".format(emp_1.pay))

print("Before Raise : {}".format(emp_2.pay))
Employee.apply_raise(emp_2)
print("After Raise : {}".format(emp_2.pay))


print (emp_1.__dict__ )
print("___"*25)
"""THIS CONVERTS THE EMP1 OBJECT INTO A DICTIONARY"""
print (emp_2.__dict__ )
print("___"*25)
print (Employee.__dict__ )

