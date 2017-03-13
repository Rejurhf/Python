# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:43:29 2016
004_RosnacyKwadrat
@author: Rejurhf
"""

import os
import time

x = int(input("Podaj szerokosc: "))
y = int(input("Podaj wysokosc: "))
dlu = 1
ogr = 0
pox = int(x / 2) + 1
poy = int(y / 2) + 1

if x > y:
    ogr = int(y / 2) + 1
else:
    ogr = int(x / 2) + 1

os.system('cls' if os.name=='nt' else 'clear')

for l in range(0, 10):
    for k in range(1, ogr+1):
        dlu = k
        for i in range(0, y):
            for j in range(0, x):
                if( ((pox-dlu)==j and i<=(poy+dlu-2) and i>=(poy-dlu)) 
                or ((pox+dlu-2)==j and i<=(poy+dlu-2) and i>=(poy-dlu))
                or ((poy-dlu)==i and j<=(pox+dlu-2) and j>=(pox-dlu)) 
                or ((poy+dlu-2)==i and j<=(pox+dlu-2) and j>=(pox-dlu)) ):
                    print("x", end="")
                else:
                    print("-", end="")
            print("")
        time.sleep(0.3)
        os.system('cls' if os.name=='nt' else 'clear')
    
    for k in range(ogr-1, 0, -1):
        dlu = k
        for i in range(0, y):
            for j in range(0, x):
                if( ((pox-dlu)==j and i<=(poy+dlu-2) and i>=(poy-dlu)) 
                or ((pox+dlu-2)==j and i<=(poy+dlu-2) and i>=(poy-dlu))
                or ((poy-dlu)==i and j<=(pox+dlu-2) and j>=(pox-dlu)) 
                or ((poy+dlu-2)==i and j<=(pox+dlu-2) and j>=(pox-dlu)) ):
                    print("x", end="")
                else:
                    print("-", end="")
            print("")
        time.sleep(0.3)
        os.system('cls' if os.name=='nt' else 'clear')
                