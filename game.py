#
# Strategy Game
#

import pygame
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Piece:
    type = ['A','B','C']
    side = ["\033[38;5;196m", "\033[38;5;14m"]
    id = 0
    coordinates = [0, 0] 

    def display(self):
        return f"{self.side}{self.type}\033[0m"
        
    def __init__(self, id, type, side, coordinates):
        self.id = id
        self.type = type
        self.side = side
        self.coordinates = coordinates
    
def drawBoard(matrix, pTurn):
    
    print(f"    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15")
    print(f"  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
    print(f"1 │ {matrix[0][0]} │ {matrix[1][0]} │ {matrix[2][0]} │ {matrix[3][0]} │ {matrix[4][0]} │ {matrix[5][0]} │ {matrix[6][0]} │ {matrix[7][0]} │ {matrix[8][0]} │ {matrix[9][0]} │ {matrix[10][0]} │ {matrix[11][0]} │ {matrix[12][0]} │ {matrix[13][0]} │ {matrix[14][0]} │")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"2 │ {matrix[0][1]} │ {matrix[1][1]} │ {matrix[2][1]} │ {matrix[3][1]} │ {matrix[4][1]} │ {matrix[5][1]} │ {matrix[6][1]} │ {matrix[7][1]} │ {matrix[8][1]} │ {matrix[9][1]} │ {matrix[10][1]} │ {matrix[11][1]} │ {matrix[12][1]} │ {matrix[13][1]} │ {matrix[14][1]} │")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"3 │ {matrix[0][2]} │ {matrix[1][2]} │ {matrix[2][2]} │ {matrix[3][2]} │ {matrix[4][2]} │ {matrix[5][2]} │ {matrix[6][2]} │ {matrix[7][2]} │ {matrix[8][2]} │ {matrix[9][2]} │ {matrix[10][2]} │ {matrix[11][2]} │ {matrix[12][2]} │ {matrix[13][2]} │ {matrix[14][2]} │ {pTurn[0][0]} {pTurn[1][0]} {pTurn[2][0]} {pTurn[3][0]} {pTurn[4][0]} │")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"4 │ {matrix[0][3]} │ {matrix[1][3]} │ {matrix[2][3]} │ {matrix[3][3]} │ {matrix[4][3]} │ {matrix[5][3]} │ {matrix[6][3]} │ {matrix[7][3]} │ {matrix[8][3]} │ {matrix[9][3]} │ {matrix[10][3]} │ {matrix[11][3]} │ {matrix[12][3]} │ {matrix[13][3]} │ {matrix[14][3]} │ {pTurn[0][1]} {pTurn[1][1]} {pTurn[2][1]} {pTurn[3][1]} {pTurn[4][1]} │")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"5 │ {matrix[0][4]} │ {matrix[1][4]} │ {matrix[2][4]} │ {matrix[3][4]} │ {matrix[4][4]} │ {matrix[5][4]} │ {matrix[6][4]} │ {matrix[7][4]} │ {matrix[8][4]} │ {matrix[9][4]} │ {matrix[10][4]} │ {matrix[11][4]} │ {matrix[12][4]} │ {matrix[13][4]} │ {matrix[14][4]} │ {pTurn[0][2]} {pTurn[1][2]} {pTurn[2][2]} {pTurn[3][2]} {pTurn[4][2]} │")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"6 │ {matrix[0][5]} │ {matrix[1][5]} │ {matrix[2][5]} │ {matrix[3][5]} │ {matrix[4][5]} │ {matrix[5][5]} │ {matrix[6][5]} │ {matrix[7][5]} │ {matrix[8][5]} │ {matrix[9][5]} │ {matrix[10][5]} │ {matrix[11][5]} │ {matrix[12][5]} │ {matrix[13][5]} │ {matrix[14][5]} │ {pTurn[0][3]} {pTurn[1][3]} {pTurn[2][3]} {pTurn[3][3]} {pTurn[4][3]} │")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"7 │ {matrix[0][6]} │ {matrix[1][6]} │ {matrix[2][6]} │ {matrix[3][6]} │ {matrix[4][6]} │ {matrix[5][6]} │ {matrix[6][6]} │ {matrix[7][6]} │ {matrix[8][6]} │ {matrix[9][6]} │ {matrix[10][6]} │ {matrix[11][6]} │ {matrix[12][6]} │ {matrix[13][6]} │ {matrix[14][6]} │ {pTurn[0][4]} {pTurn[1][4]} {pTurn[2][4]} {pTurn[3][4]} {pTurn[4][4]} │")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"8 │ {matrix[0][7]} │ {matrix[1][7]} │ {matrix[2][7]} │ {matrix[3][7]} │ {matrix[4][7]} │ {matrix[5][7]} │ {matrix[6][7]} │ {matrix[7][7]} │ {matrix[8][7]} │ {matrix[9][7]} │ {matrix[10][7]} │ {matrix[11][7]} │ {matrix[12][7]} │ {matrix[13][7]} │ {matrix[14][7]} │ {pTurn[0][5]} {pTurn[1][5]} {pTurn[2][5]} {pTurn[3][5]} {pTurn[4][5]} │")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"9 │ {matrix[0][8]} │ {matrix[1][8]} │ {matrix[2][8]} │ {matrix[3][8]} │ {matrix[4][8]} │ {matrix[5][8]} │ {matrix[6][8]} │ {matrix[7][8]} │ {matrix[8][8]} │ {matrix[9][8]} │ {matrix[10][8]} │ {matrix[11][8]} │ {matrix[12][8]} │ {matrix[13][8]} │ {matrix[14][8]} │")
    print(f"  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")

def boardFill(matrix):
    for x in range(0,15):
        for y in range(0,2):
            matrix[x][y] = f"\033[38;5;14m■\033[0m"
            matrix[x][7+y] = f"\033[38;5;196m■\033[0m"

def movePiece(turn, matrix):
    usrCoord = input()
    newCoord = input()

    usrX = int(usrCoord[:2])-1
    usrY = int(usrCoord[3:])-1

    newX = int(newCoord[:2])-1
    newY = int(newCoord[3:])-1

    print(f"{usrX}, {usrY}")
    
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
                    if newY <= 7:
                        if matrix[newX][newY+2] == "\033[38;5;196m■\033[0m":
                            matrix[newX][newY+2] = "\033[38;5;196mX\033[0m"

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
                    if newY >= 2:
                        if matrix[newX][newY-2] == "\033[38;5;14m■\033[0m":
                            matrix[newX][newY-2] = "\033[38;5;14mX\033[0m"
    return matrix

def main():
    matrix = [[' ' for _ in range(9)] for _ in range(16)] 
    pTurn = [[' ' for _ in range(5)] for _ in range(5)]
    boardFill(matrix)

    playing = True
    turn = random.randint(1, 2)
    if turn == 1:
        print("BLUE GOES FIRST")
        for x in range(0,5):
            for y in range(0,5):
                pTurn[x][y] = f"\033[38;5;14m■\033[0m"
        
    else:
        for x in range(0,5):
            for y in range(0,5):
                pTurn[x][y] = f"\033[38;5;196m■\033[0m"
        print("RED GOES FIRST")
        
    while playing:
        drawBoard(matrix, pTurn)
        matrix = movePiece(turn, matrix)
        clear_screen()

        if turn == 1: 
            turn = 2
        elif turn == 2: 
            turn = 1
    
if __name__ == "__main__":
    main()