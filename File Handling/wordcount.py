# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:06:32 2019

@author: harshvardhan
"""

file = open("romeo.txt","rt")

wordcount=0
lines=0
character=0
un=0
unique={}
chars=[]
words=[]
for i in file:
    #To calculate the no of words
    x=i.split()
    words.extend(x)
    #To calculate the no of lines    
    lines+=1
    #To calculate the no of chars    
    chars.extend(i)
    

for i in words:
    if i not in unique:
        unique[i]=1
    else:
        unique[i]+=1

wordcount=len(words)
character=len(chars)    
un=len(unique)
print("Number of words are : ",wordcount)
print("Number of chars are : ",lines)
print("Number of characters : ",character)
print("Number of unique words are : ",un)

