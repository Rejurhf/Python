# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 10:45:41 2016
013_DrzewoGenealogiczne.py
@author: Rejurhf
"""

class Osoba:
    def __init__(self, dane):
        self.dane = dane
        self.mal = None
        self.dziecko = []
        self.rodzice = []
        
    def __str__(self):
        return str(self.dane)
        

class Drzewo:
    rodz_war = 0
    mal_war = 1
    dziec_war = 2
    
    def __init__(self):
        self.pocz = None
        self.rozm = 0
        
    def dodaj(self, dane, os, rel):
        if self.rozm == 0:
            o = Osoba(dane)
            self.pocz = o
            self.rozm += 1
        else:
            o = self.znajdz(os)
            if o == -1:
                print("Nie znaleziono relacji")
                return
            if rel == self.dziec_war:
                now_o = Osoba(dane)
                o.dziecko.append(now_o)
                self.rozm += 1
                now_o.rodzice.append(o)
            elif rel == self.mal_war:
                if o.mal == None:
                    now_o = Osoba(dane)
                    o.mal = now_o
                    now_o.mal = o
                else:
                    print("Blad")
            elif rel == self.rodz_war:
                now_o = Osoba(dane)
                now_o.dziecko.append(o)
                o.rodzice.append(now_o)
                if self.pocz.dane == o.dane:
                    self.pocz = now_o          
                    
    def usun(self, os):
        o = self.znajdz(os)
        if o == -1:
                print("Nie znaleziono relacji")
                return
        #for i in o.rodzice:
            
                    
    def znajdz(self, os):
        stos = []
        stos.append(self.pocz)
        flag = True
        while len(stos) > 0 or flag == False:
            if flag:
                o = stos.pop(0)
            if o.dane == os:
                return o
            for i in o.dziecko:
                flaga = True
                for j in stos:
                    if j.dane == i.dane:
                        flaga = False
                        break
                if flaga:
                    stos.append(i)
            if o.mal != None and flag == True:
                o = o.mal
                flag = False
            else: flag = True
        return -1
                    
    def wypisz(self):
        stos = []
        stos.append(self.pocz)
        flag = True
        while len(stos) > 0 or flag == False:
            if flag:
                o = stos.pop(0)
            print("%s" %o.dane)
            for i in o.dziecko:
                flaga = True
                for j in stos:
                    if j.dane == i.dane:
                        flaga = False
                        break
                if flaga:
                    stos.append(i)
            if o.mal != None and flag == True:
                o = o.mal
                flag = False
            else: flag = True                    
   
                    
lis = Drzewo()
lis.dodaj("jakub", "lukasz", 2)
lis.dodaj("lukasz", "jakub", 0)
lis.dodaj("ola", "jakub", 1)
lis.dodaj("karol", "ola", 2)
lis.dodaj("karol", "jakub", 2)
lis.dodaj("tomasz", "jakub", 2)
lis.dodaj("tomasz", "ola", 2)
lis.dodaj("ewa", "karol", 1)
lis.usun("tomasz")
lis.wypisz()



