# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:11:05 2016
Raport_Mateusz_Ziomek.py
@author: Rejurhf
"""

import random
random.seed()

lis = []
for i in range(0, 50):
    lis.append(random.randint(1, 500))
print(lis)

lisPom = lis

'''
Sortowanie QuickSort
'''

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
    if (t-b) > 5 and (y-t) > 5:
        dzielenie(lis, b, t-1)
        dzielenie(lis, t+1, y)
    if (t-b) > 5 and (y-t) <= 5:
        dzielenie(lis, b, t-1)
        sortBomb(lis, t+1, y)
    if (t-b) <= 5 and (y-t) > 5:
        sortBomb(lis, b, t-1)
        dzielenie(lis, t+1, y)
    if (t-b) <= 5 and (y-t) <= 5:
        sortBomb(lis, b, t-1)
        sortBomb(lis, t+1, y)
        
c = 0
x = len(lis) - 1
dzielenie(lis, c, x)
print(lis)


'''
Sortowanie przez Kopcowanie
'''

lis = []
lis.append(0)
lis.extend(lisPom)


lisKop = []

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
    
print(lisKop)

'''
Sortowanie przez Wstawianie
'''

lis = lisPom

for i in range(1, len(lis)):
    pom = lis[i]
    for j in range(0, i):
        if pom < lis[j]:
            for k in range(i, j, -1):
                lis[k] = lis[k-1]
            lis[j] = pom
            break
            
print(lis)

'''
Sortowanie przez Wybieranie
'''

lis = lisPom

for i in range(0, len(lis)):
    a = i
    for j in range(i+1, len(lis)):
        if  lis[a] > lis[j]:
            a = j
    pom = lis[a]
    lis[a] = lis[i]
    lis[i] = pom

print(lis)

'''
Sortowanie Babelkowe
'''

lis = lisPom

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
    
print(lis)