from random import randint
from tkinter import *
from Raquette import Raquette
class Ball:
    def __init__(self, c,x0,y0,x1,y1) -> None:
        self.coordX0 = x0
        self.coordY0 = y0
        self.coordX1 = x1
        self.coordY1 = y1
        self.size = 15
        self.dx = 1
        self.dy = 0
        self.angle = 0
        self.nbOfTouch = 0
        self.firstTouch = False
        self.ball = c.create_oval(self.coordX0,self.coordY0,self.coordX1,self.coordY1,fill="white")
    
    def move(self,c,p1,p2):
        if(self.dx == True):
            self.coordX0,self.coordX1 = self.coordX0+self.size,self.coordX1+self.size
            self.coordY0,self.coordY1 = self.coordY0+self.angle,self.coordY1+self.angle
            c.coords(self.ball,self.coordX0,self.coordY0,self.coordX1,self.coordY1)
            if(self.coordY0 >= p2.coordY0 and self.coordY0 <= p2.coordY1 and self.coordX1 >= p2.coordX0):
                if(self.firstTouch == False):
                    self.firstTouch = True
                    self.angle = randint(-10,10)
                    if(self.angle < 2 and self.angle > -2):
                        self.angle = randint(-10,10)
                    self.coordY0,self.coordY1 = self.coordY0+self.angle,self.coordY1+self.angle
                    self.nbOfTouch += 1
                self.dx = False
                self.nbOfTouch += 1
                if(self.nbOfTouch % 5 == 0):
                    self.size += 5
            elif(self.coordY0 <= 50):
                self.angle = abs(self.angle)
            elif(self.coordY0 >= 440):
                self.angle = -(self.angle)
            elif(self.coordX1 >= 780):
                p1.score += 1
                self.nbOfTouch = 0
                self.coordX0,self.coordY0,self.coordX1,self.coordY1,self.angle = 460,250,470,260,0
                self.firstTouch = False
                self.size = 15
                
        elif(not(self.dx)):
            self.coordX0,self.coordX1 = self.coordX0-self.size,self.coordX1-self.size
            self.coordY0,self.coordY1 = self.coordY0+self.angle,self.coordY1+self.angle
            c.coords(self.ball,self.coordX0,self.coordY0,self.coordX1,self.coordY1)
            if(self.coordY0 >= p1.coordY0 and self.coordY0 <= p1.coordY1 and self.coordX0 <= p1.coordX1):
                if(self.firstTouch == False):
                    self.firstTouch = True
                    self.angle = randint(-10,10)
                    if(self.angle < 2 and self.angle > -2):
                        self.angle = randint(-10,10)
                    self.coordY0,self.coordY1 = self.coordY0+self.angle,self.coordY1+self.angle
                    self.nbOfTouch += 1
                self.dx = True
                self.nbOfTouch += 1
                if(self.nbOfTouch % 5 == 0):
                    self.size += 5
            elif(self.coordY0 <= 50):
                self.angle = abs(self.angle)
            elif(self.coordY1 >= 440):
                self.angle = -(self.angle)
            elif(self.coordX1 <= 40):
                p2.score += 1
                self.coordX0,self.coordY0,self.coordX1,self.coordY1,self.angle = 460,250,470,260,0
                self.firstTouch = False
                self.dx = False
                self.nbOfTouch = 0
                self.size = 15