# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:14:18 2019

@author: hp
"""

def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def main():
    print("Enter the number :")
    x=int(input())
    y=fact(x)
    print(y)
    
if __name__=='__main__':
    main()