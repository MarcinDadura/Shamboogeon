from classes.game_object import GameObject
import pygame


class Rainbow_2(GameObject):
    """It's just a rainbow"""

    rainbow_sprite = None
    sound = None

    def __init__(self, x: int, y: int):
        # Load sprite only once
        self.direction = [0, 0]
        self.speed = 150
        if Rainbow_2.rainbow_sprite is None:
            Rainbow_2.rainbow_sprite = pygame.image.load('img/candy_rainbow_wall2.png').convert_alpha()
            #Rainbow.rainbow_sprite = pygame.mixer.Sound('/')
        super().__init__(x, y, 14, 14, Rainbow_2.rainbow_sprite, 'rainbow2')

    def push(self, horizontal: float, vertiacal: float, objects):
        """Return True on success"""
        #self.sound = Rainbow.sound.play()
        old_x = self.get_x()
        old_y = self.get_y()
        self.set_x(self.get_x() + horizontal)
        self.set_y(self.get_y() + vertiacal)
        for x in pygame.sprite.spritecollide(self, objects, dokill=False):
            if x.type == 'wall':
                self.set_x(old_x)
                self.set_y(old_y)
                self.direction = [0, 0]


            if x.type == 'rainbow1':
                self.set_x(old_x)
                self.set_y(old_y)
                self.direction = [0, 0]


            if x.type == 'button_rainbow1':
                self.set_x(old_x)
                self.set_y(old_y)
                self.direction = [0, 0]


            if x.type == 'button_rainbow2':
                self.direction = [0, 0]
                self.set_x(x.get_x() + 1)
                self.set_y(x.get_y() + 1)
                if self.sound is not None:
                    self.sound.stop()
                open_the_trellis = True
                for x in GameObject.all_objects:
                    if x.type == 'button_rainbow2':
                        if not x.is_pushed():
                            open_the_trellis = False

                if open_the_trellis:
                    for x in GameObject.all_objects:
                        if x.type == 'trellis_rainbow2' or x.type =='button_rainbow2' :
                            x.kill()

    def update(self, time_delta, objects=None):
        old_x = self.get_x()
        old_y = self.get_y()
        self.set_x(old_x)
        self.set_y(old_y)
        self.direction = [0, 0]
    """
        if self.sound is not None:
            self.sound.stop()
    """