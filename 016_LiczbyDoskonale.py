# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:44:03 2017
016_LiczbyDoskonale.py
@author: Rejurhf
"""

z = int(input('P: '))

for i in range(2, z+1):
    s = 0
    for j in range(1, int(i/2)+1):
        if i % j == 0:
            s += j
    if s == i:
        print(s)