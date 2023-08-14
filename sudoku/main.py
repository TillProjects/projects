#!/usr/bin/env python3
# sudoku solver3
from board import create_grid, print_sudoku
from solving import solve_sudoku

# empty_sudoku_grid = [
#         [0, 0, 0,  0, 0, 0,  0, 0, 0],
#         [0, 0, 0,  0, 0, 0,  0, 0, 0],
#         [0, 0, 0,  0, 0, 0,  0, 0, 0],

#         [0, 0, 0,  0, 0, 0,  0, 0, 0],
#         [0, 0, 0,  0, 0, 0,  0, 0, 0],
#         [0, 0, 0,  0, 0, 0,  0, 0, 0],

#         [0, 0, 0,  0, 0, 0,  0, 0, 0],
#         [0, 0, 0,  0, 0, 0,  0, 0, 0],
#         [0, 0, 0,  0, 0, 0,  0, 0, 0]
#     ]

sudoku_grid = [
        [4, 1, 0,  0, 6, 5,  0, 0, 7],
        [0, 0, 6,  0, 0, 7,  4, 8, 0],
        [2, 0, 7,  4, 9, 0,  0, 0, 6],

        [0, 6, 0,  0, 7, 0,  1, 0, 0],
        [3, 0, 1,  5, 0, 0,  0, 7, 2],
        [0, 9, 0,  0, 4, 2,  3, 0, 8],

        [1, 0, 8,  6, 0, 0,  0, 2, 9],
        [0, 2, 0,  0, 1, 8,  6, 4, 0],
        [6, 0, 0,  3, 0, 0,  0, 1, 0]
    ]


sudoku_grid_np = create_grid(sudoku_grid)
print('Starting with:')
print_sudoku(sudoku_grid_np)

print('Starting to solve...')

if not solve_sudoku(sudoku_grid_np):
    print('No solution found')
    exit(1)
print('Solved!')
print_sudoku(sudoku_grid_np)
