# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:06:43 2019

@author: harshvardhan
"""
import pandas as pd
salary=pd.read_csv("Salaries.csv")

salary[salary.isnull().any(axis=1)].head(2)
new_df = salary.dropna()
salary.fillna(method='ffill')
"""IN forward fill pick the value right above it and fill the NA value
in backward fill the value at bottom on the place of Na value """

salary.fillna(100)