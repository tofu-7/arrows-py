### NOTE
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

def endCheck(board): #how was this easy
    for i in range(0, shape(board)[0]):
        for j in range(0, shape(board)[1]):
            if board[j][i] == 0:
                return False
    return True

def legalCheck(move, board): #This is terrible
    i = 1
    if move[2] == 1: #NORTH
        while True:
            try:
                if move[1] - i < 0:
                    return False
                elif board[move[1] - i][move[0]] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 2: #NE
        while True:
            try:
                if move[1] - i < 0:
                    return False
                elif board[move[1] - i][move[0] + i] == 0:
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
                    print ("here")
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 6: #SW
        while True:
            try:
                if move[0] - i < 0:
                    return False
                elif board[move[1] + i][move[0] - i] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 7: #WEST
        while True:
            try:
                if move[0] - i < 0:
                    return False
                elif board[move[1]][move[0] - i] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    if move[2] == 8: #NW
        while True:
            try:
                if move[0] - i < 0 or move[1] < 0:
                    return False
                elif board[move[1] - i][move[0] - i] == 0:
                    return True
                else:
                    i += 1
            except IndexError:
                return False
    return False

#def betterLegalCheck(move, board): #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    if move[2] == 1: #NORTH
        for i in range(0, shape(board)[0] - 1 - move[1]):
            if board[move[1]-i][move[0]] == 0:
                return True

def pointSpaceUpdate(move, board): #This is worse than legalCheck
    i = 1
    pointSpace = np.full(shape(board), False)
    pointSpace[move[1]][move[0]] = False

    if move[2] == 1: #NORTH
        while True:
            try:
                if move[1] - i < 0:
                    return pointSpace
                elif board[move[1] - i][move[0]] == 0:
                    pointSpace[move[1] - i][move[0]] = True
                    i += 1
                else:
                    i += 1
            except IndexError:
                return pointSpace
    if move[2] == 2: #NE
        while True:
            try:
                if move[1] - i < 0:
                    return pointSpace
                elif board[move[1] - i][move[0] + i] == 0:
                    pointSpace[move[1] - i][move[0] + i] = True
                    i += 1
                else:
                    i += 1
            except IndexError:
                return pointSpace
    if move[2] == 3: #EAST
        while True:
            try:
                if board[move[1]][move[0] + i] == 0:
                    pointSpace[move[1]][move[0] + i] = True
                    i += 1
                else:
                    i += 1
            except IndexError:
                return pointSpace
    if move[2] == 4: #SE
        while True:
            try:
                if board[move[1] + i][move[0] + i] == 0:
                    pointSpace[move[1] + i][move[0] + i] = True
                    i += 1
                else:
                    i += 1
            except IndexError:
                return pointSpace
    if move[2] == 5: #SOUTH
        while True:
            try:
                if board[move[1] + i][move[0]] == 0:
                    pointSpace[move[1] + i][move[0]] = True
                    i += 1
                else:
                    i += 1
            except IndexError:
                return pointSpace
    if move[2] == 6: #SW
        while True:
            try:
                if move[0] - i < 0:
                    return pointSpace
                elif board[move[1] + i][move[0] - i] == 0:
                    pointSpace[move[1] + i][move[0] - i] = True
                    i += 1
                else:
                    i += 1
            except IndexError:
                return pointSpace
    if move[2] == 7: #WEST
        while True:
            try:
                if move[0] - i < 0:
                    return pointSpace
                elif board[move[1]][move[0] - i] == 0:
                    pointSpace[move[1]][move[0] - i] = True
                    i += 1
                else:
                    i += 1
            except IndexError:
                return pointSpace
    if move[2] == 8: #NW
        while True:
            try:
                if move[1] - i < 0 or move[0] - i < 0:
                    return pointSpace
                if board[move[1] - i][move[0] - i] == 0:
                    pointSpace[move[1] - i][move[0] - i] = True
                    i += 1
                else:
                    i += 1
            except IndexError:
                return pointSpace
    return pointSpace

def floodfill(boardIn, y, x, p1, gSize): #https://stackoverflow.com/questions/19839947/flood-fill-in-python
    group = gSize
    #"hidden" stop clause - not reinvoking for "c" or "b", only for "a".
    if p1 and board[y][x] == 1:  
        group += 1
        boardIn = 2
        #recursively invoke flood fill on all surrounding cells:
        if y > 0:
            group = floodfill(boardIn,y-1,x, p1, group)
        if y < shape(board)[0] - 1:
            group = floodfill(boardIn,y+1,x, p1, group)
        if x > 0:
            group = floodfill(boardIn,y,x-1, p1, group)
        if x < shape(board)[1] - 1:
            group = floodfill(boardIn,y,x+1, p1, group)
    
    if not p1 and board[y][x] == 0:  
        group += 1
        boardIn = 2
        #recursively invoke flood fill on all surrounding cells:
        if y > 0:
            group = floodfill(boardIn,y-1,x, p1, gSize)
        if y < shape(board)[0] - 1:
            group = floodfill(boardIn,y+1,x, p1, gSize)
        if x > 0:
            group = floodfill(boardIn,y,x-1, p1, gSize)
        if x < shape(board)[1] - 1:
            group = floodfill(boardIn,y,x+1, p1, gSize)
    
    return group

boardDim = (8, 8) #Board Dimensions X,Y
board = np.full((boardDim[1],boardDim[0]), 0) #board state encoding
pointSpace = np.full((boardDim[1],boardDim[0]), True) #was a space pointed into by previous move
gameDone = False #end condition met?
p1Turn = True #whos turn is it

while not (gameDone): #Game Loop
    #Show me board state
    print(board) 

    #End Check
    gameDone = endCheck(board)
    if gameDone:
        print("Game Over")
        break

    #Input
    while True:
        mInfo = (int(input("Cell X: ")) - 1, int(input("Cell Y: ")) - 1, int(input("Direction: "))) #TODO -1 is for ease of use in console prototype
        if pointSpace [mInfo[1]][mInfo[0]] == True and board[mInfo[1]][mInfo[0]] == 0:
            break
        else:
            print("Input a Legal Space")

    #legal Move Check
    legal = legalCheck(mInfo, board)
    if not legal:
        for i in range(0, shape(board)[0]):
            for j in range(0, shape(board)[1]):
                if board[i][j] == 0 and p1Turn:
                    board[i][j] = 2
                elif board[i][j] and not p1Turn:
                    board[i][j] = 1
                    
    #Place Move
    board[mInfo[1]][mInfo[0]] = moveDirectionToEncoding(p1Turn, mInfo[2])

    #Update Point Space Matrix
    pointSpace = pointSpaceUpdate(mInfo, board)

    #Update Turn Bool
    p1Turn = not p1Turn

# TODO Count Score
p1Score = floodfill(board % 2, 0, 0, True, 0)
print (p1Score)

# TODO Determine Winner
# TODO Cry
# TODO Graphics
