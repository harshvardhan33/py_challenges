# OOP's in Python 
"""
Introducing the keywords of OOP

Logically group data and function 
Easy to re use and build upon
Data and function are known as attributes( characteristics ) 
and methods ( function associated with a class )
class is a blueprint for creating instances 


Introduce the concept of Radio Blueprint 

 
Classes and Instances

Represent Employee in Python 
Individual employee will have specific attributes and methods
Name
email address
Pay


class is a blueprint for creating instances 
each individual employee would be the instance of the class 
"""

class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()


print ( emp_1)
print ( id(emp_1))

print ( emp_2)
print ( id(emp_2))


# Instance variable has data which is unique to each instance 

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


# Why should you set the instance variable manually everytime
# It should have been set when we create the instance (object)
# Use __init__ method to create the instance variables ( constructor )
# create init method within the class 

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"


emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

print(emp_1.email)
print(emp_2.email)


# Adding Action to the class using methods 
# Display Full Name of the employee 
# create method in the class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email=first.lower() + "." + last.lower() + "@gmail.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last) 

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

print ( emp_1.fullname() )
print ( emp_2.fullname() )

# calling the methods from the class name, 
# but we need to pass the instance

print (Employee.fullname(emp_1))
print (Employee.fullname(emp_2))


# Class Variables
# Variables which are shared among all the instance of the class 
# Class variable should be the same for all the instances of the class
# Which are the data which can be shared among all the employees

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
emp_1.apply_raise()
print (emp_1.pay)


# Whats wrong. We cannot access the raise amount 
# emp1_raise_amount
# Employee.raise_amount

# Easily update  the 4 % pay raise amount

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
print (emp_1.raise_amount)
print (emp_2.raise_amount)


# The logic is that when we try to access it first check with the instance variable 
# and if it is not present it then check with the class variable  

print (emp_1.__dict__ )
# there is not raise_amount in this dictionary 

print (Employee.__dict__ )


# class variable that holds the number of employees depending on the instances created 

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

emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)


print ( Employee.num_of_emps )


# If we have class variables, do we also have class methods 
# Difference between regular methods , classmethods and staticmethods
# regular methods take self as the first argument 
# Converting a regular method to a class method is by adding a decorator to it

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
print (emp_1.raise_amount)
print (emp_2.raise_amount)

Employee.set_raise_amount(1.05)
# or
emp_1.set_raise_amount(1.05)
# you can call this from instance also.. but it doesn’t make sense 

print (Employee.raise_amount)
print (emp_1.raise_amount)
print (emp_2.raise_amount)


# Class methods are a alternative to constructors 

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

    @classmethod
    def from_string(cls,emp_str) :
        first, last,pay = emp_str.split('-')
        return cls ( first, last,pay)


emp_1 = Employee.from_string("Sylvester-Fernandes-50000")
emp_2 = Employee.from_string("Yogendra-Singh-60000")


# DateTime module uses a lot of classmethod as alternative to constructor 
# fromtimestamp
# today
# from ordinal


# Static method 

# Regular methods pass self automatically 
# Class methods pass cls automatically 
# Static methods do not pass anything automatically 


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

    @classmethod
    def from_string(cls,emp_str) :
        first, last,pay = emp_str.split('-')
        return cls ( first, last,pay)

    @staticmethod
    def is_workday(day) :
        if (day.weekday() == 5) or (day.weekday() == 6) :
            return False
        return True

import datetime
my_date = datetime.date(2016,7,10)
print ( Employee.is_workday(my_date) )

my_date = datetime.date(2016,7,11)
print ( Employee.is_workday(my_date) )


# Inheritance - Creating Subclasses

class Developer( Employee ) :
    pass

dev_1 = Employee ("Sylvester", "Fernandes",50000)
dev_2 = Employee ("Yogendra", "Singh",60000)

print (dev_1.email)
print (dev_2.email)

dev_1 = Developer ("Sylvester", "Fernandes",50000)
dev_2 = Developer ("Yogendra", "Singh",60000)

print ( dev_1.email )
print ( dev_2.email )

# This gives a clear picture of the inheritance and the variables 
# Method resolution order
print ( help( Developer ) ) 


class Developer( Employee ) :
    raise_amount = 1.10
# this will only affect the instances of the Developer class and not Employee class 

dev_1 = Employee ("Sylvester", "Fernandes",50000)

print (dev_1.pay)
dev_1.apply_raise()
print (dev_1.pay) 


# Creating the initialize 

class Developer( Employee ) :
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang ):
        super().__init__(first, last,pay)
        # or
        # Employee.__init__(self, first,last,pay)

        self.prog_lang = prog_lang  



# this will only affect the instances of the Developer class and not Employee class 

dev_1 = Developer ("Sylvester", "Fernandes",50000,"Python")
dev_2 = Developer ("Yogendra", "Singh",60000,"Java")


print ( dev_1.email )
print ( dev_1.prog_lang )

"""
Special (Magic_Dunder) Methods
Operator Overloading 
Property Decorators - Getters, Setters, and Deleters
This gives attribute a special functionality of getters, setter and deleters 
using the Property Decrators we can achieve the above in the class 
"""

# remove the email from init 


class Employee:
    # declare this in the class level 
    raise_amount = 1.04 
    num_of_emps = 0

    # declaring like a method but accessing like a attribute 
    # internal it creates two methods - getter 
    @property
    def email(self) :
        return  '{}.{}@gmail.com'.format(self.first.lower(), self.last.lower())

    @email.setter 
    def email(self, email) :
        self.email = email
  
    @email.deleter 
    def email(self) :
        print ("delete email" )
        self.email = None

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        # self.email=first.lower() + "." + last.lower() + "@gmail.com"
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

    @classmethod
    def from_string(cls,emp_str) :
        first, last,pay = emp_str.split('-')
        return cls ( first, last,pay)

    @staticmethod
    def is_workday(day) :
        if (day.weekday() == 5) or (day.weekday() == 6) :
            return False
        return True


emp_1 = Employee("Sylvester","Fernandes",50000)
emp_2 = Employee("Yogendra","Singh",60000)

# In this case it is calling getter 
print (emp_1.email)
print (emp_1.fullname())

emp_1.email = "sylvesterferns@gmail.com"
# this time it is calling the setter


del (emp_1.email )