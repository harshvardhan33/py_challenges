# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:52:07 2019

@author: harshvardhan
"""

import requests
import json
api_key = "65mczz6BHJHLMxUayNO2VXNYWedu11q4"
collection = "employee"
database = "employees"

data_dict = {}

# adding the employee in the employee collection
def add_employee(idd, first, last, pay):
  
  data_dict = {"id" : idd,"first" : first,"last" : last,"pay" : pay}
  add_data_to_mlab(data_dict)
        
        

res = ""
def add_data_to_mlab(data_dict):
    
    url = "https://api.mlab.com/api/1/databases/{}/collections/{}?apiKey={}".format(database,collection,api_key)
    response = requests.post(url, json =data_dict)
    
    res = response.status_code
    if res == 200:
        print ("data added successfully")
    else:
        print ("response is something else:")
        print (res)



    
def fetch_all_employee():
    
    url = "https://api.mlab.com/api/1/databases/{}/collections/{}?apiKey={}".format(database,collection,api_key)
    response = requests.get(url)
    
    res = json.loads(response.text)
    print (res)
    
    
    

add_employee(1,'HarshVardhan', 'Singh', 50000)
add_employee(2,'AdityaRaj', 'Singh', 70000)
add_employee(3,'Gajwardhan', 'Singh', 30000)
add_employee(4,'MohitBansal', 'Chidiya', 30000)
add_employee(5,'Bitu', 'Bhokali', 30000)

fetch_all_employee()


