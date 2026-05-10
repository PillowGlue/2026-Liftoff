#
# Strategy Game
#

import random
import os
import time

PIECES = [
    "\033[38;5;14m■\033[0m", # Blue Square
    "\033[38;5;196m■\033[0m", # Red Square

    "\033[38;5;14mX\033[0m",  # Blue Destroyed
    "\033[38;5;196mX\033[0m" # Red Destroyed
]

"""
Clear screen
"""
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

"""
Draw the board
"""
def draw_board(matrix, turn, bluePlayers, redPlayers):
    cols = len(matrix)
    rows = len(matrix[0]) if cols else 0

    header = "   " + "".join(f"{i:>4}" for i in range(1, cols + 1))
    print(header)
    print("    " + "┌" + "┬".join("───" for _ in range(cols)) + "┐")

    for y in range(rows):
        row_label = f"{y + 1:>2}"
        row_cells = "│".join(
            f" {matrix[x][y]} " if matrix[x][y] != " " else "   "
            for x in range(cols)
        )
        print(f"{row_label}  │{row_cells}│")
        if y < rows - 1:
            print("    " + "├" + "┼".join("───" for _ in range(cols)) + "┤")

    print("    " + "└" + "┴".join("───" for _ in range(cols)) + "┘")
    current_turn = "\033[38;5;14mBlue\033[0m" if turn == 1 else "\033[38;5;196mRed\033[0m"
    print()
    print(f"\033[38;5;14mBlue players: {bluePlayers}\033[0m | \033[38;5;196mRed players: {redPlayers}\033[0m\n")
    print(f"Turn: {current_turn}")

"""
Initial Board Setup
"""
def board_fill(matrix):
    for x in range(0, 15):
        for y in range(0, 2):
            matrix[x][y] = f"\033[38;5;14m■\033[0m"
            matrix[x][7 + y] = f"\033[38;5;196m■\033[0m"

"""
Check if valid move 
"""
def move_piece(turn, matrix):
    valid_move = False # Store if move is valid
    valid_coords = False

    # Get user coords
    usr_coord = input("Move from (x,y): ")
    new_coord = input("Move to   (x,y): ")

    # Convert user input to coordinates
    while not valid_coords:
        try:
            # Strings
            usr_x_str, usr_y_str = [s.strip() for s in usr_coord.split(',', 1)]
            new_x_str, new_y_str = [s.strip() for s in new_coord.split(',', 1)]

            # Ints
            usr_x = int(usr_x_str) - 1
            usr_y = int(usr_y_str) - 1
            new_x = int(new_x_str) - 1
            new_y = int(new_y_str) - 1
            valid_coords = True
        except (ValueError, IndexError):
            print("Invalid coordinates. Use format x,y like 1,1 or 01,01.")

    # Blue's turn
    if turn == 1:
        if matrix[usr_x][usr_y] == PIECES[0]:
            # Left
            if usr_x - 2 == new_x and usr_y == new_y:
                valid_move = True
            elif usr_x - 1 == new_x and usr_y == new_y:
                valid_move = True
            # Left down
            elif usr_x - 2 == new_x and usr_y + 2 == new_y:
                valid_move = True
            elif usr_x - 1 == new_x and usr_y + 1 == new_y:
                valid_move = True
            # Down
            elif usr_x == new_x and usr_y + 2 == new_y:
                valid_move = True
            elif usr_x == new_x and usr_y + 1 == new_y:
                valid_move = True
            # Right down
            elif usr_x + 2 == new_x and usr_y + 2 == new_y:
                valid_move = True
            elif usr_x + 1 == new_x and usr_y + 1 == new_y:
                valid_move = True
            # Right
            elif usr_x + 2 == new_x and usr_y == new_y:
                valid_move = True
            elif usr_x + 1 == new_x and usr_y == new_y:
                valid_move = True

            if valid_move:
                matrix[new_x][new_y] = PIECES[0]
                matrix[usr_x][usr_y] = " "
            else:
                move_piece(turn, matrix)

    # Reds's turn
    if turn == 2:
        if matrix[usr_x][usr_y] == PIECES[1]:
            # Left
            if usr_x - 2 == new_x and usr_y == new_y:
                valid_move = True
            elif usr_x - 1 == new_x and usr_y == new_y:
                valid_move = True
            # Left up
            elif usr_x - 2 == new_x and usr_y - 2 == new_y:
                valid_move = True
            elif usr_x - 1 == new_x and usr_y - 1 == new_y:
                valid_move = True
            # Up
            elif usr_x == new_x and usr_y - 2 == new_y:
                valid_move = True
            elif usr_x == new_x and usr_y - 1 == new_y:
                valid_move = True
            # Right up
            elif usr_x + 2 == new_x and usr_y - 2 == new_y:
                valid_move = True
            elif usr_x + 1 == new_x and usr_y - 1 == new_y:
                valid_move = True
            # Right
            elif usr_x + 2 == new_x and usr_y == new_y:
                valid_move = True
            elif usr_x + 1 == new_x and usr_y == new_y:
                valid_move = True

            if valid_move:
                matrix[new_x][new_y] = PIECES[1]
                matrix[usr_x][usr_y] = " "
            else:
                move_piece(turn, matrix)

    return matrix

"""
Shoot nearby piece
"""
def shoot_piece(turn, matrix):
    # Get user coords
    usr_coord = input("Shoot from (x,y): ")
    valid_coords = False

    # Convert user input to coordinates
    try:
        # Strings
        usr_x_str, usr_y_str = [s.strip() for s in usr_coord.split(',', 1)]

        # Ints
        usr_x = int(usr_x_str) - 1
        usr_y = int(usr_y_str) - 1
        valid_coords = True
    except (ValueError, IndexError):
        print("Shooting cancelled")

    if valid_coords:
        # Blue's turn
        if turn == 1:
            # Directions
            direction = input("Choose a direction. [L]eft, [R]ight, D[own]: ")

            if direction == "L":
                if matrix[usr_x-1][usr_y] == PIECES[1]:
                    matrix[usr_x-1][usr_y] = PIECES[3]
                elif matrix[usr_x-2][usr_y] == PIECES[1]:
                    matrix[usr_x-2][usr_y] = PIECES[3]

            elif direction == "D":
                if matrix[usr_x][usr_y+1] == PIECES[1]:
                    matrix[usr_x][usr_y+1] = PIECES[3]
                elif matrix[usr_x][usr_y+2] == PIECES[1]:
                    matrix[usr_x][usr_y+2] = PIECES[3]

            elif direction == "R":
                if matrix[usr_x + 1][usr_y] == PIECES[1]:
                    matrix[usr_x + 1][usr_y] = PIECES[3]
                elif matrix[usr_x + 2][usr_y] == PIECES[1]:
                    matrix[usr_x + 2][usr_y] = PIECES[3]

        # Red's turn
        # Directions
        direction = input("Choose a direction. [L]eft, [R]ight, U[p]: ")
        if turn == 2:
            if direction == "L":
                if matrix[usr_x - 1][usr_y] == PIECES[0]:
                    matrix[usr_x - 1][usr_y] = PIECES[2]
                elif matrix[usr_x - 2][usr_y] == PIECES[0]:
                    matrix[usr_x - 2][usr_y] = PIECES[2]

            elif direction == "U":
                if matrix[usr_x][usr_y + 1] == PIECES[0]:
                    matrix[usr_x][usr_y + 1] = PIECES[2]
                elif matrix[usr_x][usr_y + 2] == PIECES[0]:
                    matrix[usr_x][usr_y + 2] = PIECES[2]

            elif direction == "R":
                if matrix[usr_x + 1][usr_y] == PIECES[0]:
                    matrix[usr_x + 1][usr_y] = PIECES[2]
                elif matrix[usr_x + 2][usr_y] == PIECES[0]:
                    matrix[usr_x + 2][usr_y] = PIECES[2]

    return matrix

"""
MAIN
"""
def main():
    matrix = [[' ' for _ in range(9)] for _ in range(15)]
    red_players = 30
    blue_players = 30
    board_fill(matrix)

    playing = True
    turn = random.randint(1, 2)

    while playing:
        # Move
        clear_screen()
        draw_board(matrix, turn, blue_players, red_players)
        matrix = move_piece(turn, matrix)

        # Shoot
        clear_screen()
        draw_board(matrix, turn, blue_players, red_players)
        matrix = shoot_piece(turn, matrix)
        turn = 1 if turn == 2 else 2

        # Win 
        if blue_players <= 0:
            print("RED WINS!!!")
            playing = False
        elif red_players <= 0:
            print("BLUE WINS!!!")
            playing = False

if __name__ == "__main__":
    clear_screen()
    main()
