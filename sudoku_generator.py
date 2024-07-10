# sudoku_generator.py

from sudoku import Sudoku
from cell import Cell
import random

def create_sudoku_grid():
    """
    Creates a new Sudoku puzzle grid.

    Returns:
    - cells: The initialized cells for the Sudoku puzzle.
    - solution: The solution for the Sudoku puzzle.
    """
    # Generate a new random seed to ensure a different puzzle every time
    seed = random.randint(0, 1000000)
    puzzle = Sudoku(3, seed=seed).difficulty(0.5)  # Generate a 9x9 puzzle with 50% cells empty
    solution = puzzle.solve().board  # Get the solved board

    cells = [
        [Cell(row, col, puzzle.board[row][col] or 0, (200, 200, 200) if puzzle.board[row][col] else (255, 255, 255), not bool(puzzle.board[row][col]))
         for col in range(9)]
        for row in range(9)
    ]

    return cells, solution

def initialize_grid(cells):
    """
    Initialize the grid with the given cells.
    """
    for row in cells:
        for cell in row:
            if cell.number == 0:
                cell.active = True
                cell.color = (255, 255, 255)  # White for empty cells
            else:
                cell.active = False
                cell.color = (200, 200, 200)  # Grey for filled cells
