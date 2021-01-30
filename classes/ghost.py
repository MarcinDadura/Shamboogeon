from classes.game_object import GameObject
from classes.player import Player
import pygame


class Ghost(GameObject):
    """It's just a ghost"""

    ghost_sprite = None

    def __init__(self, x: int, y: int):
        # Load sprite only once
        self.speed = 10
        if Ghost.ghost_sprite is None:
            Ghost.ghost_sprite = pygame.image.load('img/ghost.png').convert_alpha()
        super().__init__(x, y, 16, 16, Ghost.ghost_sprite, 'ghost')

    def update(self, time_delta, objects=None):
        player = Player.get_instance()
        p_x = player.get_x()
        p_y = player.get_y()
        horizontal_direction = 0
        vertiacal_direction = 0

        if p_x > self.get_x():
            horizontal_direction = 1
        elif p_x < self.get_x():
            horizontal_direction = -1

        if p_y > self.get_y():
            vertical_direction = 1
        elif p_y < self.get_y():
            vertical_direction = -1

        self.set_x(self._x + self.speed * (time_delta/1000) * horizontal_direction)
        self.set_y(self._y + self.speed * (time_delta/1000) * vertical_direction)
