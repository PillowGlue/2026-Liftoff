#
# Strategy Game
#

import pygame

def drawBoard(matrix):
    for row in matrix:
        for item in row:
            print(f"{item} | ", end="")
        print("")
        for item in row:
            print("----", end="")
        print("")

def main():
    matrix = [[0 for _ in range(15)] for _ in range(15)] 
    for in range(15)
        for in
    matrix[0][0] = 1

    drawBoard(matrix)
    
if __name__ == "__main__":
    main()