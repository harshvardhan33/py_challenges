# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:29:49 2019

@author: harshvardhan
"""

import requests

data = {"Phone_Number":"9414291932",
        "Name":"James Bond", 
        "College_Name":"Haward",
        "Branch":"CSE"}

send_url = "http://13.127.155.43/api_v0.1/sending"
send_req = requests.post(send_url, json = data)
print (send_req.text)

receive_url = "http://13.127.155.43/api_v0.1/receiving?Phone_Number=9414291932"
receive_req = requests.get(receive_url)
print (receive_req.text)
