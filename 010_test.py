# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:22:04 2016

@author: Rejurhf
"""
"""
import random
random.seed()

lis = []
for i in range(0, 50):
    lis.append(random.randint(1, 50))
print(lis)

lisPom = []
lisPom.append(0)
lisPom.extend(lis)
print(lisPom)
"""
class cos:
    def __init__(self, dane):
        self.dane = dane
        
        
lis = []
lis.append(cos("a"))
lis.append(cos("d"))
lis.append(cos("c"))
lis.append(cos("b"))

lis2 = []
lis2.extend(lis)
lis.append(cos("de"))


for i in lis:
    if i not in lis2:
        lis2.append(i)
        
print(lis)