from tkinter import *
class Raquette:
    def __init__(self,x0,y0,x1,y1,c,f) -> None:
        self.coordX0 = x0
        self.coordY0 = y0
        self.coordX1 = x1
        self.coordY1 = y1
        self.distanceForMove = 10
        self.raq = c.create_rectangle(self.coordX0,self.coordY0,self.coordX1,self.coordY1,fill="white")
        self.flag = f
        self.score = 0
    
    def setFlag(self,e,player):
        if(player == 1):
            if(e.keysym == "Up"):
                self.flag=1
            elif(e.keysym == "Down"):
                self.flag=-1
        else:
            if(e.keysym == "z"):
                self.flag=1
            elif(e.keysym == "x"):
                self.flag=-1
    
    def move(self,c,player):
        if(player == 1):
            if(self.flag == 1 and self.coordY0 > 50):
                self.coordY0,self.coordY1 = self.coordY0-self.distanceForMove,self.coordY1-self.distanceForMove
                c.coords(self.raq,self.coordX0,self.coordY0,self.coordX1,self.coordY1)
            elif(self.flag == -1 and self.coordY1 < 440):
                self.coordY0,self.coordY1 = self.coordY0+self.distanceForMove,self.coordY1+self.distanceForMove
                c.coords(self.raq,self.coordX0,self.coordY0+self.distanceForMove,self.coordX1,self.coordY1+self.distanceForMove)
        else:
            if(self.flag == 1 and self.coordY0 > 50):
                self.coordY0,self.coordY1 = self.coordY0-self.distanceForMove,self.coordY1-self.distanceForMove
                c.coords(self.raq,self.coordX0,self.coordY0,self.coordX1,self.coordY1)
            elif(self.flag == -1 and self.coordY1 < 440):
                self.coordY0,self.coordY1 = self.coordY0+self.distanceForMove,self.coordY1+self.distanceForMove
                c.coords(self.raq,self.coordX0,self.coordY0+self.distanceForMove,self.coordX1,self.coordY1+self.distanceForMove)
