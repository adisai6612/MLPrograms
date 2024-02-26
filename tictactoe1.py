import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (len(row) * 4 - 1))

def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def user_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 'O'

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        user_move(board)
        print_board(board)
        if check_winner(board) == 'X':
            print("Congratulations! You won!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        computer_move(board)
        print("\nComputer's move:")
        print_board(board)
        if check_winner(board) == 'O':
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

play_game()
