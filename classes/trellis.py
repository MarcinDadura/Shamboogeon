from classes.game_object import GameObject
import pygame


class Trellis(GameObject):
    """It's just a trellis"""

    sprite = None

    def __init__(self, x: int, y: int):
        # Load sprite only once
        if Trellis.sprite is None:
            Trellis.sprite = pygame.image.load('img/krata.png').convert_alpha()
        super().__init__(x, y, 16, 16, Trellis.sprite, 'trellis')
