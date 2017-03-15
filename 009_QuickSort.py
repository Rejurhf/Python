# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 12:11:36 2016
009_QuickSort.py
@author: Rejurhf
"""

import time
import random
random.seed()

lis = []
for i in range(0, 100):
    lis.append(random.randint(1, 100))
print(lis)

start_time = time.time()

def quickSort(lis, p, r):
    if p < r:
        q = dzielenie(lis, p, r)
        quickSort(lis, p, q)
        quickSort(lis, q+1, r)
    
    
def dzielenie(lis, p, r):
    x = lis[random.randint(p, r)]
    i = p-1
    j = r+1
    while(True):
        j -= 1
        while(lis[j] > x):
            j -= 1
        i += 1
        while(lis[i] < x):
            i += 1
        if i < j:
            pom = lis[i]
            lis[i] = lis[j]
            lis[j] = pom
        else:
            return j
        
        
start = 0
end = len(lis) - 1
quickSort(lis, start, end)

czas = time.time() - start_time
    
print("--- %s sekund ---" %czas)

print(lis)


  