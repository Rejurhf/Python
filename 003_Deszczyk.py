# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 18:14:05 2016
003_Deszczyk
@author: Rejurhf
"""
import random
import os
import time
random.seed()

wie = int(input("Podaj liczbe wierszy: ")) 
kol = int(input("Podaj liczbe kolumn: "))
lis = []                                            #deklaracja listy przechowujacej pozycje kropel

for i in range(0, wie):                             #towrzenie listy
    lis.append(kol)
    
os.system('cls')                                    #czyszczenie terminala

for k in range(0, 50):                              #ilosć tablic
    los = random.randint(0, kol-1)                  #losowanie pozycji gornej kropli
    
    for m in range((wie-2), -1, -1):                #przesuniecie pozycji kropli o 1
        lis[m+1] = lis[m]
    lis[0] = los                                    #nadanie pozycji gornej kropli
    
    for i in range(0, wie):                         #tworzenie tablicy
        for j in range(0, kol):
            if(j == lis[i]):                        #jeżeli index wrowny pozycji kropli wypisać "x"
                print("x", end="")
            else:
                print("-", end="")                  #w przeciwnym wypadku "-"
        print("")
    print("")
    time.sleep(0.3)                                 #przerwa
    os.system('cls')  #czyszczenie tarminala
        
