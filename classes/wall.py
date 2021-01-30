from classes.game_object import GameObject
import pygame


class Wall(GameObject):
    """It's just a wall"""

    wall_sprite = None

    def __init__(self, x: int, y: int):
        # Load sprite only once
        if Wall.wall_sprite is None:
            Wall.wall_sprite = pygame.image.load('img/wall.png').convert_alpha()
        super().__init__(x, y, 16, 16, Wall.wall_sprite, 'wall')
