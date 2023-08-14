def is_valid(grid, row, col, num):
    # Check if the number already exists in the same row or column
    if num in grid[row, :] or num in grid[:, col]:
        return False

    # Check if the number exists in the 3x3 subgrid
    start_row, start_col = row - row % 3, col - col % 3  # starting indices of the subgrid
    for i in range(3):
        for j in range(3):
            if grid[i + start_row, j + start_col] == num:
                return False

    # If the number does not exist in the row, column, and 3x3 subgrid, it is valid
    return True


def solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            # If the cell is empty
            if grid[i, j] == 0:
                for num in range(1, 10):  # Try numbers from 1 to 9
                    if is_valid(grid, i, j, num):
                        grid[i, j] = num  # If the number is valid, assign it to the cell

                        # Continue with the next cells
                        if solve_sudoku(grid):
                            return True

                        # If no solution is found, backtrack and try the next number
                        grid[i, j] = 0
                return False  # Backtrack if no number can be assigned to the cell
    return True  # Return True if all cells are filled
