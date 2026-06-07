def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")


def check_winner(board, player):
    for row in board:
        if all(c == player for c in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(board[r][c] != " " for r in range(3) for c in range(3))


def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, enter a position (1-9): ")) - 1
            row, col = divmod(move, 3)
            if move < 0 or move > 8:
                print("Enter a number between 1 and 9.")
            elif board[row][col] != " ":
                print("That spot is taken.")
            else:
                return row, col
        except ValueError:
            print("Invalid input.")


def play():
    board = [[" "] * 3 for _ in range(3)]
    print("Positions:\n1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n")

    current = "X"
    while True:
        print_board(board)
        row, col = get_move(current, board)
        board[row][col] = current

        if check_winner(board, current):
            print_board(board)
            print(f"Player {current} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    play()
