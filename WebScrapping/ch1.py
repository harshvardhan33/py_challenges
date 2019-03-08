# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:27:20 2019

@author: harshvardhan
"""

from bs4 import BeautifulSoup
import urllib.request




#specify the url
wiki = "https://simple.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib.request.urlopen(wiki)

soup = BeautifulSoup(page,features="lxml")
divc=soup.find('h1',class_="firstHeading")
print('\n'+divc.text+'\n')
"""----------------------------OR WE CAN USE----------------------------------"""
#divc=soup.find_all('div')
#print(divc[2].h1.text)
#print(divc.text)

divc1=soup.find('div',class_="toctitle")
print(divc1.text)

divc1_contents=soup.find('ul')
print(divc1_contents.text)


divc2=soup.find_all('p')
print(divc2[0].text+"\n"+divc2[1].text)
