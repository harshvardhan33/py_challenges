# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 10:11:13 2019

@author: harshvardhan
"""

class Employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    
    
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    