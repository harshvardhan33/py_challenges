# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:40:56 2019

@author: harshvardhan
"""

import urllib.request
import json

send_url = "http://13.127.155.43/api_v0.1/sending"
data = {
        "Phone_Number" : "9887765324",
        "Name" : "James Bond",
        "College_Name" : "Harward",
        "Branch" : "CSE"
        }
data = json.dumps(data)
header = {"Content-Type" : "application/json"}
request = urllib.request.Request(send_url,data,headers=header)
send_response = urllib.request.urlopen(request)
print (send_response.read())
