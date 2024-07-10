"""
game.py

This file serves as the entry point for the Sudoku game. It initializes the game,
sets up the display, and contains the main game loop. It handles user inputs and
updates the game state accordingly.

Functions:
- main(): The main function that runs the game loop.
"""

import pygame
import sys
from sudoku_generator import create_sudoku_grid, initialize_grid
from events import handle_mouse_click, handle_key_press, handle_tab_key
from utils import draw_grid, draw_cells
from home_screen import home_screen
from tkinter import Tk, messagebox
import os

# Constants
WINDOW_SIZE = 450
WHITE = (255, 255, 255)

# Get the base path of the executable
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()

# Load and set the window icon
icon_path = os.path.join(base_path, 'assets', 'icon.png')
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

# Set up the display
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Sudoku by Anurag using ChatGPT 💗")

# Initialize Tkinter (used for messagebox)
root = Tk()
root.withdraw()  # Hide the root window

def main():
    """
    The main function that initializes the game, sets up the grid, and runs the
    game loop. It handles user inputs and updates the display.
    """
    while True:
        # Show the home screen
        if home_screen() != "play":
            return

        # Generate a new puzzle every time we enter the game loop
        cells, solution = create_sudoku_grid()
        initialize_grid(cells)
        selected_cell = None
        click_count = 0
        last_click_time = 0

        # Main loop
        game_running = True
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    current_time = pygame.time.get_ticks()
                    if current_time - last_click_time < 500:  # Double click detected within 500 ms
                        click_count += 1
                    else:
                        click_count = 1
                    last_click_time = current_time

                    cell_pos = handle_mouse_click(pos, cells, click_count)
                    if cell_pos:
                        if selected_cell:
                            selected_cell.set_selected(False)
                        row, col = cell_pos
                        selected_cell = cells[row][col] if cells[row][col].active else None
                        if selected_cell:
                            selected_cell.set_selected(True)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        if selected_cell:
                            selected_cell.set_selected(False)
                        selected_cell = handle_tab_key(cells, selected_cell, event)
                    elif event.key == pygame.K_ESCAPE:
                        # Show quit confirmation pop-up
                        if messagebox.askyesno("Quit", "Do you want to quit the game?"):
                            game_running = False  # Exit to home screen
                    elif selected_cell:
                        result = handle_key_press(selected_cell, cells, selected_cell.row, selected_cell.col, event.key, solution)
                        if result == "home_screen":
                            game_running = False

            # Fill the background
            window.fill(WHITE)

            # Draw the cells
            draw_cells(window, cells)

            # Draw the grid
            draw_grid(window)

            # Update the display
            pygame.display.flip()

if __name__ == "__main__":
    main()
