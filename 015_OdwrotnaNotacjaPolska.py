# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:49:00 2017
015_OdwrotnaNotacjaPolska.py
@author: Rejurhf
"""

ciag = str(input("Podaj wyrazenie: "))
lst = []
p = 0

while p < len(ciag):
    e = ''
    l = 0
    while ciag[p+l] != ' ' and p+l < len(ciag)-1:
        l += 1
    e = ciag[p:(p+l)]
    if p+l == len(ciag)-1:
        e = ciag[p:]
    p += l + 1
    if e == '+':
        a = lst[len(lst)-2]
        b = lst.pop(len(lst)-1)
        lst[len(lst)-1] = a + b
    elif e == '-':
        a = lst[len(lst)-2]
        b = lst.pop(len(lst)-1)
        lst[len(lst)-1] = a - b
    elif e == '*':
        a = lst[len(lst)-2]
        b = lst.pop(len(lst)-1)
        lst[len(lst)-1] = a * b
    elif e == '/':
        a = lst[len(lst)-2]
        b = lst.pop(len(lst)-1)
        lst[len(lst)-1] = a / b
    else:
        lst.append(int(e))
print(lst[0])    