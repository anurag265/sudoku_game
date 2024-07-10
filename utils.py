"""
utils.py

This file contains utility functions for the Sudoku game, including drawing the grid,
drawing cells, and focusing on the next or previous active cell.

Functions:
- draw_grid(window): Draws the Sudoku grid.
- draw_cells(window, grid): Draws the cells of the Sudoku grid.
- focus_next_active_cell(grid, current_row, current_col): Finds the next active cell.
- focus_prev_active_cell(grid, current_row, current_col): Finds the previous active cell.
- is_grid_complete(grid, solution): Checks if the grid is complete and correct.
"""

import pygame


def draw_grid(window):
    """
    Draws the Sudoku grid.

    Parameters:
    - window (Surface): The Pygame surface to draw on.
    """
    CELL_SIZE = 50
    BOLD_LINE_WIDTH = 5
    THIN_LINE_WIDTH = 2
    BLACK = (0, 0, 0)

    for row in range(10):
        line_width = BOLD_LINE_WIDTH if row % 3 == 0 else THIN_LINE_WIDTH
        pygame.draw.line(window, BLACK, (0, row * CELL_SIZE), (450, row * CELL_SIZE), line_width)
        pygame.draw.line(window, BLACK, (row * CELL_SIZE, 0), (row * CELL_SIZE, 450), line_width)


def draw_cells(window, grid):
    """
    Draws the cells of the Sudoku grid.

    Parameters:
    - window (Surface): The Pygame surface to draw on.
    - grid (list): The Sudoku grid.
    """
    for row in range(9):
        for col in range(9):
            grid[row][col].draw(window)


def focus_next_active_cell(grid, current_row, current_col):
    """
    Finds the next active cell in the grid.

    Parameters:
    - grid (list): The Sudoku grid.
    - current_row (int): The current row index.
    - current_col (int): The current column index.

    Returns:
    - tuple: The row and column of the next active cell.
    """
    for row in range(current_row, 9):
        for col in range(current_col + 1, 9):
            if grid[row][col].active:
                return row, col
        current_col = -1  # Reset column index after finishing the current row

    for row in range(current_row + 1):
        for col in range(9):
            if grid[row][col].active:
                return row, col

    return None, None


def focus_prev_active_cell(grid, current_row, current_col):
    """
    Finds the previous active cell in the grid.

    Parameters:
    - grid (list): The Sudoku grid.
    - current_row (int): The current row index.
    - current_col (int): The current column index.

    Returns:
    - tuple: The row and column of the previous active cell.
    """
    for row in range(current_row, -1, -1):
        for col in range(current_col - 1, -1, -1):
            if grid[row][col].active:
                return row, col
        current_col = 9  # Reset column index after finishing the current row

    for row in range(8, current_row, -1):
        for col in range(8, -1, -1):
            if grid[row][col].active:
                return row, col

    return None, None


def is_grid_complete(grid, solution):
    """
    Checks if the grid is complete and correct.

    Parameters:
    - grid (list): The Sudoku grid.
    - solution (list): The solution to the Sudoku puzzle.

    Returns:
    - bool: True if the grid is complete and correct, False otherwise.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col].number != solution[row][col]:
                return False
    return True
