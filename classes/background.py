from classes.game_object import GameObject
import pygame
from pygame.sprite import Sprite


class Background(GameObject):
    """It's just a wall"""

    sprite = None

    def __init__(self, x: int, y: int, sprite: Sprite = None):
        # Load sprite only once
        self.sprite = pygame.image.load('img/dungeon_background.png').convert_alpha() if sprite is None else sprite
        super().__init__(x, y, 16, 16, self.sprite, 'background')
