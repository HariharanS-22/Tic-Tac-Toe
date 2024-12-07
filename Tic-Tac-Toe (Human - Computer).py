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

def human_move(board):
    valid = False
    while not valid:
        move = input("Enter your move (1-9): ") 
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
    board[row][col] = 'O' 

def computer_move(board):
    free = free_boxes(board) 
    count = len(free)
    if count > 0:    
        move = randrange(count)
        row, col = free[move]
        board[row][col] = 'X'

def free_boxes(board):
    free = []    
    for row in range(3): 
        for col in range(3):
            if board[row][col] not in ['O', 'X']:
                free.append((row, col)) 
    return free

def victory_for(board, sign):
    if sign == "X":    
        who = 'Computer'    
    elif sign == "O": 
        who = 'Human'
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
user = input("Do you want to play the first move (Yes/No) :")
if user == "Yes":
    human_turn = True
else:
    human_turn = False

while len(free):
    display_board(board)
    if human_turn:
        human_move(board)
        victor = victory_for(board, 'O')
    else:    
        computer_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn        
    free = free_boxes(board)

display_board(board)
if victor == 'Human':
    print("You won!")
elif victor == 'Computer':
    print("I won!")
else:
    print("Tie!")
