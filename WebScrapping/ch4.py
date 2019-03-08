# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 12:09:16 2019

@author: harshvardhan
"""

import pandas as pd
from selenium import webdriver

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#driver=webdriver.Chrome("C:\\Users\\harshvardhan\\Downloads\\chromedriver_win32")#THIS IS UPDATED IN LOWER LINE 
driver = webdriver.Chrome(executable_path=r'C:/Users/harshvardhan/Downloads/chromedriver_win32/chromedriver.exe')

driver.get(wiki)

rt=driver.find_element_by_class_name('wikitable sortable plainrowheaders')
A=[] 
B=[]
C=[] 
D=[] 
E=[] 
F=[]
G=[]

for row in rt.find_elements_by_tag_name("tr"):
    cells = rt.find_elements_by_tag_name("td")
    states=rt.find_elements_by_tag_name("th")
    
    if len(cells)==5: #Only extract table body not heading
        A.append(str(cells[0].text))
        B.append(str(states[1].text))
        C.append(str(unicodedata.normalize('NFKD', cells[1].text).encode('ascii','ignore')))        
        D.append(str(unicodedata.normalize('NFKD', cells[2].text).encode('ascii','ignore')))
        E.append(str(cells[3].text))
        F.append(str(unicodedata.normalize('NFKD', cells[4].text).encode('ascii','ignore')))
        


df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=A
df['Legislative_Capital']=C
df['Judiciary_Capital']=D
df['Year_Capital']=E
df["Former_Capital"] = F

print(df)

driver.quit()