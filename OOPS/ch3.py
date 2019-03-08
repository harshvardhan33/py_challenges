# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:59:27 2019

@author: harshvardhan
"""

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"
        print("SUCCESS")

    def fullname(self):
        return "{} {}".format(self.first,self.last) 

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)


# calling the methods from the class name, 
# but we need to pass the instance

print (Employee.fullname(emp_1))
print (Employee.fullname(emp_2))

