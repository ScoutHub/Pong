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
player1 = Raquette(50,190,60,300,canvaJeu,1)
player2 = Raquette(750,190,760,300,canvaJeu,-1)
ball = Ball(canvaJeu,460,250,470,260)
tempScore1, tempScore2 = 0,0
scoreFirstPlayer = canvaJeu.create_text(WINDOWS_WIDTH/4,25,text=str(player1.score),font=myFont)
scoreSecondPlayer = canvaJeu.create_text(WINDOWS_WIDTH - (WINDOWS_WIDTH/4),25,text=str(player2.score),font=myFont)

# Play functions

def moveWithKey(e):
    player1.setFlag(e,1)
    player2.setFlag(e,2)

def play():
    global tempScore1,tempScore2,scoreFirstPlayer,scoreSecondPlayer
    ball.move(canvaJeu,player1,player2)
    player1.move(canvaJeu,1)
    player2.move(canvaJeu,2)
    if(tempScore1 != player1.score):
        tempScore1 += 1
        canvaJeu.delete(scoreFirstPlayer)
        scoreFirstPlayer = canvaJeu.create_text(WINDOWS_WIDTH/4,25,text=str(player1.score),font=myFont)
    elif(tempScore2 != player2.score):
        tempScore2 += 1
        canvaJeu.delete(scoreSecondPlayer)
        scoreSecondPlayer = canvaJeu.create_text(WINDOWS_WIDTH - (WINDOWS_WIDTH/4),25,text=str(player2.score),font=myFont)
    root.after(40,play)

# Main functions

play()
root.bind("<KeyPress>", moveWithKey)
root.mainloop()