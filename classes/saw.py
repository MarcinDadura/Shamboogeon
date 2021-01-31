from classes.game_object import GameObject
import pygame


class Saw(GameObject):
    """It's just a saw"""

    saw_sprite = None
    sound = None

    def __init__(self, x: int, y: int, horizontal=True):
        # Load sprite only once
        self.horizontal = horizontal
        self.direction = 1
        self.speed = 50
        if Saw.saw_sprite is None:
            Saw.saw_sprite = pygame.image.load('img/saw.png').convert_alpha()
            Saw.sound = pygame.mixer.Sound('sounds/kamyk.ogg')
        super().__init__(x, y, 16, 16, Saw.saw_sprite, 'saw')

    def update(self, time_delta, objects=None):
        if objects is None:
            return
        movement = self.speed * (time_delta/1000)

        old_x = self.get_x()
        old_y = self.get_y()

        if self.horizontal:
            self.set_x(self.get_x() + movement * self.direction)
        else:
            self.set_y(self.get_y() + movement * self.direction)

        for obj in  pygame.sprite.spritecollide(self, objects, dokill=False):
            if obj.type == 'wall':
                self.set_x(old_x)
                self.set_y(old_y)
                self.direction = -self.direction
