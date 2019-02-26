# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:12:09 2019

@author: harshvardhan
"""

import pandas as pd 


data=pd.read_csv("zoo.csv")
print(data['animal'].unique())
print(data.groupby('animal')['water_need'].sum())
print("Total Sum oF nEED :",data['water_need'].sum())