#
# Strategy Game
#

import pygame

class PieceA:
    character = 'A'
    
def drawBoard(matrix):
    
    print(f"    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15")
    print(f"  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐")
    print(f"1 │ {matrix[0][0]} │ {matrix[1][0]} │ {matrix[2][0]} │ {matrix[3][0]} │ {matrix[4][0]} │ {matrix[5][0]} │ {matrix[6][0]} │ {matrix[7][0]} │ {matrix[8][0]} │ {matrix[9][0]} │ {matrix[10][0]} │ {matrix[11][0]} │ {matrix[12][0]} │ {matrix[13][0]} │ {matrix[14][0]} │ {matrix[15][0]}")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"2 │ {matrix[0][1]} │ {matrix[1][1]} │ {matrix[2][1]} │ {matrix[3][1]} │ {matrix[4][1]} │ {matrix[5][1]} │ {matrix[6][1]} │ {matrix[7][1]} │ {matrix[8][1]} │ {matrix[9][1]} │ {matrix[10][1]} │ {matrix[11][1]} │ {matrix[12][1]} │ {matrix[13][1]} │ {matrix[14][1]} │ {matrix[15][1]}")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"3 │ {matrix[0][2]} │ {matrix[1][2]} │ {matrix[2][2]} │ {matrix[3][2]} │ {matrix[4][2]} │ {matrix[5][2]} │ {matrix[6][2]} │ {matrix[7][2]} │ {matrix[8][2]} │ {matrix[9][2]} │ {matrix[10][2]} │ {matrix[11][2]} │ {matrix[12][2]} │ {matrix[13][2]} │ {matrix[14][2]} │ {matrix[15][2]}")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"4 │ {matrix[0][3]} │ {matrix[1][3]} │ {matrix[2][3]} │ {matrix[3][3]} │ {matrix[4][3]} │ {matrix[5][3]} │ {matrix[6][3]} │ {matrix[7][3]} │ {matrix[8][3]} │ {matrix[9][3]} │ {matrix[10][3]} │ {matrix[11][3]} │ {matrix[12][3]} │ {matrix[13][3]} │ {matrix[14][3]} │ {matrix[15][3]}")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"5 │ {matrix[0][4]} │ {matrix[1][4]} │ {matrix[2][5]} │ {matrix[3][4]} │ {matrix[4][4]} │ {matrix[5][4]} │ {matrix[6][4]} │ {matrix[7][4]} │ {matrix[8][4]} │ {matrix[9][4]} │ {matrix[10][4]} │ {matrix[11][4]} │ {matrix[12][4]} │ {matrix[13][4]} │ {matrix[14][4]} │ {matrix[15][4]}")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"6 │ {matrix[0][5]} │ {matrix[1][5]} │ {matrix[2][5]} │ {matrix[3][5]} │ {matrix[4][5]} │ {matrix[5][5]} │ {matrix[6][5]} │ {matrix[7][5]} │ {matrix[8][5]} │ {matrix[9][5]} │ {matrix[10][5]} │ {matrix[11][5]} │ {matrix[12][5]} │ {matrix[13][5]} │ {matrix[14][5]} │ {matrix[15][5]}")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"7 │ {matrix[0][6]} │ {matrix[1][6]} │ {matrix[2][6]} │ {matrix[3][6]} │ {matrix[4][6]} │ {matrix[5][6]} │ {matrix[6][6]} │ {matrix[7][6]} │ {matrix[8][6]} │ {matrix[9][6]} │ {matrix[10][6]} │ {matrix[11][6]} │ {matrix[12][6]} │ {matrix[13][6]} │ {matrix[14][6]} │ {matrix[15][6]}")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"8 │ {matrix[0][7]} │ {matrix[1][7]} │ {matrix[2][7]} │ {matrix[3][7]} │ {matrix[4][7]} │ {matrix[5][7]} │ {matrix[6][7]} │ {matrix[7][7]} │ {matrix[8][7]} │ {matrix[9][7]} │ {matrix[10][7]} │ {matrix[11][7]} │ {matrix[12][7]} │ {matrix[13][7]} │ {matrix[14][7]} │ {matrix[15][7]}")
    print(f"  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤")
    print(f"9 │ {matrix[0][8]} │ {matrix[1][8]} │ {matrix[2][8]} │ {matrix[3][8]} │ {matrix[4][8]} │ {matrix[5][8]} │ {matrix[6][8]} │ {matrix[7][8]} │ {matrix[8][8]} │ {matrix[9][8]} │ {matrix[10][8]} │ {matrix[11][8]} │ {matrix[12][8]} │ {matrix[13][8]} │ {matrix[14][8]} │ {matrix[15][8]}")
    print(f"  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘")

def boardFill(matrix):
    for x in range(0,15):
        for y in range(0,2):
            matrix[x][y] = "\033[38;5;14m1\033[0m"
            matrix[x][7+y] = "\033[38;5;196m1\033[0m"

def main():
    matrix = [[' ' for _ in range(9)] for _ in range(16)] 
  
    boardFill(matrix)

    playing = True
    while playing:
        drawBoard(matrix)
        input()
    
if __name__ == "__main__":
    main()

    #https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797