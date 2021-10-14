# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:22:19 2021

@author: Spandan
"""

import random

#%%
def random_board(height,width):
    board = []
    for x in range(height):
        row = []
        for y in range(width):
            row.append(random.choice([0,1]))
        board.append(row)
    return board


def render(board):
    print("----"*len(board[0]))
    for x in range(len(board)):
        for y in range(len(board[x])):
            if(board[x][y] == 0):
                print (".",end="   ")
            else:
                print("#",end="   ")
        print('\n')
    print("----"*len(board[0]))

def cell_state(x,n):
    if(x==1):
        if(n<2):
            return 0
        elif(n<=3):
            return 1
        else:
            return 0
    else:
        if(n==3):
            return 1
        else:
            return 0


def next_state(in_board):
    new_state = []
    
    for x in range(len(in_board)):
        row = []
        n = len(in_board[x])
        for y in range(len(in_board[0])):
            
            count=in_board[x][(y+1)%n]+in_board[x][(y-1)%n]+in_board[(x-1)%n][y]+in_board[(x+1)%n][y] \
                +in_board[(x-1)%n][(y-1)%n]+in_board[(x+1)%n][(y-1)%n]+in_board[(x-1)%n][(y+1)%n] \
                    +in_board[(x+1)%n][(y+1)%n]
            row.append(cell_state(in_board[x][y], count))
        new_state.append(row)
    
    return new_state
    
def check_stae(board):
    for x in board:
        for i in x:
            if i==1:
                return True
    return False
#%%
board = random_board(50,50)
render(board)
#%%
while(check_stae(board)):
    new_board = next_state(board)
    render(new_board)
    board = new_board