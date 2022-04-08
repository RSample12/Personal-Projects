# Riley Sample
# Sudoku Solver: Solves sudoku board input in matrix form
# Created: 3/28/22
# Last edited: 3/29/22

import sys


def is_valid(board, row, col, n):

    # check row if any numbers are the same
    if n in board[row]:
        return False

    # check col
    same_col = [i[col] for i in board]
    if n in same_col:
        return False

    # finds square n resides in
    # calculates starting row, col for square
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == n:
                return False

    return True


def sudoku_solver(board, row, col):

    # check if reaches end of board
    if row == 8 and col == 8:
        print("Output:")
        for row in board:
            print(row)
        return

    # if col reaches end of row, move to next row
    elif col == 9:
        row += 1
        col = 0

    # if spot is empty check if nums 1-9 are valid
    if board[row][col] == 0:
        for n in range(1, 10):
            if is_valid(board, row, col, n):
                board[row][col] = n
                # create new branch
                sudoku_solver(board, row, col + 1)
                board[row][col] = 0

    # if spot is full, move to next spot
    else:
        sudoku_solver(board, row, col + 1)


def main():
    # read in board and convert to ints
    file = sys.stdin.readlines()
    board = []
    for line in file:
        temp = [int(i) for i in line.split()]
        board.append(temp)

    # print board before sudoku
    print("Input:")
    for row in board:
        print(row)

    # fill in board and print result
    sudoku_solver(board, 0, 0)


main()
