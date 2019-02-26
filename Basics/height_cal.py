# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 12:14:05 2019

@author: hp
"""

foot=int(input("Enter your height in FOOT\n"))
inch=int(input("Enter your height in INCH\n"))
fm=float(foot*0.3048)
im=float(inch*0.0254)
print("Total Height in Metres",fm + im)
print("Total Height in Centimetres",(fm + im)*100)

