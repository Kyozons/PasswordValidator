# Reversegam: a clone of Reversi
import random
import sys
WIDTH = 8 # Board is 8 spaces wide
HEIGHT = 8 # Board is 8 spaces tall
def drawBoard(board):
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
    for x in range(WIDTH):
        board.append([' ', ' ', ' ',' ', ' ', ' ', ' ',' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    # Return False if the player's move on space xstaart, ystart is invalid.
    # If it is a valid mone, return a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' '  or not isOnBoard(xstart, ystart):
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
        while isOnBoard(x, y) and board[x][y] == otherTile:
            #Keep moving on this x & y direction.
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse
                # Direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip
def isOnBoard(x, y):
    # Return True if the coordinates are located on the board.
    return x >= 0 and x <= WIDTH -1 and y >= 0 and y <= HEIGHT -1

def getBoardWithValidMoves(board, tile):
    #Return a new board with periods marking the valid moves the player can make.
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    # Return a list of [x,y] lists of valid moves for the given player
    # on the given board.
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if  isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Return a dictionary with keys 'X' and 'O'.
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O': oscore}

def enterPlayerTile():
    # Let the player enter wich tile they want to be.
    # Return a list with the player's tile as the first item and the computer's tile as the second
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Quieres jugar como X o como O?')
        tile = input().upper()

        # The first element in the list is the player's tile, the second is the computer's tile.
        if tile == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    # Randomly select who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart and flip any of the opponent's pieces.
    # Return False if this is an invalid move; True if valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False
    
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    # make a duplicate af the board list and return it.
    boardCopy = getNewBoard()

    for x in range (WIDTH):
        for y in range (HEIGHT):
            boardCopy[x][y] = board[x][y]
    
    return boardCopy

def isOnCorner(x, y):
    # Return True if the position is on one of the four corners.
    return (x == 0 or x == WIDTH -1) and (y == 0 or y == HEIGHT -1)

def getPlayerMove(board, playerTile):
    # Let the player enter their move.
    # Return the move as [x, y] (or return the string 'hints' or 'quiit').
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Ingresa un movimiento, "salir" para finalizar el juego, o "pistas" para mostrar los movimientos posibles.')
        move = input().lower()
        if move == 'salir' or move == 'pistas':
            return move

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('Movimiento no válido. Usa la columna (1-8) y la fila (1-8).')
            print('Por ejemplo, 81 se moverá a la esquina superior derecha.')

    return [x, y]

def getComputerMove(board, computerTile):
    # Given a board and the computer's tile. determine where to 
    # move and return that move as an [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves) # Randomize the order of the moves.
    
    # Always go for a corner if available
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Find the highest-scoring move possible.
    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
        return bestMove

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('You: {} points. Computer: {} points.'.format(scores[playerTile], scores[computerTile]))

def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print('The {} will go first'.format(turn))
    
    # Clear the board and place starting pieces
    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board # No one can move, so end the game.

        elif turn == 'player': # Player's turn
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile)
                if move == 'salir':
                    print('Thanks for playing!')
                    sys.exit()  # Terminate the program
                elif move == 'pistas':
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])
            turn = 'computer'
        elif turn == 'computer': # CPU's turn
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)
                input('Press Enter to see computer\'s move.')
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[0], move[1])
            turn = 'player'

print('Welcome To Reversegam!')

playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)

    # Display the final score.
    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X scored {} points. O scored {} points.'.format(scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by {} points! Congrats!'.format(scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You lost. The computer beat you by {} points'.format(scores[computerTile] - scores[playerTile]))
    else:
        print('The game was a tie!')

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break


