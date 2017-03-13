# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:14:52 2017
014_SitoEratostelesa.py
@author: Rejurhf
"""
import math

z = int(input("Podaj najwieksza liczbe jaka chcesz sprawdzic czy jest pierwsza: "))
s = int(math.sqrt(z))
lst = [True]*(z+1)
lst[0] = False
lst[1] = False

for i in range(2, s+1):
    if lst[i] == True:
        for j in range(2, int(z/i)+1):
            lst[j*i] = False

c = 1
for i in range(2, z+1):
    if lst[i] == True:
        print("%d. %d" %(c, i))
        c += 1