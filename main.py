import pygame
from classes.game_state import GameState

# Initialize pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("Shamboo")

def main_menu() -> bool:
    """Should return False player when player hits exit button"""
    # TODO
    return True

def game(screen):
    """Main game loop"""
    game_state = GameState.get_instance()
    game_state.reset()
    # TODO

while main_menu():
    game(screen)
