from classes.game_object import GameObject
import pygame


class Rock(GameObject):
    """It's just a rock"""

    rock_sprite = None

    def __init__(self, x: int, y: int):
        # Load sprite only once
        if Rock.rock_sprite is None:
            Rock.rock_sprite = pygame.image.load('img/skull.png').convert_alpha()
        super().__init__(x, y, 16, 16, Rock.rock_sprite, 'rock')

    def try_to_move(self, horizontal: float, vertiacal: float, objects):
        """Return True on success"""
        old_x = self.get_x()
        old_y = self.get_y()
        self.set_x(self.get_x() + horizontal)
        self.set_y(self.get_y() + vertiacal)
        for x in  pygame.sprite.spritecollide(self, objects, dokill=False):
            if x.type != 'player' and x is not self:
                self.set_x(old_x)
                self.set_y(old_y)
                return False
        return True
