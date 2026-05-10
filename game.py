#
# Strategy Game
#

import pygame
import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    
def drawBoard(matrix, turn, bluePlayers, redPlayers):
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

def boardFill(matrix):
    for x in range(0,15):
        for y in range(0,2):
            matrix[x][y] = f"\033[38;5;14m■\033[0m"
            matrix[x][7+y] = f"\033[38;5;196m■\033[0m"

def movePiece(turn, matrix, bluePlayers, redPlayers):
    usrCoord = input("Move from (x,y): ")
    newCoord = input("Move to   (x,y): ")

    # Convert user input to coordinates
    try:
        usrX_str, usrY_str = [s.strip() for s in usrCoord.split(',', 1)]
        newX_str, newY_str = [s.strip() for s in newCoord.split(',', 1)]
        usrX = int(usrX_str) - 1
        usrY = int(usrY_str) - 1
        newX = int(newX_str) - 1
        newY = int(newY_str) - 1
    except (ValueError, IndexError):
        print("Invalid coordinates. Use format x,y like 1,1 or 01,01.")
        return matrix
    
    # Check move validity
    if turn == 1:
        if matrix[usrX][usrY] == "\033[38;5;14m■\033[0m":
            print("BLUE!!!")
            if abs((usrX+usrY) - (newX+newY)) <= 2:
                if matrix[newX][newY] == " ":
                    matrix[newX][newY] = "\033[38;5;14m■\033[0m"
                    matrix[usrX][usrY] = " "

                    if newY <= 6:
                        if matrix[newX][newY+1] == "\033[38;5;196m■\033[0m":
                            matrix[newX][newY+1] = "\033[38;5;196mX\033[0m"
                            redPlayers -= 1
                    if newY <= 7:
                        if matrix[newX][newY+2] == "\033[38;5;196m■\033[0m":
                            matrix[newX][newY+1] = "\033[38;5;72mi\033[0m"
                            drawBoard(matrix, turn, bluePlayers, redPlayers)
                            time.sleep(1.0)
                            matrix[newX][newY+1] = " "
                            matrix[newX][newY+2] = "\033[38;5;196mX\033[0m"
                            redPlayers -= 1 

    if turn == 2:
        if matrix[usrX][usrY] == "\033[38;5;196m■\033[0m":
            print("RED!!!")
            if abs((usrX+usrY) - (newX+newY)) <= 2:
                if matrix[newX][newY] == " ":
                    matrix[newX][newY] = "\033[38;5;196m■\033[0m"
                    matrix[usrX][usrY] = " "

                    if newY >= 1:
                        if matrix[newX][newY-1] == "\033[38;5;14m■\033[0m":
                            matrix[newX][newY-1] = "\033[38;5;14mX\033[0m"
                            bluePlayers -= 1
                    if newY >= 2:
                        matrix[newX][newY-1] = "\033[38;5;72mi\033[0m"
                        drawBoard(matrix, turn, bluePlayers, redPlayers)
                        time.sleep(1.0)
                        if matrix[newX][newY-2] == "\033[38;5;14m■\033[0m":
                            matrix[newX][newY-2] = "\033[38;5;14mX\033[0m"
                            bluePlayers -= 1
                    
    return matrix, bluePlayers, redPlayers

def main():
    matrix = [[' ' for _ in range(9)] for _ in range(15)]
    redPlayers = 30
    bluePlayers = 30
    boardFill(matrix)

    playing = True
    turn = random.randint(1, 2)

    while playing:
        drawBoard(matrix, turn, bluePlayers, redPlayers)
        matrix, bluePlayers, redPlayers = movePiece(turn, matrix, bluePlayers, redPlayers)
        clear_screen()

        if turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1

        if bluePlayers <= 0:
            print("RED WINS!!!")
            playing = False
        elif redPlayers <= 0:
            print("BLUE WINS!!!")
            playing = False
            
if __name__ == "__main__":
    clear_screen()
    main()