#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:44:05 2018

@author: ajoyfern
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 07:02:21 2017

@author: Forsk
"""

# Web Scrapping
#import the library used to query a website
import urllib2
#specify the url
wiki = "https://simple.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)

"""
If you are using the requests library, do:
import requests
page = requests.get(wiki).text

"""

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page) #lxml is the best parser, html5lib is also popular 

#to see the html, you can use "print soup"
# to see indented html content, use
# print soup.prettify()

#in case you do not find the object, please check for right table name
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]


for row in right_table.find_all("tr"):   #findAll() also works
  
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].text)
        B.append(states[0].text)
        C.append(cells[1].text)
        D.append(cells[2].text)
        E.append(cells[3].text)
        F.append(cells[4].text)
        G.append(cells[5].text)
        #G.append(cells[5].find(text=True))
        

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print df













"""

Example 02

"""


# Web Scrapping
#import the library used to query a website
import urllib2
#specify the url
wiki = "https://wordpandit.com/29-states-capitals/"
#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)

"""
If you are using the requests library, do:
import requests
page = requests.get(wiki).text

"""

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page) #lxml is the best parser, html5lib is also popular 

#to see the html, you can use "print soup"
# to see indented html content, use
# print soup.prettify()

#in case you do not find the object, please check for right table name
right_table=soup.find('table', class_='alignleft')

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]


for row in right_table.findAll("tr"):
  
    cells = row.findAll('td')
    
    A.append(cells[0].find(text=True))
    B.append(cells[1].find(text=True))
    C.append(cells[2].find(text=True))
    D.append(cells[3].find(text=True))
    E.append(cells[4].find(text=True))
    F.append(cells[5].find(text=True))
    

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A[1:],columns=['S. No.'])
df['States']=B[1:]
df['Capital']=C[1:]
df['Cheif Minister']=D[1:]
df['Political Party']=E[1:]
df['Governer']=F[1:]



print df