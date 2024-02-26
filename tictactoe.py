def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    moves_left = 9

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while moves_left > 0:
        row = int(input(f"Player {players[current_player]}, enter row (0-2): "))
        col = int(input(f"Player {players[current_player]}, enter column (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move, try again.")
            continue

        board[row][col] = players[current_player]
        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break

        moves_left -= 1
        if moves_left == 0:
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2


# Start the game
tic_tac_toe()
