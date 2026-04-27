from random import randrange
from time import sleep

def init ():
    global BOT_KEY, USER_KEY, DRAWED_TABLE
    BOT_KEY = 'X'
    USER_KEY = 'O'
    DRAWED_TABLE = f"""
                {'+-------'*3}+
                {'|       '*4}
                {'|   $   |   $   |   $   |'}
                {'|       '*4}
                """*3+f"{'+-------'*3}+"

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    table = DRAWED_TABLE
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            table = table.replace('$', str(board[i][j]), 1)

    print(table)


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        try:
            print("🎮 Your turn!")
            entry = int(input("Choose a position (1-9): "))
            if entry < 1 or entry > 9: raise ValueError
            if not draw_move(board, entry, sign = USER_KEY): raise ValueError
            break
        except ValueError: 
            print("❌ Invalid move. Choose a free position between 1 and 9.")
    
def enter_moveBot(board):
    print("🤖 Bot is thinking...")
    # Duerme 2 segundos
    sleep(2)
    print("🤖 Bot played its move!")
    while True:
        if draw_move(board, randrange(1, 10), sign = BOT_KEY): break

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
    global FREE_SPACES
    FREE_SPACES = {
        board[r][c]: (r, c)
        for r in range(3)
        for c in range(3)
        if board[r][c] != BOT_KEY and board[r][c] != USER_KEY
    }
    return FREE_SPACES

    # return FREE_SPACES

def victory_for(board):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    hasWinner, sign = check_victory(board)

    if hasWinner:
        print(f""" 
              🏆 Game Ended! 
              🎉 Winner: {'X' if sign == "X" else "O"} """)
        return  True
    else:
        # Check free spaces
        if len(FREE_SPACES) == 0:
            print(f"""🤝 It's a draw! No winners this time.""")
            return True
    return False
        
def check_victory(board):
    # For rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] and board[r][0] in (BOT_KEY, USER_KEY):
            return True, board[r][0]
    # For cols
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] and board[0][c] in (BOT_KEY, USER_KEY):
            return True, board[0][c]
    # For diag
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] in (BOT_KEY, USER_KEY):
        return True, board[0][0]
    # For inv_diag
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] in (BOT_KEY, USER_KEY):
        return True, board[2][0]

    return False, None

def draw_move(board, value, sign):
    if value in FREE_SPACES:
        r, c = FREE_SPACES[value] #(0,1)
        board[r][c] = sign
        FREE_SPACES.pop(value)
        return True
    return False

def start_game():
    keep_alive = True
    while keep_alive:
        init()
        board = [[i+j*3+1 if i+j*3+1!=5 else BOT_KEY for i in range(3)] for j in range(3)]

        make_list_of_free_fields(board)
        display_board(board)
        turnPhase = True 
        
        while True:
            if turnPhase:
                enter_move(board)
            else: 
                enter_moveBot(board)
                
            display_board(board)        
            if victory_for(board): break    
            turnPhase = not turnPhase
            print("\n" + "="*30 + "\n")
            
        while True:
            try:
                entry = input("🔁 Do you want to play again? (s/n): ")
                answer = entry.lower()
                if answer not in ('s', 'n'):
                    raise ValueError
                
                keep_alive = answer == 's'

                break
            except ValueError:
                print("❌ Please type 's' for yes or 'n' for no.")

start_game()