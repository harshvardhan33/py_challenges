# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:47:36 2019

@author: harshvardhan
"""

import urllib.request
import requests


cityName = input("Enter the city name please: ")

url = "http://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid=e9185b28e9969fb7a300801eb026de9c"
resp = urllib.request.urlopen(url)   # GET request to REST API
print(resp.read())

print(" * "*20)

resp = requests.get(url)
print (resp.text)