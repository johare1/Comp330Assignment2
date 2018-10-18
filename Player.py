# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:52:57 2018

@author: singh
"""
from Board import Board
from tkinter import *

class Player(Board):
    
    p1 = ""
    p2 = ""
    global num_wins1
    num_wins1 = 0
    global num_wins2
    num_wins2 = 0
    global num_draws
    num_draws = 0
    
    def setNames(self):
        p1 = input('Enter your name player 1: ')
        p2 = input('Enter your name player 1: ')
        
    def addWins(self):
        if(Board.win == True and self.turn%2 == 0):
            num_wins1 = num_wins1 + 1
            print(num_wins1)
        elif(Board.win == True):
            num_wins2 = num_wins2 + 1
        elif(Board.draw == True):
            num_draws = num_draws + 1
    """     
    global winCount
    winCount = StringVar()
    global winDisp
    winDisp = Label(ttt, textvariable = winCount)
    winDisp.pack()
    winDisp.place(height=20, width=100, x=200, y=450)
    winCount.set("Player 1 wins: " + num_wins1 + "Player 2 wins: " + num_wins2)
    """
#creating board

global board

board = [[2,2,2],[2,2,2],[2,2,2]]

global ttt

ttt = Tk()

ttt.title("tic tac toe")

ttt.geometry('500x500')

canvas = Canvas(ttt, width = 500, height = 500, bg = 'black')

    #turn/win label

global hud 

hud = StringVar()

global disp 

disp = Label(ttt, textvariable= hud)

disp.pack()

disp.place(height=20,width=100, x=50, y=450)

hud.set("O's turn")

boardGame = Board()

#intializing buttons on the board

b1 = tkinter.Button(ttt, text="click", command = boardGame.callback1,fg="black" )

        

b1.pack()

b1.place(height=50,width=100, x=35, y=50)

        

b2 = tkinter.Button(ttt, text="click", command = boardGame.callback2,fg="black")

        

b2.pack()

b2.place(height=50,width=100, x=200, y=50)

        

b3 = tkinter.Button(ttt, text="click", command = boardGame.callback3,fg="black")

        

b3.pack()

b3.place(height=50,width=100, x=365, y=50)

        

b4 = tkinter.Button(ttt, text="click", command = boardGame.callback4,fg="black")

        

b4.pack()

b4.place(height=50,width=100, x=35, y=225)

        

b5 = tkinter.Button(ttt, text="click",command = boardGame.callback5,fg="black")

        

b5.pack()

b5.place(height=50,width=100, x=200, y=225)

        

b6 = tkinter.Button(ttt, text="click",command = boardGame.callback6,fg="black")

        

b6.pack()

b6.place(height=50,width=100, x=365, y=225)

        

b7 = tkinter.Button(ttt, text="click",command = boardGame.callback7,fg="black")

        

b7.pack()

b7.place(height=50,width=100, x=35, y=375)

        

b8 = tkinter.Button(ttt, text="click",command = boardGame.callback8,fg="black")



b8.pack()

b8.place(height=50,width=100, x=200, y=375)

        

b9 = tkinter.Button(ttt, text="click",command = boardGame.callback9,fg="black")

        

b9.pack()

b9.place(height=50,width=100, x=365, y=375)

boardGame.makeBoard()



canvas.pack(fill=BOTH)

ttt.mainloop()
    
        
        
    
