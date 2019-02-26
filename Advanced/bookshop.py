# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 11:36:06 2019

@author: harshvardhan
"""



import pandas as pd

data=pd.read_csv('bookshop.txt',sep=" ",header=None)
data.columns=["OrderNumber","BookTitle","Author","Quantity","Price"]




print("Enter The Product ID(0,1,2,3): ")
prid=int(input())
quant=int(input("Enter Quantity "))

if(prid==0):
    x=float(data.loc[prid:prid,'Price'])
    val=float(x*quant)
    if(val<100):
        val+=10
        print(val)
    
elif(prid==1):
    x=float(data.loc[prid:prid,'Price'])
    val=float(x*quant)
    if(val<100):
        val+=10
        print(val)

elif(prid==2):
    x=float(data.loc[prid:prid,'Price'])
    val=float(x*quant)
    if(val<100):
        val+=10
        print(val)

elif(prid==3):
    x=float(data.loc[prid:prid,'Price'])
    val=float(x*quant)
    if(val<100):
        val+=10
        print(val)
