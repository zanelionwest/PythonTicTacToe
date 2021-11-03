import sys

board = [['1','2','3'],['4','5','6'],['7','8','9']]

userinput1 = ''
userinput2 = ''
player1 = ''
player2 = ''
gamewinner = False
player1turn = True 

def start():
    
    p1 = ''
    p2 = ''
    p1_x_or_o = ''

    p1_x_or_o = input("Player one, please type in either X or O")    
    
    p1_x_or_o = p1_x_or_o.upper()
    
    if p1_x_or_o == 'X':
        print("Nice, X is a good selection")
        p1 = 'X'
        p2 = 'O'
    elif p1_x_or_o == 'O':
        print("Nice, O is a good selection")
        p1 = 'O'
        p2 = 'X'
    else:
        print("Please type in either X or O")

    return p1, p2

def player1move(p1,b1):
    board = []
    board = b1

    while True:
        try:  
            player1move = int(input("Player 1 please choose a number 1 - 9 to make your move"))
            break
        except ValueError:
            print("Please enter a number")
       
    # player1move = int(player1move)
    if player1move == 1 and (board[0][0] != 'X' or board[0][0] != 'O'):
        board[0][0] = p1
        return board
    elif player1move == 2 and (board[0][1] != 'X' or board[0][1] != 'O'):
        board[0][1] = p1
        return board
    elif player1move == 3 and (board[0][2] != 'X' or board[0][2] != 'O'):
        board[0][2] = p1
        return board
    elif player1move == 4 and (board[1][0] != 'X' or board[1][0] != 'O'):
        board[1][0] = p1
        return board
    elif player1move == 5 and (board[1][1] != 'X' or board[1][1] != 'O'):
        board[1][1] = p1
        return board
    elif player1move == 6 and (board[1][2] != 'X' or board[1][2] != 'O'):
        board[1][2] = p1
        return board
    elif player1move == 7 and (board[2][0] != 'X' or board[2][0] != 'O'):
        board[2][0] = p1
        return board
    elif player1move == 8 and (board[2][1] != 'X' or board[2][1] != 'O'):
        board[2][1] = p1
        return board
    elif player1move == 9 and (board[2][2] != 'X' or board[2][2] != 'O'):
        board[2][2] = p1
        return board
    else:
        print("Please make a valid selection")
        return board

    
def printrows():

    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")

def player2move(p2,b1):
    board = []
    board = b1

    while True:
        try:  
            player2move = int(input("Player 2 please choose a number 1 - 9 to make your move"))
            break
        except ValueError:
            print("Please enter a number")

    # player2move = input("Player 2 please choose a number 1 - 9 to make your move")
    # player2move = int(player2move)
    if player2move == 1 and (board[0][0] != 'X' or board[0][0] != 'O'):
        board[0][0] = p2
        return board
    elif player2move == 2 and (board[0][1] != 'X' or board[0][1] != 'O'):
        board[0][1] = p2
        return board
    elif player2move == 3 and (board[0][2] != 'X' or board[0][2] != 'O'):
        board[0][2] = p2
        return board
    elif player2move == 4 and (board[1][0] != 'X' or board[1][0] != 'O'):
        board[1][0] = p2
        return board
    elif player2move == 5 and (board[1][1] != 'X' or board[1][1] != 'O'):
        board[1][1] = p2
        return board
    elif player2move == 6 and (board[1][2] != 'X' or board[1][2] != 'O'):
        board[1][2] = p2
        return board
    elif player2move == 7 and (board[2][0] != 'X' or board[2][0] != 'O'):
        board[2][0] = p2
        return board
    elif player2move == 8 and (board[2][1] != 'X' or board[2][1] != 'O'):
        board[2][1] = p2
        return board
    elif player2move == 9 and (board[2][2] != 'X' or board[2][2] != 'O'):
        board[2][2] = p2
        return board
    else:
        print("Please make a valid selection")
        return board    

    
def winner(board):
    win = False
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" or board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" or board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        win = True
        print("We have a winner!")
        exit()
        return win
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" or board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" or board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        win = True
        print("We have a winner!")
        exit()
        return win
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        win = True
        print("We have a winner!")
        exit()
        return win
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" or board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" or board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        win = True
        print("We have a winner!")
        exit()
        return win
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" or board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" or board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        win = True
        print("We have a winner!")
        exit()
        return win
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" or board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        win = True
        print("We have a winner!")
        exit()
        return win
    elif board[0][0] != 1 and board[0][1] != 2 and board[0][2] != 3 and board[1][0] != 4 and board[1][1] != 5 and board[1][2] != 6 and board[2][0] != 7 and board[2][1] != 8 and board[2][2] != 9:
        print("We have a stalemate, draw!!")
        exit()
    else:
        win = False
        return win
        

def gameflow(p1, p2, board):
    thewinner = False 
    p1turn = True
    while thewinner != True:
        while p1turn == True:        
        
            print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
            print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
            print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")
            # printrows()
            thewinner = winner(board)
            board = player1move(p1,board)
            p1turn = False     

        else:
            print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
            print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
            print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")
            # printrows()
            thewinner = winner(board)            
            board = player2move(p2,board)
            p1turn = True



player1, player2 = start()
gameflow(player1,player2,board)
