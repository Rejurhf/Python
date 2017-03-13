# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 23:07:08 2017
017_LiczbyZaprzyjaznione.py
@author: Rejurhf
"""

z = int(input('P: '))
lst = []

for i in range(2, z+1):
    s = 0
    for j in range(1, int(i/2)+1):
        if i % j == 0:
            s += j
    lst.append(s)

for j in range(0, len(lst)):
    lstp = []
    if lst[j] != 0:
        for i in range(j, len(lst)):
            if lst[j] == lst[i]:
                lstp.append(i+2)
                if i > j: lst[i] = 0
        lst[j] = 0
    if len(lstp) > 1: print(lstp)