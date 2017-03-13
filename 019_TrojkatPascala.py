# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:07:44 2017
019_TrojkatPascala.py
@author: Rejurhf
"""

x = int(input("X: "))
y = int(input("Y: "))

def pascal(x, y):
    if x == 1:
        return 1
    elif x == y:
        return 1
    else:
        return pascal(x, y-1) + pascal(x-1, y-1)
        
print(pascal(x, y))