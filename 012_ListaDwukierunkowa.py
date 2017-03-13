# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:23:20 2016
012_ListaDwukierunkowa.py
@author: Mateusz Ziomek
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
    def __str__(self):
        return str(self.data)
 
class UnidirectionalList:
    def __init__(self):
        self.head = None
        self.size = 0
 
    def addEnd(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.size += 1
        else:
            n = self.head
            while n.next != None:
                n = n.next
            new_node = Node(data)
            n.next = new_node
            n.next.prev = n
            self.size += 1
            
    def addBgn(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.size += 1
        else:
            n = self.head
            new_node = Node(data)
            new_node.next = n
            n.prev = new_node
            self.size += 1
            #tmp = self.head
            self.head = new_node
            #new_node = tmp
            
    def addMdl(self, data, poz):
        if poz > self.size+1 or poz < 1:
            print("Pozycja %d poza zakresem(dlugosc listy: %d). (%s)" %(poz, self.size, data))
            return
        elif poz == 1: 
            self.addBgn(data)
            return
        elif poz == self.size+1: 
            self.addEnd(data)
            return
        if not self.head:
            n = Node(data)
            self.head = n
            self.size += 1
        else:
            n = self.head  
            for i in range(1, poz-1):
                n = n.next
            new_node = Node(data)
            new_node.next = n.next
            new_node.prev = n
            n.next.prev = new_node
            n.next = new_node
            self.size += 1
            
    def remEnd(self):
        if not self.head:
            print("Lista jest pusta, nie ma czego usowac")
        elif self.size == 1:
            self.head = None
            self.size -= 1
        else:
            n = self.head
            while n.next.next != None:
                n = n.next
            n.next = None
            self.size -= 1
            
    def remBgn(self):
        if not self.head:
            print("Lista jest pusta, nie ma czego usowac")
        elif self.size == 1:
            self.head = None
            self.size -= 1
        else:
            n = self.head
            self.head = n.next
            n.next.prev = None
            self.size -= 1
 
    def printList(self):
        n = self.head
        i = 1
        print("Lista od poczatku:")
        while n:
            print("%d %s"%(i, n))
            n = n.next
            i += 1
            
    def printListEnd(self):
        n = self.head
        while n.next != None:
            n = n.next
        i = 1
        print("Lista od konca:")
        while n:
            print("%d %s"%(i, n))
            n = n.prev
            i += 1
            
    def printBestScore(self):
        n = self.head
        bestPer = ""
        score = 0
        while n:
            person = str(n)
            ind = person.index(" ")+1
            if score < int(person[ind:]):
                score = int(person[ind:])
                bestPer = person
            n = n.next
        print("Najlepszt wynik usyskał %s" %bestPer)

ll = UnidirectionalList()
ll.remBgn()
ll.addBgn("Nowak 71")
ll.remEnd()
ll.addBgn("Kowalski 27")
ll.addEnd("Piotrowski 92")
ll.addBgn("Kaczmarek 88")
ll.addMdl("Lewandowski 63", 1)
ll.addMdl("Kowalczyk 94", 4)
ll.addMdl("Jankowski 55", 3)
ll.addMdl("Wojciechowski 26", 15)
ll.addMdl("Kwiatkowski 67", 6)
ll.addBgn("Mazur 59")
ll.addMdl("Krawczyk 18", 3)
ll.remBgn()
ll.addEnd("Grabowski 33")
ll.addEnd("Nowakowski 49")
ll.addEnd("Michalski 65")
ll.addBgn("Nowicki 68")
ll.addEnd("Michalak 99")
ll.remEnd()
ll.addBgn("Adamczyk 73")
ll.addEnd("Dudek 88")
ll.addMdl("Wieczorek 59", 10)
ll.addEnd("Majewski 5")
ll.addBgn("Olszewski 21")
ll.addEnd("Jaworski 39")
ll.addBgn("Malinowski 48")
ll.addBgn("Pawlak 55")
ll.addMdl("Witkowski 66", 15)
ll.addEnd("Walczak 78")
ll.addBgn("Rutkowski 85")
ll.addMdl("Sikora 9", 24)
ll.remEnd()

ll.printList()
print("  -----  ")
ll.printListEnd()
print("  -----  ")
ll.printBestScore()