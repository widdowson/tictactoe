def print_board(board):
    """Print the current state of the 3x3 board to stdout.

    Cells in each row are separated by ' | ', and rows are separated
    by a horizontal '---------' divider.
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")


def check_winner(board, player):
    """Return True if the given player has three marks in a row.

    Checks all three rows, all three columns, and both diagonals.
    Returns False if no winning line is found for the player.
    """
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
    """Return True if every cell on the board is occupied.

    Used to detect a draw when no player has won.
    """
    return all(board[r][c] != " " for r in range(3) for c in range(3))


def get_move(name, marker, board):
    """Prompt the named player for a move and return (row, col).

    Accepts a position 1-9 numbered left-to-right, top-to-bottom, and
    keeps prompting until the input is a valid integer in range that
    points to an empty cell.
    """
    while True:
        try:
            move = int(input(f"{name} ({marker}), enter a position (1-9): ")) - 1
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
    """Run one full game of tic-tac-toe between two human players.

    Prompts for each player's name, initializes an empty board, prints
    a numbered position key for reference, then alternates between
    players X and O until one wins or the board fills and the game is
    a draw.
    """
    board = [[" "] * 3 for _ in range(3)]

    name_x = input("Enter name for Player 1 (X): ").strip() or "Player 1"
    name_o = input("Enter name for Player 2 (O): ").strip() or "Player 2"
    names = {"X": name_x, "O": name_o}

    print("\nPositions:\n1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9\n")

    current = "X"
    while True:
        print_board(board)
        row, col = get_move(names[current], current, board)
        board[row][col] = current

        if check_winner(board, current):
            print_board(board)
            print(f"{names[current]} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    play()
