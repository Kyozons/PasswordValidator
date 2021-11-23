import random
import sys
import math

def getNewBoard():
    # Create 60x15 board data structure.
    board = []
    for x in range(60): # Main list is a list of 60 lists.
        board.append([])
        for y in range(15): #Each list in the main list has 15 single character strings.
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append("'")
    return board

def drawBoard(board):
    tensDigitsLine = '   '
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    print(tensDigitsLine)
    print('   ' + ('0123456789' * 6))
    print()
    
    for row in range(15):
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    print()
    print(' ' + ('0123456789') * 6)
    print(tensDigitsLine)

def getRandomChests(numChests):
    # Create empty list of chests and append to it a two item list (x,y) coordinates.
    chests = []
    while len(chests) < numChests:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests: # Make sure chest is not created
            chests.append(newChest)
    return chests

def isOnBoard(x, y):
    #True if coordinates are on the board if not return False
    return x >= 0 and x <= 59 and y >= 0 and y <= 14 

def makeMove(board, chests, x, y):
    #Change the board data structure with a sonar device that remove treasure chests from the chests list when found
    # Return False if is invalid move. Otherwise, return the string of the result of this move.
    smallestDistance = 100 # Any chest will be closer than 100.
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))
        
        if distance < smallestDistance: # We want the closest treasure chest
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        # sonar is on a chest
        chests.remove([x, y])
        return 'Encontraste un cofre!'
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return 'Tesoro encontrado a distancia de %s' % (smallestDistance)
        else:
            board[x][y] = 'x'
            return 'No se detectó nada, cofres fuera de rango'

def enterPlayerMove(previousMoves):
    # Let the player enter their move. Return a two-item list of int xy coord.
    print('Donde desplegar sonar? (0-59 0-14) (o escribe \"salir\")')
    while True:
        move = input()
        if move.lower() == 'salir':
            print('Gracias por jugar!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('Ya te moviste ahí')
                continue
            return [int(move[0]), int(move[1])]
        print('Ingresa un número entre 0 y 59, un espacio y otro numero de 0 a 14. (Ej: 15 8)')

print('S O N A R!')
print()
while True:
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChests(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        # Show sonar and chests Statuses
        print('tienes %s sonares y faltan por encontrar %s cofres' % (sonarDevices, len(theChests)))

        x, y = enterPlayerMove(previousMoves)
        previousMoves.append([x, y]) #Track moves for updating sonar devices

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult == 'Encontraste un cofre!':
                # Update the sonar devices on the map
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)

        if len(theChests) == 0:
            print('Encontraste todos los cofres! Ganaste!')
            break

        sonarDevices -= 1

    if sonarDevices == 0:
        print('No hay más sonares disponibles... Pa casa.')
        print('Los cofres que faltaron estaban en: ')
        print('   %s, %s'% (x, y))

    print('Jugar nuevamente? (si/no)')
    if not input().lower().startswith('s'):
        sys.exit()


