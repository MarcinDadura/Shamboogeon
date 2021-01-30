from classes.game_object import GameObject
import pygame


class Button(GameObject):
    """It's just a button"""

    button_sprite = None

    def __init__(self, x: int, y: int):
        # Load sprite only once
        self.speed = 10
        if Button.button_sprite is None:
            Button.button_sprite = pygame.image.load('img/button.png').convert_alpha()
        super().__init__(x, y, 16, 16, Button.button_sprite, 'button')
