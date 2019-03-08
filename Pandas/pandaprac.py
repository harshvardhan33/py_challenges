# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:28:01 2019

@author: harshvardhan
"""

import pandas as pd

df=pd.read_csv("Salaries.csv")
print(df)

print(df.dtypes)
print(df.axes)
print(df.columns)
print(df.ndim)
print(df.shape)
print(df.values)
print(df.describe)
print(df.max())
print(df.min())
print(df.mean())
print(df.median())
print(df.std())
print(df.sample())
