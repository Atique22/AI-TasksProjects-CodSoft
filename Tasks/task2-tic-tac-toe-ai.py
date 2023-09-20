# TASK 2: TIC-TAC-TOE AI
# Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human
# player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to
# make the AI player unbeatable. This project will help you understand game theory 
# and basic search algorithms.

import random

# Define constants for the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the board is full
def is_full(board):
    return all(all(cell != EMPTY for cell in row) for row in board)

# Function to check if a player has won
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to evaluate the current state of the board for the Minimax algorithm
def evaluate(board):
    if is_winner(board, PLAYER_X):
        return 1  # Player X wins
    elif is_winner(board, PLAYER_O):
        return -1  # Player O wins
    else:
        return 0  # It's a draw

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, PLAYER_X):
        return 1
    if is_winner(board, PLAYER_O):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to make the AI move using Minimax with Alpha-Beta Pruning
def ai_move(board):
    best_move = None
    best_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, False, alpha, beta)
                board[i][j] = EMPTY

                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

# Main game loop
def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    
    print("Welcome to Tic-Tac-Toe! You are 'O', and the AI is 'X'.")
    print_board(board)

    while True:
        # Human player's move
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if board[row][col] == EMPTY:
                    break
                else:
                    print("That cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers (0, 1, or 2).")

        board[row][col] = PLAYER_O
        print_board(board)

        if is_winner(board, PLAYER_O):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI player's move
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = PLAYER_X
        print("AI's move:")
        print_board(board)

        if is_winner(board, PLAYER_X):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
