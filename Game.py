from tkinter import *
import tkinter.font
from Raquette import *
from Ball import *

# Windows config 

WINDOWS_WIDTH = 800
WINDOWS_HEIGHT = 500

# Root windows
root = Tk()
root['bg']="black"
root.title("Snake")
root.geometry("+500+100")

# Play area
myFont = tkinter.font.Font(weight="bold",size=40)
canvaJeu = Canvas(root,width=WINDOWS_WIDTH,height=WINDOWS_HEIGHT)
canvaJeu['bg']="black"
middleLine = canvaJeu.create_line(WINDOWS_WIDTH/2,50,WINDOWS_WIDTH/2,WINDOWS_HEIGHT-50,width=2)
topLine = canvaJeu.create_line(0,50,WINDOWS_WIDTH,50,width=2)
botLine = canvaJeu.create_line(0,450,WINDOWS_WIDTH,450,width=2)
scoreLabel = canvaJeu.create_text(WINDOWS_WIDTH/2,25,text="SCORE",font=myFont)
canvaJeu.pack()

# Init. var
player1 = Raquette(50,190,60,300,canvaJeu)
player2 = Raquette(750,190,760,300,canvaJeu)
ball = Ball(canvaJeu,460,250,470,260)

# Play functions

def moveWithKey(e):
    player1.move(canvaJeu,e,1)
    player2.move(canvaJeu,e,2)

def play():
    ball.move(canvaJeu)
    root.after(40,play)
# Main functions

play()
root.bind("<KeyPress>", moveWithKey)
root.mainloop()