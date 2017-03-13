# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:46:45 2016
008_SortKop.py
@author: Rejurhf
"""

import time
import random
random.seed()

lis = []
lisKop = []
lis.append(0)
for i in range(0, 700):
    lis.append(random.randint(1, 1000))
print(lis)

start_time = time.time()

for i in range(2, len(lis)):
    j = i
    while(j > 1):
        if lis[j] < lis[int(j/2)]:
            pom = lis[int(j/2)]
            lis[int(j/2)] = lis[j]
            lis[j] = pom
            j = int(j/2)
            continue
        break
    
while(len(lis)>1):
    pom = lis[1]
    lis[1] = lis[len(lis)-1]
    lis[len(lis)-1] = pom
    lisKop.append(lis.pop(len(lis)-1))
    j = 1
    while(j <= int((len(lis)-1)/2)):
        flag = True
        if 2*j == len(lis)-1:
            if lis[j] > lis[len(lis)-1]:
                pom = lis[j]
                lis[j] = lis[len(lis)-1]
                lis[len(lis)-1] = pom
            break
        elif lis[2*j] > lis[2*j+1] and lis[2*j+1] < lis[j]:
            pom = lis[j]
            lis[j] = lis[2*j+1]
            lis[2*j+1] = pom
            j = (2 * j) + 1
            flag = False
        elif lis[2*j] < lis[2*j+1] and lis[2*j] < lis[j]:
            pom = lis[j]
            lis[j] = lis[2*j]
            lis[2*j] = pom
            j = 2 * j
            flag = False
        elif lis[2*j] == lis[2*j+1] and lis[2*j] < lis[j]:
            pom = lis[j]
            lis[j] = lis[2*j]
            lis[2*j] = pom
            j = 2 * j
            flag = False
        if flag == True:
            break
    
czas = time.time() - start_time
    
print("--- %s sekund ---" %czas)
        
print(lisKop)
"""
war = True
for i in range(0, len(lisKop)-1):
    if lisKop[i] > lisKop[i+1]:
        print(i)
        war = False
        break
if(war):
    print("Dobrze")
else:
    print("Zle")
"""
