# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:59:45 2017
018_CiagFibonacciego.py
@author: Rejurhf
"""

e = int(input("Podaj element: "))

def fibonacci(elm):
    if elm == 1:
        return 0
    elif elm == 2:
        return 1
    elif elm > 2:
        return fibonacci(elm-1)+fibonacci(elm-2)
        
print(fibonacci(e))
