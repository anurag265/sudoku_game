# sudoku_generator.py

from sudoku import Sudoku
from cell import Cell
import random

def has_unique_solution(puzzle):
    """
    Check if the given Sudoku puzzle has a unique solution.

    Args:
    - puzzle: The Sudoku puzzle to check.

    Returns:
    - bool: True if the puzzle has a unique solution, False otherwise.
    """
    solutions = []

    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            solve(board)
                            board[i][j] = 0
                    return
        solutions.append([row[:] for row in board])

    def is_valid(board, row, col, num):
        for x in range(9):
            if board[row][x] == num or board[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    board = [row[:] for row in puzzle.board]
    solve(board)
    return len(solutions) == 1

def create_sudoku_grid():
    """
    Creates a new Sudoku puzzle grid.

    Returns:
    - cells: The initialized cells for the Sudoku puzzle.
    - solution: The solution for the Sudoku puzzle.
    """
    while True:
        # Generate a new random seed to ensure a different puzzle every time
        seed = random.randint(0, 1000000)
        puzzle = Sudoku(3, seed=seed).difficulty(0.5)  # Generate a 9x9 puzzle with 50% cells empty
        solution = puzzle.solve().board  # Get the solved board

        if has_unique_solution(puzzle):
            break

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
