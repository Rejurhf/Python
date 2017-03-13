# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 18:07:16 2016
PorzPong.py
@author: Rejurhf
"""

import tkinter
from tkinter import Frame, BOTH, Canvas 

class Pong(Frame):
    canvas = 0
    winHEIGHT = 600;
    winWIDTH = 800;
 
    ball = 0
    paddle1 = 0
    paddle2 = 0
 
    player1Points = 0
    player2Points = 0
    textLabel = 0
    
    ballDX = 2
    ballDY = -2
    paddleSpeed = 15

    
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.parent.bind("<Key>", self.key)
        self.parent.title("Pong")
        self.initUI()
        self.doMove()
 
    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self)
        self.ball = self.canvas.create_oval(400,400,410,410, fill="red")
        self.paddle1 = self.canvas.create_rectangle(0,0,10,50, fill="yellow")
        self.paddle2 = self.canvas.create_rectangle(780,0,790,50, fill="blue")
        self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
        self.canvas.pack(fill=BOTH, expand=1)
        
    def key(self, event):
        if event.char == 'w':
            self.canvas.move(self.paddle1,0,-self.paddleSpeed)
        if event.char == 's':
            self.canvas.move(self.paddle1,0,self.paddleSpeed)
        if event.char == 'o':
            self.canvas.move(self.paddle2,0,-self.paddleSpeed)
        if event.char == 'l':
            self.canvas.move(self.paddle2,0,self.paddleSpeed)
            
    def doMove(self):
        self.canvas.move(self.ball,self.ballDX, self.ballDY)
        if self.canvas.coords(self.ball)[1] <= 0 or self.canvas.coords(self.ball)[3] >= self.winHEIGHT:
            self.ballDY = -self.ballDY
        if self.canvas.coords(self.ball)[0] <= 0 or self.canvas.coords(self.ball)[2] >= self.winWIDTH:
            if self.canvas.coords(self.ball)[0] <= 0:
                self.player2Points+=1
            else:
                self.player1Points+=1
            self.ballDX = -self.ballDX
            self.canvas.delete(self.textLabel)
            self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
            self.canvas.coords(self.ball,self.winWIDTH/2,self.winHEIGHT/2,self.winWIDTH/2+10,self.winHEIGHT/2+10)
        if self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.paddle1)) or self.doCollide(self.canvas.coords(self.ball),self.canvas.coords(self.paddle2)):
            self.ballDX = -self.ballDX
        self.after(10, self.doMove)
        
    def doCollide(self,coords1,coords2):
        return False
        
root = tkinter.Tk()
Pong(root)
root.geometry("800x600")
root.mainloop()