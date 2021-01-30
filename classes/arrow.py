from classes.game_object import GameObject
from classes.player import Player
import pygame


class Arrow(GameObject):
    """It's just a arrow"""

    sprites = None

    def __init__(self, x: int, y: int, horizontal_direction=0, vertical_direction=0):
        # Load sprite only once
        self.speed = 150
        self.horizontal_direction = horizontal_direction
        self.vertical_direction = vertical_direction
        if Arrow.sprites is None:
            Arrow.sprites = [
                pygame.image.load('img/strzala_lewo.png').convert_alpha(),
                pygame.image.load('img/strzala_gora.png').convert_alpha(),
                pygame.image.load('img/strzala_prawo.png').convert_alpha(),
                pygame.image.load('img/strzala_dol.png').convert_alpha(),
            ]
        if horizontal_direction > 0:
            super().__init__(x, y, 16, 16, Arrow.sprites[0], 'arrow')
        elif horizontal_direction < 0:
            super().__init__(x, y, 16, 16, Arrow.sprites[2], 'arrow')
        elif vertical_direction < 0:
            super().__init__(x, y, 16, 16, Arrow.sprites[1], 'arrow')
        else:
            super().__init__(x, y, 16, 16, Arrow.sprites[3], 'arrow')
        self.set_sprite(self.image)

    def update(self, time_delta, objects=None):
        self.set_x(self._x + self.speed * (time_delta/1000) * -self.horizontal_direction)
        self.set_y(self._y + self.speed * (time_delta/1000) * self.vertical_direction)

    @classmethod
    def shoot_arrow(self, horizontal, vertical):
        player = Player.get_instance()
        arrow = Arrow(player.get_x() + (16 * horizontal), player.get_y() + (16 * vertical), -horizontal, vertical)
        return arrow
