# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:22:25 2016
002_10doDowolny
@author: Rejurhf
"""

a = int(input("Podaj liczbe w systemie dziesietnym: "))
s = int(input("Wybierz system na ktory chcesz przejsc: "))
w = ""
l = 0

while(a > 0):
    l = a % s
    w = str(l) + w
    a = int(a / s)

print(w)   
