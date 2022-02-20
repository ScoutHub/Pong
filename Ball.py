import this
from tkinter import *
from Raquette import Raquette
class Ball:
    def __init__(self, c,x0,y0,x1,y1) -> None:
        self.coordX0 = x0
        self.coordY0 = y0
        self.coordX1 = x1
        self.coordY1 = y1
        self.size = 10
        self.dx = 1
        self.dy = 0
        self.ball = c.create_oval(self.coordX0,self.coordY0,self.coordX1,self.coordY1,fill="white")
    
    def move(self,c):
        if(self.dx == True):
            self.coordX0,self.coordX1 = self.coordX0+self.size,self.coordX1+self.size
            c.coords(self.ball,self.coordX0,self.coordY0,self.coordX1,self.coordY1)
            if(self.coordX1 >= 760 ):
                self.dx = False
            
        if(not(self.dx)):
            self.coordX0,self.coordX1 = self.coordX0-self.size,self.coordX1-self.size
            c.coords(self.ball,self.coordX0,self.coordY0,self.coordX1,self.coordY1)
            if(self.coordX1 <= 70 ):
                self.dx = True