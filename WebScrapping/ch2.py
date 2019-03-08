# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:42:16 2019

@author: harshvardhan
"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

url="https://wordpandit.com/29-states-capitals/"
page=urllib.request.urlopen(url)

soup=BeautifulSoup(page,features="lxml")

table1=soup.find('table',class_='alignleft')
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in table1.findAll('tr'):
    cells=row.findAll('td')
    
    A.append(cells[0].find(text=True))
    B.append(cells[1].find(text=True))
    C.append(cells[2].find(text=True))
    D.append(cells[3].find(text=True))
    E.append(cells[4].find(text=True))
    F.append(cells[5].find(text=True))
    
df=pd.DataFrame(A,columns=['S. No.'])

df['States']=B
df['Capital']=C
df['Cheif Minister']=D
df['Political Party']=E
df['Governer']=F

print(df)
df.to_csv("testing.csv")