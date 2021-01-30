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
            Player.player_sprite = pygame.image.load('img/player.png').convert_alpha()
        super().__init__(x, y, 12, 12, Player.player_sprite, 'player')

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # Create instance
            cls(50, 50)
        return cls._instance

    def update(self, time_delta, objects):
        keys = pygame.key.get_pressed()
        old_x = self.get_x()
        horizontal_direction = 0
        if keys[K_d]:
            horizontal_direction += 1
        if keys[K_a]:
            horizontal_direction -= 1

        self.set_x(self._x + self.speed * (time_delta/1000) * horizontal_direction)

        for obj in  pygame.sprite.spritecollide(self, objects, dokill=False):
            if obj.type == 'rock':
                if not obj.push(self.speed * (time_delta/1000) * horizontal_direction, 0, objects):
                    self.set_x(old_x)
                    break
            elif obj.type == 'key':
                # Collect key
                obj.kill()
                print('collect')
            elif obj.type == 'door':
                # Collect key
                obj.kill()
                print('open')
            elif obj.type == 'ghost':
                print('ghost!!!')
            else:
                self.set_x(old_x)
                break

        vertical_direction = 0
        if keys[K_s]:
            vertical_direction -= 1
        if keys[K_w]:
            vertical_direction += 1
        old_y = self.get_y()

        self.set_y(self._y - self.speed * (time_delta/1000) * vertical_direction)

        for obj in  pygame.sprite.spritecollide(self, objects, dokill=False):
            if obj.type == 'rock':
                if not obj.push(0, self.speed * (time_delta/1000) * -vertical_direction, objects):
                    self.set_y(old_y)
                    break
            elif obj.type == 'key':
                # Collect key
                print('collect')
            elif obj.type == 'door':
                # Collect key
                obj.kill()
                print('open')
            elif obj.type == 'ghost':
                print('ghost!!!')
            else:
                self.set_y(old_y)
                break

    def check_if_hit_border(self) -> bool:
        if self._x < 0 or self._y < 0 or (self._x + self._width) > (16*16) or (self._y + self._height) > (16*16):
            return True
        return False
