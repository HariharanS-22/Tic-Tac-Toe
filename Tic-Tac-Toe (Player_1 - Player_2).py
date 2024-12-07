
from random import randrange

def display_board(board):
    print(" -------" * 3, " ", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print(" -------" * 3, " ", sep="")

def free_boxes(board):
    free = []    
    for row in range(3): 
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col)) 
    return free

def player_move(board,player):
    valid = False
    while not valid:
        move = input(f"{player}: Enter your move (1-9): ") 
        valid = len(move) == 1 and move >= '1' and move <= '9'
        if not valid:
            print("Bad move - repeat your input!") 
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3  
        sign = board[row][col]
        valid = sign not in ['O', 'X']
        if not valid:    
            print("Field already occupied - repeat your input!")
            continue
    if player == "Player 1":
        board[row][col] = 'X'
    elif player == "Player 2":
        board[row][col] = 'O' 

def victory_for(board, sign):
    if sign == "X":    
        who = 'Player 1'    
    elif sign == "O": 
        who = 'Player 2'
    else:
        who = None    
    cross1 = cross2 = True
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return who
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return who
        if board[i][i] != sign:
            cross1 = False
        if board[i][2 - i] != sign:
            cross2 = False
    if cross1 or cross2:
        return who
    return None

board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  

free = free_boxes(board)

print("\nPlayer 1 plays 'X' \nPlayer 2 plays 'O'\n")
player1_turn = True
while len(free):
    display_board(board)
    if player1_turn:
        player_move(board,"Player 1")
        victor = victory_for(board, 'X')
    else:    
        player_move(board,"Player 2")
        victor = victory_for(board, 'O')
    if victor != None:
        break
    player1_turn = not player1_turn        
    free = free_boxes(board)

display_board(board)
if victor == 'Player 1':
    print("Player 1 won!")
elif victor == 'Player 2':
    print("Player 2 won!")
else:
    print("Tie!")
