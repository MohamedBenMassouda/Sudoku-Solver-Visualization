import random

board: list[list[int]] = \
    [[0, 0, 5, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [6, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [2, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 3]]


def find_empty(board: list[list[int]]):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j

    return False

def solve(board: list[list[int]]):
    find = find_empty(board)

    if not find:
        return True

    else:
        row, col = find

    for i in range(1, 10):
        if check_num(board, i, row, col):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False




def check_num(board:list[list[int]], i, row:int, col:int):
    for j in range(len(board)):
        if board[j][col] == i and j != row:
            return False

    for j in range(len(board[row])):
        if board[row][j] == i and j != col:
            return False

    # Checking 3x3
    box_x = col // 3
    box_y = row // 3

    for j in range(box_y * 3, box_y * 3 + 3):
        for k in range(box_x * 3, box_x * 3 + 3):
            if board[j][k] == i and j != row and k != col:
                return False

    return True


def print_board(board: list[list[int]]):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " " , end="")


print("This is the board before solving\n")
print_board(board)

solve(board)

print("\nThis is after being solved\n")
print_board(board)