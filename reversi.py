# Reversegam: a clone of Reversi
import random
import sys
WIDTH = 8 # Board is 8 spaces wide
HEIGHT = 8 # Board is 8 spaces tall
def dawBoard(board):
    # Print the board pased to this function. Return None.
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print(  '12345678')

def getNewBoard():
    # Create a brand-new, blank board structure.
    board= []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ',' ', ' ', ' ', ' ',' '])
        return board

def isValidMove(board, title, xstart, ystart):
    # Return False if the player's move on space xstaart, ystart is invalid.
    # If it is a valid mone, return a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBard(xstart, ystart):
        return False
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1,0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # First step in the x direction
        y += ydirection # First step in the y direction
        while
