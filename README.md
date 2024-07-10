# Sudoku Game by Anurag using ChatGPT 💗

This project is a Sudoku game built using Python and Pygame, with a graphical user interface. The game generates new Sudoku puzzles every time you play and includes features such as cell highlighting, input validation, and a home screen.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Features

- Generates new Sudoku puzzles each time you play.
- Validates user inputs according to Sudoku rules.
- Highlights selected cells and provides visual feedback for correct and incorrect inputs.
- Home screen with options to start a new game or exit.
- Pause and resume the game using the Esc key.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```sh
   git clone https://github.com/anurag265/sudoku_game.git
   cd sudoku-game
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

5. **Run the game:**

   ```sh
   python game.py
   ```

## Usage

- **Play Game:** From the home screen, click "Play Game" to start a new Sudoku puzzle.
- **Quit Game:** Press the `Esc` key during the game to pause and return to the home screen or quit the game.

## Project Structure

```
sudoku_game/
├── assets/
│   ├── BebasNeue-Regular.ttf
│   ├── home_screen_image.png
│   └── icon.png
├── cell.py
├── events.py
├── game.py
├── home_screen.py
├── sudoku_generator.py
├── utils.py
└── README.md
```

- **assets/**: Contains images, fonts, and icons used in the game.
- **cell.py**: Defines the Cell class representing each cell in the Sudoku grid.
- **events.py**: Handles event processing, including mouse clicks and key presses.
- **game.py**: Entry point for the game. Initializes and runs the main game loop.
- **home_screen.py**: Handles the home screen with the Play Game and Exit options.
- **sudoku_generator.py**: Generates new Sudoku puzzles and initializes the grid.
- **utils.py**: Contains utility functions for drawing the grid and cells.

## Contributing

Contributions are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
