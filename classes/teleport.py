from classes.game_object import GameObject
import pygame


class Teleport(GameObject):
    """Move player to next lvl"""

    teleport_sprite = None

    def __init__(self, x: int, y: int):
        # Load sprite only once
        if Teleport.teleport_sprite is None:
            Teleport.teleport_sprite = pygame.image.load('img/teleport.png').convert_alpha()
        super().__init__(x, y, 16, 16, Teleport.teleport_sprite)
