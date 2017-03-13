# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:56:22 2017
004_RosnacyKwadrat_v2
@author: Rejurhf
"""

import os
import time

rozm = int(input("Podaj dlugosc boku: "))
os.system('cls')

for i in range(0, 50):
    for j in range(0, int(rozm/2)+1):
        x = j*2 + 1
        p = int((rozm-x)/2)
        for k in range(0, rozm):
            if k == p or k == rozm-p-1:
                w = "-"*p + "x"*x + "-"*p
            elif k > p and k < rozm-p-1:
                w = "-"*p + "x" + " "*(x-2) + "x" + "-"*p
            else:
                w = "-" * rozm
            print(w)
        time.sleep(0.2)
        os.system('cls')
    for j in range(int(rozm/2), -1, -1):
        x = j*2 + 1
        p = int((rozm-x)/2)
        for k in range(0, rozm):
            if k == p or k == rozm-p-1:
                w = "-"*p + "x"*x + "-"*p
            elif k > p and k < rozm-p-1:
                w = "-"*p + "x" + " "*(x-2) + "x" + "-"*p
            else:
                w = "-" * rozm
            print(w)
        time.sleep(0.2)
        os.system('cls')