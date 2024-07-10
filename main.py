import pygame
import sys
from sudoku_generator import create_sudoku_grid, initialize_grid, is_valid_move, get_correct_number, is_grid_complete
from tkinter import Tk, messagebox

# Constants
WINDOW_SIZE = 450
GRID_SIZE = 9
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
BOLD_LINE_WIDTH = 5
THIN_LINE_WIDTH = 2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("9x9 Grid with Cells")

# Initialize Tkinter (used for messagebox)
root = Tk()
root.withdraw()  # Hide the root window

def draw_grid():
    for row in range(GRID_SIZE + 1):
        line_width = BOLD_LINE_WIDTH if row % 3 == 0 else THIN_LINE_WIDTH
        pygame.draw.line(window, BLACK, (0, row * CELL_SIZE), (WINDOW_SIZE, row * CELL_SIZE), line_width)
        pygame.draw.line(window, BLACK, (row * CELL_SIZE, 0), (row * CELL_SIZE, WINDOW_SIZE), line_width)

def draw_cells(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            grid[row][col].draw(window)

def handle_mouse_click(pos, grid, click_count):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    if row < GRID_SIZE and col < GRID_SIZE:
        if click_count == 2:  # Double click detected
            grid[row][col].set_number(0, 0)
        return row, col
    return None

def handle_key_press(cell, grid, row, col, key, solution):
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
                correct_number = get_correct_number(solution, row, col)
                cell.set_number(number, correct_number)

                # Redraw the cells and grid to update the display
                window.fill(WHITE)
                draw_cells(grid)
                draw_grid()
                pygame.display.flip()

                if is_grid_complete(grid, solution):
                    pygame.time.delay(100)  # Small delay to ensure the display updates
                    messagebox.showinfo("Congratulations!", "You have completed the Sudoku puzzle!")

def focus_next_active_cell(grid, current_row, current_col):
    for row in range(current_row, GRID_SIZE):
        for col in range(current_col + 1, GRID_SIZE):
            if grid[row][col].active:
                return row, col
        current_col = -1  # Reset column index after finishing the current row

    for row in range(current_row + 1):
        for col in range(GRID_SIZE):
            if grid[row][col].active:
                return row, col

    return None, None

def focus_prev_active_cell(grid, current_row, current_col):
    for row in range(current_row, -1, -1):
        for col in range(current_col - 1, -1, -1):
            if grid[row][col].active:
                return row, col
        current_col = GRID_SIZE  # Reset column index after finishing the current row

    for row in range(GRID_SIZE - 1, current_row, -1):
        for col in range(GRID_SIZE - 1, -1, -1):
            if grid[row][col].active:
                return row, col

    return None, None

def main():
    # Initialize the grid with a new Sudoku puzzle
    cells, solution = create_sudoku_grid()
    initialize_grid(cells)
    selected_cell = None
    click_count = 0
    last_click_time = 0

    # Main loop
    while True:
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
                if selected_cell:
                    if event.key == pygame.K_TAB:
                        if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            selected_cell.set_selected(False)
                            row, col = selected_cell.row, selected_cell.col
                            prev_row, prev_col = focus_prev_active_cell(cells, row, col)
                            if prev_row is not None and prev_col is not None:
                                selected_cell = cells[prev_row][prev_col]
                                selected_cell.set_selected(True)
                        else:
                            selected_cell.set_selected(False)
                            row, col = selected_cell.row, selected_cell.col
                            next_row, next_col = focus_next_active_cell(cells, row, col)
                            if next_row is not None and next_col is not None:
                                selected_cell = cells[next_row][next_col]
                                selected_cell.set_selected(True)
                    else:
                        handle_key_press(selected_cell, cells, selected_cell.row, selected_cell.col, event.key, solution)

        # Fill the background
        window.fill(WHITE)

        # Draw the cells
        draw_cells(cells)

        # Draw the grid
        draw_grid()

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
