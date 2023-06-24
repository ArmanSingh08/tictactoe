import random

# Tic Tac Toe

# Create the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    line = "-------------"
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        print(line)

# Function to check if someone has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# Function for player's turn
def player_turn():
    print_board()
    position = int(input("Enter a position (1-9): ")) - 1

    if board[position] == " ":
        board[position] = "X"
        if check_win("X"):
            print_board()
            print("Congratulations! You win!")
            return True
    else:
        print("Invalid move. Try again.")
        return player_turn()

# Function for computer's turn
def computer_turn():
    available_positions = [i for i, value in enumerate(board) if value == " "]
    if available_positions:
        position = random.choice(available_positions)
        board[position] = "O"
        if check_win("O"):
            print_board()
            print("The computer wins!")
            return True

# Function to play the game
def play_game():
    game_over = False

    while not game_over:
        if player_turn():
            break
        
        if computer_turn():
            break

        if " " not in board:
            print_board()
            print("It's a tie!")
            break

# Start the game
play_game()
