"""
events.py

This file handles all the event processing for the Sudoku game, including mouse clicks,
key presses, and tab navigation.

Functions:
- handle_mouse_click(pos, grid, click_count): Handles mouse click events.
- handle_key_press(cell, grid, row, col, key, solution): Handles key press events.
- handle_tab_key(grid, selected_cell, event): Handles Tab and Shift+Tab key events.
- is_valid_move(grid, row, col, number): Checks if a move is valid based on Sudoku rules.
"""

import pygame
from tkinter import messagebox
from utils import focus_next_active_cell, focus_prev_active_cell, is_grid_complete, draw_cells, draw_grid

def handle_mouse_click(pos, grid, click_count):
    """
    Handles mouse click events to select cells in the grid.

    Parameters:
    - pos (tuple): The position of the mouse click.
    - grid (list): The Sudoku grid.
    - click_count (int): The number of clicks detected.

    Returns:
    - tuple: The row and column of the clicked cell.
    """
    CELL_SIZE = 50
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    if row < 9 and col < 9:
        if click_count == 2:  # Double click detected
            grid[row][col].set_number(0, 0)
        return row, col
    return None

def handle_key_press(cell, grid, row, col, key, solution):
    """
    Handles key press events to enter numbers into the selected cell.

    Parameters:
    - cell (Cell): The currently selected cell.
    - grid (list): The Sudoku grid.
    - row (int): The row index of the selected cell.
    - col (int): The column index of the selected cell.
    - key (int): The key that was pressed.
    - solution (list): The solution to the Sudoku puzzle.
    """
    numpad_keys = {
        pygame.K_KP1: 1,
        pygame.K_KP2: 2,
        pygame.K_KP3: 3,
        pygame.K_KP4: 4,
        pygame.K_KP5: 5,
        pygame.K_KP6: 6,
        pygame.K_KP7: 7,
        pygame.K_KP8: 8,
        pygame.K_KP9: 9,
        pygame.K_KP0: 0,
    }

    if key in range(pygame.K_1, pygame.K_9 + 1):
        number = key - pygame.K_0
    elif key in numpad_keys:
        number = numpad_keys[key]
    else:
        number = None

    if number is not None:
        if number == 0:
            cell.set_number(0, 0)
        else:
            if is_valid_move(grid, row, col, number):
                correct_number = solution[row][col]
                cell.set_number(number, correct_number)
            else:
                # Provide some feedback for invalid moves (optional)
                cell.set_selected(True)

        # Redraw the cells and grid to update the display
        window = pygame.display.get_surface()
        window.fill((255, 255, 255))
        draw_cells(window, grid)
        draw_grid(window)
        pygame.display.flip()

        if is_grid_complete(grid, solution):
            pygame.time.delay(100)  # Small delay to ensure the display updates
            messagebox.showinfo("Congratulations!", "You have completed the Sudoku puzzle!")
            return "home_screen"

def handle_tab_key(grid, selected_cell, event):
    """
    Handles Tab and Shift+Tab key events to navigate between active cells.

    Parameters:
    - grid (list): The Sudoku grid.
    - selected_cell (Cell): The currently selected cell.
    - event (Event): The key event.

    Returns:
    - Cell: The newly selected cell after navigation.
    """
    if selected_cell:
        row, col = selected_cell.row, selected_cell.col
        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
            prev_row, prev_col = focus_prev_active_cell(grid, row, col)
            if prev_row is not None and prev_col is not None:
                selected_cell = grid[prev_row][prev_col]
                selected_cell.set_selected(True)
        else:
            next_row, next_col = focus_next_active_cell(grid, row, col)
            if next_row is not None and next_col is not None:
                selected_cell = grid[next_row][next_col]
                selected_cell.set_selected(True)
    else:
        next_row, next_col = focus_next_active_cell(grid, 0, -1)
        if next_row is not None and next_col is not None:
            selected_cell = grid[next_row][next_col]
            selected_cell.set_selected(True)
    return selected_cell

def is_valid_move(grid, row, col, number):
    """
    Checks if a move is valid based on Sudoku rules.

    Parameters:
    - grid (list): The Sudoku grid.
    - row (int): The row index of the move.
    - col (int): The column index of the move.
    - number (int): The number to be placed in the cell.

    Returns:
    - bool: True if the move is valid, False otherwise.
    """
    # Check the row
    for c in range(9):
        if grid[row][c].number == number:
            return False

    # Check the column
    for r in range(9):
        if grid[r][col].number == number:
            return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c].number == number:
                return False

    return True
