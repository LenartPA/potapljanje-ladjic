from random import *

#x = int(input("x(5, 10) = "))
x = 10
if x > 10:
    x = 10
elif x < 5:
    x = 5
#y = int(input("y(5, 10) = "))
y = 10
if y > 10:
    y = 10
elif y < 5:
    y = 5

# Create the boards
# ' ' or '~' for water, 'S' for ship
hidden_board = [[" " for _ in range(x)] for _ in range(y)]
# '*' for unknown, 'M' for miss, 'H' for hit
player_board = [["~" for _ in range(x)] for _ in range(y)]

matrix = [[0 for _ in range(y)] for _ in range(x)]

xcord = [i for i in range(1, x+1)]
ycord = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def print_board(board, x, y, ycord):
    print("  " + " ".join(str(i) for i in range(1, x + 1)))
    for i in range(y):
        print(f"{ycord[i]} " + " ".join(board[i]))

print_board(player_board, x, y, ycord)


num = int(input("Number of ships: "))
for i in range(num):
    size = randint(2, 5)
    orient = randint(0, 1)

