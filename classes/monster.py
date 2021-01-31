
from classes.player import Player
import pygame
from pygame.sprite import Sprite

from classes.game_object import GameObject

class Monster(GameObject):
    """Monster abstract obj"""

    sprite = None
    sound = None
    horizontal_direction = 0
    vertical_direction = 0

    def __init__(self, x: int, y: int, speed: int ,sound_path: str, sprite_path: str, obj_name: str, max_s: int ):
        # Load sprite only once
        self.speed = speed
        self.count = 0
        self.name = obj_name
        self.max = max_s
        self.sprite = pygame.image.load(sprite_path.format(self.count)).convert_alpha()
        Monster.sound = pygame.mixer.Sound(sound_path)
        self.sound = Monster.sound
        super().__init__(x, y, 16, 16, self.sprite, 'monster')

    def update(self, time_delta, objects):
        old_x = self.get_x()
        old_y = self.get_y()
        if self.count % 20 == 0:
            self.set_sprite(pygame.image.load('img/{}_{}.png'.format(self.name, self.count // 20)).convert_alpha())

        player = Player.get_instance()
        p_x = player.get_x()
        p_y = player.get_y()
        self.horizontal_direction = 0
        self.vertical_direction = 0

        if p_x > self.get_x():
            self.horizontal_direction = 1
        elif p_x < self.get_x():
            self.horizontal_direction = -1

        if p_y > self.get_y():
            self.vertical_direction = 1
        elif p_y < self.get_y():
            self.vertical_direction = -1


        self.count = self.count + 1 if self.count < self.max*20 else 0


        self.set_x(self._x + self.speed * (time_delta / 1000) * self.horizontal_direction)
        for obj in pygame.sprite.spritecollide(self, objects, dokill=False):
            if obj.type == 'rock' or obj.type == 'wall':
                self.horizontal_direction = -self.horizontal_direction
                self.set_x(old_x)
                break
        #self.set_x(self._x + self.speed * (time_delta / 1000) * self.horizontal_direction)

        self.set_y(self._y + self.speed * (time_delta / 1000) * self.vertical_direction)
        for obj in pygame.sprite.spritecollide(self, objects, dokill=False):
            if obj.type == 'rock' or obj.type == 'wall':
                    self.vertical_direction = -self.vertical_direction
                    self.set_y(old_y)
                    break
        #self.set_y(self._y + self.speed * (time_delta / 1000) * self.vertical_direction)

