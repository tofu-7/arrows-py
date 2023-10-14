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
# Encoding Directions for Player 1 (add 1 for Player 2 Directions)
# 15  1  3
#   \ | /
# 13--0--5
#   / | \
# 11  9  7
#
# Standard Rules
# https://docs.google.com/document/d/1ktpS0tOxAkbPBtf-p-Orr_Svy0R5ypZU-VdUvGMtIas/edit?usp=sharing

import numpy as np
from numpy.core.fromnumeric import shape
from numpy.core.numeric import full
import largestBlob as lcb

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
        return legalCheck(y-1, x, d, board)
    elif d == 2 and board[y][x] == 0: #NE
        return True
    elif d== 2 and (y > 0 and x < xMax):
        return legalCheck(y-1, x+1, d, board)
    elif d == 3 and board[y][x] == 0: #East
        return True
    elif d== 3 and (x < xMax):
        return legalCheck(y, x+1, d, board)
    elif d == 4 and board[y][x] == 0: #SE
        return True
    elif d== 4 and (y < yMax and x < xMax):
        return legalCheck(y+1, x+1, d, board)
    elif d == 5 and board[y][x] == 0: #South
        return True
    elif d== 5 and (y < yMax):
        return legalCheck(y+1, x, d, board)
    elif d == 6 and board[y][x] == 0: #SW
        return True
    elif d== 6 and (y < yMax and x > 0):
        return legalCheck(y+1, x-1, d, board)
    elif d == 7 and board[y][x] == 0: #West
        return True
    elif d== 7 and (x > 0):
        return legalCheck(y, x-1, d, board)
    elif d == 8 and board[y][x] == 0: #NW
        return True
    elif d== 8 and (y > 0 and x > 0):
        return legalCheck(y-1, x-1, d, board)
    else:
        return False
        
def pointSpaceUpdate(y, x, d, board, psMatrix): #i think it works?
    xMax = shape(board)[1] - 1
    yMax = shape(board)[0] - 1

    if d == 1 and board[y][x] == 0 and psMatrix[y][x] != True: #NORTH
        psMatrix[y][x] = True
        return pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d == 1 and (y > 0):
        return pointSpaceUpdate(y-1, x, d, board, psMatrix)
    elif d == 2 and board[y][x] == 0 and psMatrix[y][x] != True: #NE
        psMatrix[y][x] = True
        return pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 2 and (y > 0 and x < xMax):
        return pointSpaceUpdate(y-1, x+1, d, board, psMatrix)
    elif d == 3 and board[y][x] == 0 and psMatrix[y][x] != True: #East
        psMatrix[y][x] = True
        return pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 3 and (x < xMax):
        return pointSpaceUpdate(y, x+1, d, board, psMatrix)
    elif d == 4 and board[y][x] == 0 and psMatrix[y][x] != True: #SE
        psMatrix[y][x] = True
        return pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 4 and (y < yMax and x < xMax):
        return pointSpaceUpdate(y+1, x+1, d, board, psMatrix)
    elif d == 5 and board[y][x] == 0 and psMatrix[y][x] != True: #South
        psMatrix[y][x] = True
        return pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 5 and (y < yMax):
        return pointSpaceUpdate(y+1, x, d, board, psMatrix)
    elif d == 6 and board[y][x] == 0 and psMatrix[y][x] != True: #SW
        psMatrix[y][x] = True
        return pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 6 and (y < yMax and x > 0):
        return pointSpaceUpdate(y+1, x-1, d, board, psMatrix)
    elif d == 7 and board[y][x] == 0 and psMatrix[y][x] != True: #West
        psMatrix[y][x] = True
        return pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 7 and (x > 0):
        return pointSpaceUpdate(y, x-1, d, board, psMatrix)
    elif d == 8 and board[y][x] == 0 and psMatrix[y][x] != True: #NW
        psMatrix[y][x] = True
        return pointSpaceUpdate(y, x, d, board, psMatrix)
    elif d== 8 and (y > 0 and x > 0):
        return pointSpaceUpdate(y-1, x-1, d, board, psMatrix)
    else:
        return psMatrix
    
def scoreCount(board, col):
    board = board % 2
    board = lcb.LargestColorBlob(board)
    return board.biggest_blob(col)

        

boardDim = (4, 4) #Board Dimensions X,Y
board = np.full((boardDim[1],boardDim[0]), 0) #board state encoding
pointSpace = np.full((boardDim[1],boardDim[0]), True) #was a space pointed into by previous move
gameDone = False #end condition met?
p1Turn = True #whos turn is it

while not (endCheck(board)): #Game Loop
    #Show me board state
    print(board) 

    #Input
    print(pointSpace)
    while True:
        mInfo = (int(input("Cell X: ")) - 1, int(input("Cell Y: ")) - 1, int(input("Direction: "))) #NOTE -1 is for ease of use in console prototype
        if pointSpace[mInfo[1]][mInfo[0]] == True and board[mInfo[1]][mInfo[0]] == 0:
            break
        else:
            print("Input a Legal Space")

    #Place Move
    board[mInfo[1]][mInfo[0]] = moveDirectionToEncoding(p1Turn, mInfo[2])

    #Legal Check
    '''legal = legalCheck(mInfo[1], mInfo[0], mInfo[2], board)
    print(legal)

    if legal == False: #if not legal
        for i in range(0, shape(board)[0]): #loop over board filling empty spaces with oppsing player arrows (per rule 3.2)
            for j in range(0, shape(board)[1]):
                if board[i][j] == 0 and p1Turn:
                    board[i][j] = 2
                elif board[i][j] and not p1Turn:
                    board[i][j] = 1

        if endCheck(board):
            break'''


    #Update Point Space Matrix
    pointSpace = np.full(shape(board), False)
    pointSpace = pointSpaceUpdate(mInfo[1], mInfo[0], mInfo[2], board, pointSpace)
    if not np.any(pointSpace) == True:
        print('here')
        for i in range(shape(board)[0]):
            for j in range(shape(board)[1]):
                if board[i][j] == 0:
                    board[i][j] = int(p1Turn) + 1
        print(int(p1Turn)+1)
        print(board)

    #Update Turn Bool
    p1Turn = not p1Turn

print(board)


# Determine Winner
p1Score = scoreCount(board, 1)
p2Score = scoreCount(board, 0)

if p1Score > p2Score:
    print("Player 1 Wins: " + str(p1Score) + " v " + str(p2Score))
elif p2Score > p1Score:
    print("Player 2 Wins: " + str(p1Score) + " v " + str(p2Score))
elif p1Score == p2Score:
    print("Draw: " + str(p1Score) + " v " + str(p2Score))

# TODO Cry
# TODO Graphics
