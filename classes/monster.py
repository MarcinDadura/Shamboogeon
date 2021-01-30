from classes.game_object import GameObject
from classes.player import Player
import pygame


class Monster(GameObject):
    """Monster abstract obj"""

    sprite = None
    sound = None

    def __init__(self, x: int, y: int, speed: int ,sound_path: str, sprite_path: str, obj_name: str, max_s: int ):
        # Load sprite only once
        self.speed = speed
        self.count = 0
        self.name = obj_name
        self.max = max_s
        if Monster.sprite is None:
            Monster.sprite = pygame.image.load(sprite_path.format(self.count)).convert_alpha()
            Monster.sound = pygame.mixer.Sound(sound_path)
        self.sound = Monster.sound
        super().__init__(x, y, 16, 16, Monster.sprite, obj_name)

    def update(self, time_delta, objects=None):
        self.set_sprite(pygame.image.load('img/{}_{}.png'.format(self.name, self.count)).convert_alpha())
        player = Player.get_instance()
        p_x = player.get_x()
        p_y = player.get_y()
        horizontal_direction = 0
        vertical_direction = 0

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
        self.count = self.count + 1 if self.count < self.max else 0
