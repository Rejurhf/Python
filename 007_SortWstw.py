# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 18:27:42 2016
007_SoreWstw.py
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

for i in range(1, len(lis)):
    pom = lis[i]
    for j in range(0, i):
        if pom < lis[j]:
            for k in range(i, j, -1):
                lis[k] = lis[k-1]
            lis[j] = pom
            break
      
czas = time.time() - start_time
    
print("--- %s sekund ---" %czas)
        
print(lis)