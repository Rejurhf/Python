# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 18:08:50 2016
006_SortWybr.py
@author: Rejurhf
"""

import time
import random 
random.seed()

lis = []
for i in range(0, 700):
    lis.append(random.randint(1, 1000))
print(lis)

start_time = time.time()

for i in range(0, len(lis)):
    a = i
    for j in range(i+1, len(lis)):
        if  lis[a] > lis[j]:
            a = j
    pom = lis[a]
    lis[a] = lis[i]
    lis[i] = pom

czas = time.time() - start_time
    
print("--- %s sekund ---" %czas)

print(lis)