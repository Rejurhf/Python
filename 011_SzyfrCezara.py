# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 19:08:36 2016
011_SzyfrCezara.py
@author: Rejurhf
"""
import random

random.seed()
ciag = input("Podaj wiadomosc: ")
prze = int(input("Podaj liczbe przestawienia: "))
klucz = input("Podaj klucz: ")

def uprosc(ciag):
    ciag = ciag.lower()
    ciag = ciag.replace(" ","")
    if ciag.isalpha() == False:
        for i in range(0, 10):
            ciag = ciag.replace(str(i), "")
    return ciag

def genAlf():
    lis = []
    alf = ""
    for i in range(97, 123):
        lis.append(i)
    for i in range(1, len(lis)-1):
        a = random.randint(i, len(lis)-1)
        pom = lis[i]
        lis[i] = lis[a]
        lis[a] = pom
    for i in range(0, len(lis)):
        alf += chr(lis[i])
    return alf

def cezar(ciag, prze):
    pomCiag = ''
    for i in range(0, len(ciag)):
        if prze <= 122 - ord(ciag[i]):
            pomCiag += chr(ord(ciag[i]) + prze)
        else:
            a = prze - (122 - ord(ciag[i]))
            pomCiag += chr(96 + a)
    return pomCiag
    
def deCezar(ciag, prze):
    pomCiag = ''
    for i in range(0, len(ciag)):
        if prze <= ord(ciag[i]) - 97:
            pomCiag += chr(ord(ciag[i]) - prze)
        else:
            a = prze - (ord(ciag[i])-97)
            pomCiag += chr(123 - a)
    return pomCiag

def przestawieniowy(ciag, alf):
    ciag2 = ''
    for i in range(0, len(ciag)):
        ciag2 += alf[ord(ciag[i]) - 97]
    return ciag2
    
def dePrzestawieniowy(ciag, alf):
    ciag2 = ''
    alfP = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0, len(ciag)):
        ciag2 += alfP[alf.index(ciag[i])]
    return ciag2

def zKluczem(ciag, klucz):
    lisK = []
    lisC = []
    a = 0
    for i in range(0, len(klucz)):
        lisK.append(ord(klucz[i]) - 96)
    for i in range(0, len(ciag)):
        if lisK[a] <= 122-ord(ciag[i]):
            lisC.append(ord(ciag[i]) + lisK[a])
        else:
            b = lisK[a] - (122-ord(ciag[i]))
            lisC.append(96 + b)
        a += 1
        if a == len(klucz): a = 0
    ciag = ''
    for i in range(0, len(lisC)):
        ciag += chr(lisC[i])
    return ciag
    
def deZKluczem(ciag, klucz):
    lisK = []
    lisC = []
    a = 0
    for i in range(0, len(klucz)):
        lisK.append(ord(klucz[i]) - 96)
    for i in range(0, len(ciag)):
        if lisK[a] <= ord(ciag[i])-97:
            lisC.append(ord(ciag[i]) - lisK[a])
        else:
            b = lisK[a] - (ord(ciag[i])-97)
            lisC.append(123 - b)
        a += 1
        if a == len(klucz): a = 0
    ciag = ''
    for i in range(0, len(lisC)):
        ciag += chr(lisC[i])
    return ciag

ciag = uprosc(ciag)
ciag = cezar(ciag, prze)
print("Cezar: %s" %ciag)
ciag = deCezar(ciag, prze)
print("DeCezar: %s" %ciag)

alf = genAlf()
print("Alfabet: %s" %alf)
ciag = przestawieniowy(ciag, alf)
print("Przestawieniowy: %s" %ciag)
ciag = dePrzestawieniowy(ciag, alf)
print("DePrzestawieniowy: %s" %ciag)

klucz = uprosc(klucz)
ciag = zKluczem(ciag, klucz)
print("ZKluczem: %s" %ciag)
ciag = deZKluczem(ciag, klucz)
print("DeZKluczem: %s" %ciag)