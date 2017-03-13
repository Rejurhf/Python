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
for i in range(0, 700):
    lis.append(random.randint(1, 1000))
print(lis)

start_time = time.time()

def quickSort(lis, a, z):
    s = a
    k = z
    while(a < z):
        if lis[a] > lis[s]:
            while(lis[z] > lis[s]):
                if z == a:
                    break
                z = z - 1
            if a == z:
                break
            elif a < z:
                pom = lis[a]
                lis[a] = lis[z]
                lis[z] = pom
        if a == z:
            break
        else:
            a = a + 1
    if(z != k):
        pom = lis[s]
        lis[s] = lis[z-1]
        lis[z-1] = pom
    else:
        for i in range(s+1, k+1):
            if lis[s] != lis[i]:
                pom = lis[i]
                lis[i] = lis[s]
                lis[s] = pom 
                return s-1
        return len(lis)
    return z-1

def sortBomb(lis, d, w):
    for i in range(d, w):
        flag = False
        for j in range(d, w):
            if lis[j] > lis[j+1]:
                pom = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = pom
                flag = True
        if flag == False:
            break
    
def dzielenie(lis, b, y):
    t = quickSort(lis, b, y)
    if t == len(lis):
        return
    if (t-b) > 9 and (y-t) > 9:
        dzielenie(lis, b, t-1)
        dzielenie(lis, t+1, y)
    if (t-b) > 9 and (y-t) <= 9:
        dzielenie(lis, b, t-1)
        sortBomb(lis, t+1, y)
    if (t-b) <= 9 and (y-t) > 9:
        sortBomb(lis, b, t-1)
        dzielenie(lis, t+1, y)
    if (t-b) <= 9 and (y-t) <= 9:
        sortBomb(lis, b, t-1)
        sortBomb(lis, t+1, y)
        
c = 0
x = len(lis) - 1
dzielenie(lis, c, x)

czas = time.time() - start_time
    
print("--- %s sekund ---" %czas)

print(lis)

war = True
for i in range(0, len(lis)-1):
    if lis[i] > lis[i+1]:
        print(i)
        war = False
        break
if(war):
    print("Dobrze")
else:
    print("Zle")

  