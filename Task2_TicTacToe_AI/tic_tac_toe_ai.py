# Tic Tac Toe AI using Minimax

import math

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

def human_move():
    while True:
        pos = int(input("Enter position (1-9): ")) - 1
        if board[pos] == " ":
            board[pos] = "X"
            break
        else:
            print("Position already taken")

def play_game():

    print("Tic Tac Toe Game")
    print("You are X , AI is O")
    print("Positions are 1-9")

    print_board()

    while True:

        human_move()
        print_board()

        if check_winner("X"):
            print("You Win!")
            break

        if is_draw():
            print("Draw!")
            break

        ai_move()
        print("AI Move:")
        print_board()

        if check_winner("O"):
            print("AI Wins!")
            break

        if is_draw():
            print("Draw!")
            break

play_game()