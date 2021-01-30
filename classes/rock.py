from classes.game_object import GameObject
import pygame


class Rock(GameObject):
    """It's just a rock"""

    rock_sprite = None
    sound = None

    def __init__(self, x: int, y: int):
        # Load sprite only once
        self.direction = [0, 0]
        self.speed = 150
        if Rock.rock_sprite is None:
            Rock.rock_sprite = pygame.image.load('img/kamien.png').convert_alpha()
            Rock.sound = pygame.mixer.Sound('sounds/kamyk.ogg')
        super().__init__(x, y, 14, 14, Rock.rock_sprite, 'rock')

    def push(self, horizontal: float, vertiacal: float, objects):
        """Return True on success"""
        self.sound = Rock.sound.play()
        old_x = self.get_x()
        old_y = self.get_y()
        self.set_x(self.get_x() + horizontal)
        self.set_y(self.get_y() + vertiacal)
        if horizontal > 0:
            self.direction[0] = 1
        if horizontal < 0:
            self.direction[0] = -1
        if vertiacal > 0:
            self.direction[1] = 1
        if vertiacal < 0:
            self.direction[1] = -1
        for x in  pygame.sprite.spritecollide(self, objects, dokill=False):
            if x.type != 'player' and x is not self:
                self.set_x(old_x)
                self.set_y(old_y)
                return False
        return True

    def update(self, time_delta, objects=None):
        if objects is None:
            return
        movement = self.speed * (time_delta/1000)

        old_x = self.get_x()
        old_y = self.get_y()

        self.set_x(self.get_x() + movement * self.direction[0])
        self.set_y(self.get_y() + movement * self.direction[1])

        for obj in  pygame.sprite.spritecollide(self, objects, dokill=False):
            if obj.type == 'button':
                self.direction = [0, 0]
                self.set_x(obj.get_x() + 1)
                self.set_y(obj.get_y() + 1)
                if self.sound is not None:
                    self.sound.stop()
                open_the_trellis = True
                for x in GameObject.all_objects:
                    if x.type == 'button':
                        if not x.is_pushed():
                            open_the_trellis = False
                
                if open_the_trellis:
                    for x in GameObject.all_objects:
                        if x.type == 'trellis':
                            x.kill()



            elif obj.type != 'player' and obj is not self:
                self.set_x(old_x)
                self.set_y(old_y)
                self.direction = [0, 0]
                if self.sound is not None:
                    self.sound.stop()
