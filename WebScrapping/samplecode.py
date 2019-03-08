from bs4 import BeautifulSoup
import urllib.request
import unicodedata
import pandas as pd



#specify the url
wiki = "https://simple.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib.request.urlopen(wiki)

soup = BeautifulSoup(page,features="lxml")



rtable=soup.find('table',class_='wikitable sortable plainrowheaders')
print(rtable)
A=[] 
B=[]
C=[] 
D=[] 
E=[] 
F=[]
G=[]


for row in rtable.find_all("tr"):
    
    cells=row.findAll('td')
    states=row.findAll('th')
    
    if(len(cells)==6):
        A.append(cells[0].text)
        B.append(states[0].text)
        C.append(cells[1].text)
        D.append(cells[2].text)
        E.append(cells[3].text)
        F.append(cells[4].text)
        G.append(cells[5].text)
        
        
df=pd.DataFrame(A,columns=['Numbers'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G

print(df)