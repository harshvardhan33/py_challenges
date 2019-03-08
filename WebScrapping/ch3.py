# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:20:38 2019

@author: harshvardhan
"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


wiki="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
page=urllib.request.urlopen(wiki)
soup=BeautifulSoup(page,features="lxml")


tableicc=soup.find('table',class_='table')
A=[]
B=[]
C=[]
D=[]
E=[]

for row in tableicc.find_all("tr"):
    cells=row.findAll('td')
    
    if(len(cells)==5):
        A.append(cells[0].text)
        B.append(cells[1].text)
        C.append(cells[2].text)
        D.append(cells[3].text)
        E.append(cells[4].text)
      
        
df=pd.DataFrame(A,columns=['Pos'])
df['Team']=B
df['Weighted_Matches']=C
df['Points']=D
df['Rating']=E


print(df)