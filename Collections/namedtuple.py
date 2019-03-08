# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:29:07 2019

@author: harshvardhan
"""

from collections import namedtuple
Point = namedtuple('ForskLabs','x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
print (dot_product)