# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:08:56 2019

@author: harshvardhan
"""

import json
import requests


def main():
    sendData()
    #recieveData()
def sendData():
    r = requests.post('http://httpbin.org/post', json={"firstname": "harshvardhan","lastname":"singh"})
    print(r)
    data =r.json()
    print(data)
    

    




if __name__=="__main__":
    main()