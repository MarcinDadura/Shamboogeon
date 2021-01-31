from classes.game_object import GameObject
import pygame
from pygame.sprite import Sprite


class Wall(GameObject):
    """It's just a wall"""

    wall_sprite = None

    def __init__(self, x: int, y: int, sprite: Sprite = None, type: str = ""):
        # Load sprite only once
        if type != "rocket":
            self.type = 'wall'
            self.wall_sprite = pygame.image.load('img/wall.png').convert_alpha() if sprite is None else sprite
            super().__init__(x, y, 16, 16, self.wall_sprite, 'wall')
        else:
            self.type = type
            self.wall_sprite = pygame.image.load('img/wall.png').convert_alpha() if sprite is None else sprite
            super().__init__(x, y, 16, 16, self.wall_sprite, type)
