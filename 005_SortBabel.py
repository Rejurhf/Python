# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 17:44:30 2016
005_SortBabel.py
@author: Rejurhf
"""

import time
import random
random.seed()

lis = []
for i in range(0, 700):
    lis.append(random.randint(1,1000))
print(lis)

start_time = time.time()

for i in range(0, len(lis)):
    flag = False
    for j in range(0, len(lis)-i-1):
        if lis[j] > lis[j+1]:
            pom = lis[j]
            lis[j] = lis[j+1]
            lis[j+1] = pom
            flag = True
    if flag == False:
        break
    
czas = time.time() - start_time
    
print("--- %s sekund ---" %czas)
    
print(lis)