# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:28:55 2019

@author: harshvardhan
"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# create the database if does not exists
mydb = client.employee



# adding the employee in the employee collection
def add_employee(idd, first, last, pay):
    unique_employee = mydb.employees.find_one({"id":idd})
    if unique_employee:
        return "Employee already exists"
    else:
        mydb.employees.insert_one(
                {
                "id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "Employee added successfully"

def fetch_all_employee():
    user = mydb.employees.find()
    for i in user:
        print (i)


add_employee(1,'HarshVardhan', 'Singh', 50000)
add_employee(2,'AdityaRaj', 'Singh', 70000)
add_employee(3,'Gajwardhan', 'Singh', 30000)
add_employee(4,'MohitBansal', 'Chidiya', 30000)
add_employee(5,'Bitu', 'Bhokali', 30000)

fetch_all_employee()
