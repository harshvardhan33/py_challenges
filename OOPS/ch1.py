# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:34:24 2019

@author: harshvardhan
"""

class Employee:
    pass
        
emp_1=Employee()
emp_2=Employee()

print ( emp_1)
print ( id(emp_1))

print ( emp_2)
print ( id(emp_2))

emp_1.first = "Sylvester"
emp_1.last = "Fernandes"
emp_1.email = "sylvester.fernandes@gmail.com"
emp_1.pay = 50000

emp_2.first = "Yogendra"
emp_2.last = "Singh"
emp_2.email = "yogendra.singh@gmail.com"
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

