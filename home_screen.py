"""
home_screen.py

This file handles the home screen of the Sudoku game, featuring an image, title,
and buttons to start the game or exit.
"""

import pygame
import sys
import os

# Constants
WINDOW_SIZE = 450
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SHADOW_COLOR = (50, 50, 50)
BUTTON_COLOR = BLACK
BUTTON_HOVER_COLOR = (70, 70, 70)  # Slightly lighter black for hover effect
BUTTON_TEXT_COLOR = WHITE
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60
FONT_SIZE = 32
SHADOW_OFFSET = 2

# Get the base path of the executable
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()

# Load the home screen image
home_screen_image_path = os.path.join(base_path, 'assets', 'home_screen_image.png')
home_screen_image = pygame.image.load(home_screen_image_path)

# Load the custom font
font_path = os.path.join(base_path, 'assets', 'BebasNeue-Regular.ttf')
title_font_size = 80
button_font_size = 32
title_font = pygame.font.Font(font_path, title_font_size)
button_font = pygame.font.Font(font_path, button_font_size)

# Set up the display
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Sudoku Game")

# Define buttons
play_button_rect = pygame.Rect((WINDOW_SIZE // 2 - BUTTON_WIDTH // 2, 200), (BUTTON_WIDTH, BUTTON_HEIGHT))
exit_button_rect = pygame.Rect((WINDOW_SIZE // 2 - BUTTON_WIDTH // 2, 300), (BUTTON_WIDTH, BUTTON_HEIGHT))

def draw_button(surface, rect, text, font, color, hover_color):
    """
    Draws a button with text and handles hover effect.

    Parameters:
    - surface (Surface): The surface to draw the button on.
    - rect (Rect): The rectangle defining the button's position and size.
    - text (str): The text to display on the button.
    - font (Font): The font of the button text.
    - color (tuple): The color of the button.
    - hover_color (tuple): The color of the button when hovered.
    """
    mouse_pos = pygame.mouse.get_pos()
    button_color = hover_color if rect.collidepoint(mouse_pos) else color
    pygame.draw.rect(surface, button_color, rect, border_radius=10)
    button_text = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = button_text.get_rect(center=rect.center)
    surface.blit(button_text, text_rect)

def draw_home_screen():
    """
    Draws the home screen with the background image, title, and buttons.
    """
    window.fill(WHITE)

    # Scale the background image to fill the screen
    bg_image = pygame.transform.scale(home_screen_image, (WINDOW_SIZE, WINDOW_SIZE))
    window.blit(bg_image, (0, 0))

    # Draw title shadow
    title_shadow = title_font.render("Sudoku", True, SHADOW_COLOR)
    title_shadow_rect = title_shadow.get_rect(center=(WINDOW_SIZE // 2 + SHADOW_OFFSET, 100 + SHADOW_OFFSET))
    window.blit(title_shadow, title_shadow_rect)

    # Draw title
    title = title_font.render("Sudoku", True, WHITE)
    title_rect = title.get_rect(center=(WINDOW_SIZE // 2, 100))
    window.blit(title, title_rect)

    # Draw buttons
    draw_button(window, play_button_rect, "Play Sudoku", button_font, BUTTON_COLOR, BUTTON_HOVER_COLOR)
    draw_button(window, exit_button_rect, "Exit", button_font, BUTTON_COLOR, BUTTON_HOVER_COLOR)

    pygame.display.flip()

def home_screen():
    """
    The home screen function that handles events and updates the display.
    """
    while True:
        draw_home_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = event.pos
                    if play_button_rect.collidepoint(mouse_pos):
                        return "play"  # Start the game
                    elif exit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    home_screen()
