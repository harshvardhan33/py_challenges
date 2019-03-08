# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:26:19 2019

@author: harshvardhan
"""

from pymongo import MongoClient
client=MongoClient('localhost',27017)
mydb=client.student

mydb.student.insert_one({"id" :1,"first" : 'harsh',"last" :'vardhan',"pay" :10})
mydb.student.insert_one({"id" :2,"first" : 'adityaraj',"last" :'singh',"pay" :20})