### THOUGHTS
# Encode board state as a matrix:
# x, y, Cell State
# Cell States = Nothing, P1 North, P2 North, P1 NE, P2 NE, ..., P1 NW, P2 NW.

import numpy as np
from numpy.core.fromnumeric import shape

def moveDirectionToEncoding(p1, dir): #take input direction and converts it into encoding direction
    val = (2 * dir) - 1 #why does this feel wrong to me lol
    if not p1: #scuff
        val += 1
    return val

def endCheck(board):
    for i in range(0, shape(board)[0]):
        for j in range(0, shape(board)[1]):
            if board[j][i] == 0:
                return False
    return True

def legalCheck(move, board):
    i = 1
    if move[2] == 1: #NORTH
        while True:
            try:
                if board[move[1] - i][move[0]] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 2: #NE
        while True:
            try:
                if board[move[1] - i][move[0] + i] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 3: #EAST
        while True:
            try:
                if board[move[1]][move[0] + i] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 4: #SE
        while True:
            try:
                if board[move[1] + i][move[0] + i] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 5: #SOUTH
        while True:
            try:
                if board[move[1] + i][move[0]] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 6: #SW
        while True:
            try:
                if board[move[1] + i][move[0] - i] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 7: #WEST
        while True:
            try:
                if board[move[1]][move[0] - i] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 8: #NW
        while True:
            try:
                if board[move[1] - i][move[0] - i] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    return False

boardDim = (8, 8) #Board Dimensions X,Y
board = np.full((boardDim[1],boardDim[0]), 0) #board state encoding
pointSpace = np.full((boardDim[1],boardDim[0]), True) #was a space pointed into by previous move
gameDone = False #end condition met?
p1Turn = True #whos turn is it


while not (gameDone):
    #Show me board state
    print(board) 

    #Input
    while True:
        mInfo = (int(input("Cell X: ")) - 1, int(input("Cell Y: ")) - 1, int(input("Direction: "))) #TODO -1 is for ease of use in console prototype
        if pointSpace [mInfo[1]][mInfo[0]] == True:
            break
        else:
            print("Input a Legal Space")

    #End Check
    gameDone = endCheck(board)

    #legal Move Check
    legal = legalCheck(mInfo, board)
    if not legal:
        for i in range(0, shape(board)[0]):
            for j in range(0, shape(board)[1]):
                if board[j][i] == 0 and p1Turn:
                    board[j][i] = 1
                elif board[j][i] and not p1Turn:
                    board[j][i] = 2
                    
    #Place Move
    board[mInfo[1]][mInfo[0]] = moveDirectionToEncoding(p1Turn, mInfo[2])

    #Update Point Space Matrix

    #Update Turn Bool
    p1Turn = not p1Turn