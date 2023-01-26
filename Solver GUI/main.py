import random

import pygame

pygame.init()

WIDTH = 800
window = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sudoku Solver Visualization")

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0
WHITE  = 255, 255, 255
FONT = pygame.font.SysFont("comicsans", 35)

window.fill(WHITE)
pygame.display.flip()

def draw_3x3():
    width = 100
    height = 70 # 700
    block = 70

    for i in range(10):
        """Adjusting the first height make the line longer"""
        w = 1
        if i % 3 == 0:
            w = 2

        #pygame.draw.rect(window, BLACK, (width + block * i, height + 630, block, block), 1)
        pygame.draw.line(window, BLACK, (width + block * i, height), (width + block * i, height + 630), w)
        for j in range(10):
            w = 1
            if j % 3 == 0:
                w = 2

            pygame.draw.line(window, BLACK, (width , block * (j + 1)), (800 - 70, block * (j + 1)), w)


def fill_3x3(board: list[list[int]]):
    block = 70
    for row in range(9):
        for col in range(9):
            num = FONT.render(f"{board[row][col]}", 1, BLACK)
            window.blit(num, (125 + block * col, 80 + block * row))

    pygame.display.update()

def generateBoard():
    l: list[list[int]] = \
            [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(15):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        while not check_num(l, num, row, col):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)

        l[row][col] = num

    return l

def find_empty(board: list[list[int]]):
    for j in range(len(board)):
        for k in range(len(board[j])):
            if board[j][k] == 0:
                return j, k

    return False

def clear_spot(row, col):
    # To clear the spot before changing the value
    block = 70
    num = FONT.render("0", 1, BLACK)
    num.fill((255, 255, 255))
    window.blit(num, (125 + block * col, 80 + block * row))
    pygame.display.update()

def redraw_line(row, col, color):
    width = 100
    block = 70
    height = 70
    pygame.draw.rect(window, color, (width + block * col, height + block * row, block, block), 3)


def solve(board: list[list[int]]):
    find = find_empty(board)
    block = 70

    if not find:
        return True

    else:
        row, col = find

    for i in range(1, 10):
        if check_num(board, i, row, col):
            board[row][col] = i
            clear_spot(row, col)
            num = FONT.render(f"{board[row][col]}", 1, BLACK)
            window.blit(num, (125 + block * col, 80 + block * row))
            redraw_line(row, col, GREEN)
            pygame.time.delay(200)

            # Recursion until the board is solved
            if solve(board):
                return True

            redraw_line(row, col, RED)
            board[row][col] = 0

    return False


def check_num(board: list[list[int]], n: int, row: int, col: int):
    """Checking Row"""
    for i in range(len(board)):
        if board[i][col] == n and i != row:
            return False

    """Checking Col"""
    for j in range(len(board)):
        if board[row][j] == n and j != col:
            return False

    """Checking 3x3"""
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == n and i != row and j != col:
                return False

    return True


def main():
    run = True
    board = generateBoard()
    #pygame.draw.line(window, BLACK, (100, 100), (200, 100), 1)
    draw_3x3()
    fill_3x3(board)
    pygame.display.update()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve(board)

                if event.key == pygame.K_r:
                    board = generateBoard()
                    draw_3x3()

    pygame.quit()


if __name__ == '__main__':
    main()
