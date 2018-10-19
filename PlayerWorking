# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:52:57 2018

@author: singh
"""
from Board import Board

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
         

        
        
    
