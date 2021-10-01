### NOTE
# Encode board state as a matrix:
# x, y, Cell State
# Cell States = Nothing, P1 North, P2 North, P1 NE, P2 NE, ..., P1 NW, P2 NW.
#
# Input Directions
# 8  1  2
#  \ | /
# 7--0--3
#  / | \
# 6  5  4
#
# Standard Rules
# https://docs.google.com/document/d/1ktpS0tOxAkbPBtf-p-Orr_Svy0R5ypZU-VdUvGMtIas/edit?usp=sharing

import numpy as np
from numpy.core.fromnumeric import shape
from numpy.core.numeric import full

def moveDirectionToEncoding(p1, dir): #take input direction and converts it into encoding direction
    val = (2 * dir) - 1 #why does this feel wrong to me lol
    if not p1: #scuff
        val += 1
    return val

def endCheck(board): #how was this easy
    for i in range(0, shape(board)[1]):
        for j in range(0, shape(board)[0]):
            if board[i][j] == 0:
                return False
    return True

def legalCheck(y, x, d, board): #better now maybe
    xMax = shape(board)[1] - 1
    yMax = shape(board)[0] - 1

    if d == 1 and board[y][x] == 0: #NORTH
        return True
    elif d == 1 and (y > 0):
        legalCheck(y-1, x, d, board)
    elif d == 2 and board[y][x] == 0: #NE
        return True
    elif d== 2 and (y > 0 and x < xMax):
        legalCheck(y-1, x+1, d, board)
    elif d == 3 and board[y][x] == 0: #East
        return True
    elif d== 3 and (x < xMax):
        legalCheck(y, x+1, d, board)
    elif d == 4 and board[y][x] == 0: #SE
        return True
    elif d== 4 and (y < yMax and x < xMax):
        legalCheck(y+1, x+1, d, board)
    elif d == 5 and board[y][x] == 0: #South
        return True
    elif d== 5 and (y < yMax):
        legalCheck(y+1, x, d, board)
    elif d == 6 and board[y][x] == 0: #SW
        return True
    elif d== 6 and (y < yMax and x > 0):
        legalCheck(y+1, x-1, d, board)
    elif d == 7 and board[y][x] == 0: #West
        return True
    elif d== 7 and (x > 0):
        legalCheck(y, x-1, d, board)
    elif d == 8 and board[y][x] == 0: #NW
        return True
    elif d== 8 and (y > 0 and x > 0):
        legalCheck(y-1, x-1, d, board)
    else:
        return False
        
def pointSpaceUpdate(y, x, d, board, psMatrix): #i think it works?
    xMax = shape(board)[1] - 1
    yMax = shape(board)[0] - 1

    if d == 1 and board[y][x] == 0 and psMatrix[y][x] != True: #NORTH
        psMatrix[y][x] = True
        pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d == 1 and (y > 0):
        pointSpaceUpdate(y-1, x, d, board, psMatrix)
    elif d == 2 and board[y][x] == 0 and psMatrix[y][x] != True: #NE
        psMatrix[y][x] = True
        pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 2 and (y > 0 and x < xMax):
        pointSpaceUpdate(y-1, x+1, d, board, psMatrix)
    elif d == 3 and board[y][x] == 0 and psMatrix[y][x] != True: #East
        psMatrix[y][x] = True
        pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 3 and (x < xMax):
        pointSpaceUpdate(y, x+1, d, board, psMatrix)
    elif d == 4 and board[y][x] == 0 and psMatrix[y][x] != True: #SE
        psMatrix[y][x] = True
        pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 4 and (y < yMax and x < xMax):
        pointSpaceUpdate(y+1, x+1, d, board, psMatrix)
    elif d == 5 and board[y][x] == 0 and psMatrix[y][x] != True: #South
        psMatrix[y][x] = True
        pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 5 and (y < yMax):
        pointSpaceUpdate(y+1, x, d, board, psMatrix)
    elif d == 6 and board[y][x] == 0 and psMatrix[y][x] != True: #SW
        psMatrix[y][x] = True
        pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 6 and (y < yMax and x > 0):
        pointSpaceUpdate(y+1, x-1, d, board, psMatrix)
    elif d == 7 and board[y][x] == 0 and psMatrix[y][x] != True: #West
        psMatrix[y][x] = True
        pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 7 and (x > 0):
        pointSpaceUpdate(y, x-1, d, board, psMatrix)
    elif d == 8 and board[y][x] == 0 and psMatrix[y][x] != True: #NW
        psMatrix[y][x] = True
        pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 8 and (y > 0 and x > 0):
        pointSpaceUpdate(y-1, x-1, d, board, psMatrix)
    else:
        return psMatrix

def floodfill(boardIn, y, x, check): #TODO return a floodfilled matrix from point y,x
    print("placeholder")

boardDim = (8, 8) #Board Dimensions X,Y
board = np.full((boardDim[1],boardDim[0]), 0) #board state encoding
pointSpace = np.full((boardDim[1],boardDim[0]), True) #was a space pointed into by previous move
gameDone = False #end condition met?
p1Turn = True #whos turn is it

while not (endCheck(board)): #Game Loop
    #Show me board state
    print(board) 

    #Input
    while True:
        mInfo = (int(input("Cell X: ")) - 1, int(input("Cell Y: ")) - 1, int(input("Direction: "))) #TODO -1 is for ease of use in console prototype
        if pointSpace[mInfo[1]][mInfo[0]] == True and board[mInfo[1]][mInfo[0]] == 0:
            break
        else:
            print("Input a Legal Space")

    #Place Move
    board[mInfo[1]][mInfo[0]] = moveDirectionToEncoding(p1Turn, mInfo[2])

    #Legal Check
    legal = legalCheck(mInfo[1], mInfo[0], mInfo[2], board)

    if legal == False: #if not legal
        for i in range(0, shape(board)[0]): #loop over board filling empty spaces with oppsing player arrows (per rule 3.2)
            for j in range(0, shape(board)[1]):
                if board[i][j] == 0 and p1Turn:
                    board[i][j] = 2
                elif board[i][j] and not p1Turn:
                    board[i][j] = 1

        if endCheck(board):
            break


    #Update Point Space Matrix
    pointSpace = np.full(shape(board), False)
    pointSpace = pointSpaceUpdate(mInfo[1], mInfo[0], mInfo[2], board, pointSpace)

    #Update Turn Bool
    p1Turn = not p1Turn

print(board)

# TODO Count Score
#p1board = floodfill(board % 2, 0, 0, True, 0)

# TODO Determine Winner
# TODO Cry
# TODO Graphics
