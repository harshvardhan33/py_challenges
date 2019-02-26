# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:45:52 2019

@author: hp
"""

"""Exception handling in python"""
import traceback
try:
    file=open("words1.txt","rt")
    print(file.name)

except Exception:
    print(traceback.format_exc())

finally:
    print("Always performed")
    
file.close()