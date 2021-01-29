from classes.game_object import GameObject
import pygame
from pygame.locals import *


class Player(GameObject):
    player_sprite = None

    _instance = None

    def __init__(self, x: int, y: int):
        Player._instance = self
        self.speed = 100
        # Load sprite only once
        if Player.player_sprite is None:
            Player.player_sprite = pygame.image.load('img/skull.png').convert_alpha()
        super().__init__(x, y, 16, 16, Player.player_sprite)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # Create instance
            cls(50, 50)
        return cls._instance

    def update(self, time_delta, objects):
        keys = pygame.key.get_pressed()
        old_x = self.get_x()
        if keys[K_RIGHT]:
            self.set_x(self._x + self.speed * (time_delta/1000))
        if keys[K_LEFT]:
            self.set_x(self._x - self.speed * (time_delta/1000))
        if pygame.sprite.spritecollideany(self, objects):
            self.set_x(old_x)

        old_y = self.get_y()
        if keys[K_UP]:
            self.set_y(self._y - self.speed * (time_delta/1000))
        if keys[K_DOWN]:
            self.set_y(self._y + self.speed * (time_delta/1000))
        if pygame.sprite.spritecollideany(self, objects):
            self.set_y(old_y)

    def check_if_hit_border(self) -> bool:
        if self._x < 0 or self._y < 0 or (self._x + self._width) > (16*16) or (self._y + self._height) > (16*16):
            return True
        return False
