"""Cuatro en línea, por Kyozons practicando pythonic code
Un juego donde hay que formar cuatro fichas en línea
dejando caer fichas, inspirado en conecta cuatro"""

import sys

# Constantes usadas para mostrar tablero:
EMTPY_SPACE = "."  # Un punto es más facil de contar que un espacio en blanco.
PLAYER_X = "X"
PLAYER_O = "O"

# Nota: Actualizar BOARD_TEMPLATE y COLUMN_LABELS si se modifica BOARD_WIDTH.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# El molde para mostrar el tablero:
BOARD_TEMPLATE = """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+"""

def main():
    """Inicia un solo juego de cuatro en línea. """
    print(
        """Cuatro en línea, por Kyozons

Dos jugadores toman turnos para soltar fichas en una de las siete columnas,
tratando de formar cuatro en línea de manera horizontal, vertical o diagonal.
""")

    # Preparar un nuevo juego:
    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:  # Comienza un turno.
        # Muestra el tablero y toma un movimiento de jugador:
        display_board(game_board)
        player_move = get_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        # Verifica una victoria o un empate:
        if is_winner(player_turn, game_board):
            display_board(game_board)  # Muestra el tablero una última vez.
            print("Jugador {} ha ganado!".format(player_turn))
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)  # Muestra el tablero una última vez.
            print("Hay un empate!")
            sys.exit()

        # Cambio de turno:
        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X

def get_new_board():
    """Devuelve un diccionario que reperesenta un tablero de cuatro en línea.

    Los Keys son (colum_index, row_index) tuplas de dos integers, y los
    valores son uno de los strings 'X', 'O' ó '.'(espacio vacío)."""
    board = {}
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            board[(column_index, row_index)] = EMTPY_SPACE
    return board


def display_board(board):
    """Muestra el tablero con las fichas en la pantalla."""

    # Prepara una lista para pasar al método format() para
    # el template del tablero. La lista tiene todas las 
    # fichas del tablero (y espacios vacios) llendo de
    # izquierda a derecha, de arriba a abajo:
    tile_chars = []
    for row_index in range(BOARD_HEIGHT):
        for colum_index in range(BOARD_WIDTH):
            tile_chars.append(board[(colum_index, row_index)])

    # Muestra el tablero:
    print(BOARD_TEMPLATE.format(*tile_chars))


def get_player_move(player_tile, board):
    """Dejar que el jugador eliga una columna en la cual
    dejar caer una ficha.

    Devuelve una tupla del can la (columna, fila) en la que
    cae la ficha."""
    while True: # Le sigue preguntando al jugador hasta que ingrese movimiento válido.
        print(f"Jugador {player_tile}, elige columna del 1 al {BOARD_WIDTH} o SALIR: ")
        response = input(">> ").upper().strip()

        if response == "SALIR":
            print("Gracias por jugar!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print(f"Ingresa un número del 1 al {BOARD_WIDTH}.")
            continue # Le pregunta denuevo por un movimiento.
        
        column_index = int(response) - 1  # -1 porque el índice empieza en 0.

        # Si la columna está llena, pregunta por un movimiento nuevamente:
        if board[(column_index, 0)] != EMTPY_SPACE:
            print("Esa columna está llena, prueba otra.")
            continue # Le pregunta denuevo por un movimiento.

        # Encuentra el primer espacio vacío, empezando desde el fondo:
        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(column_index, row_index)] == EMTPY_SPACE:
                return (column_index, row_index)

def is_full(board):
    """Devuelve True si el tablero no tiene espacios vacíos,
    de lo contrario devuele False."""
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            if board[(column_index, row_index)] == EMTPY_SPACE:
                return False  # Se encontró un espacio vacío
    return True  # Todos los espacios llenos.

def is_winner(player_tile, board):
    """Devuelve True si un jugador (player_tile) tiene
    cuatro en línea en el tablero (board), de lo contrario
    devuelve False."""

    # Busca un cuatro en línea por todo el tablero:
    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT):
            # Busca un cuatro en línea de izquierda a derecha:
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index)]
            tile3 = board[(column_index + 2, row_index)]
            tile4 = board[(column_index + 3, row_index)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True
    
    for column_index in range(BOARD_WIDTH):
        for row_index in  range(BOARD_HEIGHT - 3):
            # Busca un cuatro en línea de arriba a abajo:
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index, row_index + 1)]
            tile3 = board[(column_index, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT - 3):
            # Busca un cuatro en línea en diagonal de derecha a abajo:
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index + 1)]
            tile3 = board[(column_index + 2, row_index + 2)]
            tile4 = board[(column_index + 3, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True
            
            # Busca un cuatro en línea en diagonal de izquierda a abajo:
            tile1 = board[(column_index + 3, row_index)]
            tile2 = board[(column_index + 2, row_index + 1)]
            tile3 = board[(column_index + 1, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True
    return False

# Si el programa se ejecuta directamente (en vez de importarse), corre el juego:
if __name__ == "__main__":
    main()



