from pygame.sprite import Sprite
from classes.game_object import GameObject
import pygame


class Trellis_rainbow1(GameObject):
    """It's just a trellis rainbow1"""

    sprite = None

    def __init__(self, x: int, y: int, sprite: Sprite = None):
        # Load sprite only once
        self.sprite = pygame.image.load('img/candy_trelis.png').convert_alpha() if not sprite else sprite
        super().__init__(x, y, 16, 16, self.sprite, 'trellis_rainbow1')
