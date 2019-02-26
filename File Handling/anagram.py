# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 08:05:50 2019

@author: harshvardhan
"""

n1=input("Enter A Word You want to check anagram for :").upper()

dict1={}

for i in n1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
print(dict1)    

inp=int(input("Enter The Number of Words you want to enter :"))
dict2={}
for i in range(inp):
    n2=input("Enter A Word :").upper()
    for j in n2:
        if j not in dict2:
            dict2[j]=1
        else:
            dict2[j]+=1
    
    if(dict1==dict2):
        print("Yes Anagram")
        with open("anagram.txt","a") as file:
            file.writelines(n2+"\n")
    dict2.clear()

    
    

        



    