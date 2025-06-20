import numpy as np

def is_valid(board, num, pos):
    row, col = pos
    if num in board[row]: return False
    if num in board[:, col]: return False

    box_x, box_y = col // 3, row // 3
    box = board[box_y*3:box_y*3+3, box_x*3:box_x*3+3]
    if num in box: return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, (i, j)):
                        board[i][j] = num
                        if solve(board): return True
                        board[i][j] = 0
                return False
    return True

def solve_sudoku(board):
    board = np.array(board)
    if solve(board):
        return board
    else:
        raise ValueError("Unsolvable Sudoku")
