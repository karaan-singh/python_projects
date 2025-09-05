def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

print("Welcome to Tic Tac Toe!")
print_board(board)

while True:
    try:
        move = input(f"Player {current_player}, enter your move (row and column: 1 1 for top-left): ")
        if move.lower() == "quit":
            print("Game exited.")
            break
        row, col = map(int, move.split())
        if board[row - 1][col - 1] != " ":
            print("Cell already taken. Try again.")
            continue
        board[row - 1][col - 1] = current_player
        print_board(board)
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"
    except (ValueError, IndexError):
        print("Invalid input. Enter row and column numbers between 1 and 3, separated by a space.")