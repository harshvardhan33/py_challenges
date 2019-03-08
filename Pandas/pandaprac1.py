# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:37:02 2019

@author: harshvardhan
"""
import pandas as pd 

df=pd.read_csv("Salaries.csv")

print(df["rank"])
print(df["rank"].value_counts(normalize=True))
"""if we put the normalize function then it will return in the percentage"""
print(df["rank"].count())


print(df['salary'].mean())
"""The describe is the method that will give us different statistitcal values"""
print(df['salary'].describe())

"""Grouping and slicing of pandas dataframes"""
df.groupby(['rank'],sort=False).mean()


dfsalary=df[(df['salary']>120000)][['rank','discipline']]


df_sub=df[(df['salary']>120000) & \
           (df['years']>10) & \
           (df['sex']=='Male')]

df.loc[10:,['rank','sex']]
df.iloc[2:10,[0,2,3]]

df.iloc[1:5, :-5]


df.iloc[[0,5,6,7], [1,3]]


df.sort_values( by='service').head()

df_sorted= df.sort_values( by=['service','salary'], ascending = [False,False])
df_sorted.head(10)
