# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 10:56:52 2019

@author: harshvardhan
"""

import time
start_time = time.time()

file = open("james_joyce_ulysses.txt","rt",encoding="utf8")
file1 = open("metamorphosis_kafka.txt","rt",encoding="utf8")
file2 = open("sons_and_lovers_lawrence.txt","rt",encoding="utf8")

wordcount=0
wordcount1=0
wordcount2=0
lines=0
lines1=0
lines2=0
character=0
character1=0
character2=0
un=0
un1=0
un2=0
unique={}
unique1={}
unique2={}
chars=[]
chars1=[]
chars2=[]
words=[]
words1=[]
words2=[]


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

for i in file1:
    #To calculate the no of words
    x=i.split()
    words1.extend(x)
    #To calculate the no of lines    
    lines1+=1
    #To calculate the no of chars    
    chars1.extend(i)
for i in words1:
    if i not in unique1:
        unique1[i]=1
    else:
        unique1[i]+=1

for i in file2:
    #To calculate the no of words
    x=i.split()
    words2.extend(x)
    #To calculate the no of lines    
    lines2+=1
    #To calculate the no of chars    
    chars2.extend(i)
for i in words2:
    if i not in unique2:
        unique2[i]=1
    else:
        unique2[i]+=1



wordcount=len(words)
character=len(chars)    
un=len(unique)
print("Number of words are : ",wordcount)
print("Number of chars are : ",lines)
print("Number of characters : ",character)
print("Number of unique words are : ",un)


print("* "*40)


wordcount1=len(words1)
character1=len(chars1)    
un1=len(unique1)
print("Number of words are : ",wordcount1)
print("Number of chars are : ",lines1)
print("Number of characters : ",character1)
print("Number of unique words are : ",un1)




print("* "*40)



wordcount2=len(words2)
character2=len(chars2)    
un2=len(unique2)
print("Number of words are : ",wordcount2)
print("Number of chars are : ",lines2)
print("Number of characters : ",character2)
print("Number of unique words are : ",un2)


a=set(unique.keys())
b=set(unique1.keys())
c=set(unique2.keys())

listuly=a - (b | c) 
listcommon= a & b & c
print(listcommon)


print ("\nMy program took :", time.time() - start_time, "to run")
