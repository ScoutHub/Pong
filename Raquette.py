from tkinter import *
class Raquette:
    def __init__(self,x0,y0,x1,y1,c) -> None:
        self.coordX0 = x0
        self.coordY0 = y0
        self.coordX1 = x1
        self.coordY1 = y1
        self.distanceForMove = 10
        self.raq = c.create_rectangle(self.coordX0,self.coordY0,self.coordX1,self.coordY1,fill="white")
    
    def move(self,c,e,player):
        if(player == 1 ):
            if(e.keysym == "Up"):
                self.coordY0,self.coordY1 = self.coordY0-self.distanceForMove,self.coordY1-self.distanceForMove
                c.coords(self.raq,self.coordX0,self.coordY0,self.coordX1,self.coordY1)
            elif(e.keysym == "Down"):
                self.coordY0,self.coordY1 = self.coordY0+self.distanceForMove,self.coordY1+self.distanceForMove
                c.coords(self.raq,self.coordX0,self.coordY0+self.distanceForMove,self.coordX1,self.coordY1+self.distanceForMove)
        else:
            if(e.keysym == "z"):
                self.coordY0,self.coordY1 = self.coordY0-self.distanceForMove,self.coordY1-self.distanceForMove
                c.coords(self.raq,self.coordX0,self.coordY0,self.coordX1,self.coordY1)
            elif(e.keysym == "x"):
                self.coordY0,self.coordY1 = self.coordY0+self.distanceForMove,self.coordY1+self.distanceForMove
                c.coords(self.raq,self.coordX0,self.coordY0+self.distanceForMove,self.coordX1,self.coordY1+self.distanceForMove)