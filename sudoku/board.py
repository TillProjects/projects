import numpy as np


def create_grid(grid) -> np.array:
    sudoku_grid_np = np.array(grid, dtype=np.int8)
    return sudoku_grid_np


def print_sudoku(grid) -> None:
    for i in range(9):
        for j in range(9):
            print(grid[i, j], end=" ")
            if (j + 1) % 3 == 0 and j < 8:  # Add vertical separator every 3 cells
                print("|", end=" ")
        print()  # New line after each row
        if (i + 1) % 3 == 0 and i < 8:  # Add horizontal separator every 3 rows
            print("- " * 11)


