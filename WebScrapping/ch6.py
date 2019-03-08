# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:02:14 2019

@author: harshvardhan
"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd



#specify the url
wiki = "https://geographyfieldwork.com/WorldCapitalCities.htm"
page = urllib.request.urlopen(wiki)

soup = BeautifulSoup(page,features="lxml")
divc=soup.find('table',class_="sortable")



A=[]
B=[]

for row in divc.find_all("tr"):
    cells=row.findAll('td')
    
    
    if(len(cells)==2):
        A.append(cells[0].text)
        B.append(cells[1].text)
        
df=pd.DataFrame(A,columns=['Country'])
df['Capital']=B



print(df)