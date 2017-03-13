# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:22:07 2017
003_Deszczyk_v2.py
@author: Rejurhf
"""

import random
import os
import time
random.seed()

wrs = int(input("Podaj ilosc wierszy: "))
kol = int(input("Podaj ilosc kolumn: "))
lst = []
for i in range(0, wrs):
    w = " " * kol
    lst.append(w)

for i in range(0, 500):
    r = random.randint(1, kol)
    w = " "*(r-1) + "x" + " "*(kol-r)
    """
    r1 = random.randint(1, kol)
    r2 = random.randint(1, kol)
    if r2 > r1:
        tmp = r1
        r1 = r2
        r2 = tmp
    elif r1 == r2:
        r1 += 1
    w = " "*(r2-1) + "x" + " "*(r1-r2-1) + "x" + " "*(kol-r2)
    """
    lst.pop(0)
    lst.append(w)
    for j in range(wrs-1, -1, -1):
        print(lst[j])
    time.sleep(0.3)
    os.system('cls')