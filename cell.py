"""
cell.py

This file defines the Cell class, which represents a single cell in the Sudoku grid.
Each cell has properties such as its number, color, and whether it is active or selected.

Class:
- Cell: Represents a single cell in the Sudoku grid.
"""

import pygame

# Constants
CELL_SIZE = 50
FONT_SIZE = 32
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
MUTED_RED = (255, 102, 102)  # Muted red

class Cell:
    """
    Represents a single cell in the Sudoku grid.

    Attributes:
    - row (int): The row index of the cell.
    - col (int): The column index of the cell.
    - number (int): The number displayed in the cell.
    - color (tuple): The background color of the cell.
    - active (bool): Whether the cell is active (editable) or inactive (fixed).
    - selected (bool): Whether the cell is currently selected.
    """
    def __init__(self, row, col, number, color, active):
        self.row = row
        self.col = col
        self.number = number
        self.color = color
        self.active = active
        self.selected = False

    def draw(self, surface):
        """
        Draws the cell on the given surface.

        Parameters:
        - surface (Surface): The Pygame surface to draw on.
        """
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE
        if self.selected:
            pygame.draw.rect(surface, SKY_BLUE, (x, y, CELL_SIZE, CELL_SIZE))
        else:
            pygame.draw.rect(surface, self.color, (x, y, CELL_SIZE, CELL_SIZE))
        if self.number != 0:
            font = pygame.font.SysFont(None, FONT_SIZE)
            text = font.render(str(self.number), True, BLACK)
            text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
            surface.blit(text, text_rect)

    def set_number(self, number, correct_number):
        """
        Sets the number in the cell and updates its background color.

        Parameters:
        - number (int): The number to set in the cell.
        - correct_number (int): The correct number for the cell.
        """
        if self.active:
            self.number = number
            if number == 0:
                self.color = WHITE
            elif number == correct_number:
                self.color = GREEN
            else:
                self.color = MUTED_RED

    def set_selected(self, selected):
        """
        Sets the selected state of the cell.

        Parameters:
        - selected (bool): Whether the cell is selected or not.
        """
        if self.active:
            self.selected = selected
