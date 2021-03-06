from classes.game_object import GameObject
from classes.player import Player
from classes.inventory import Inventory
import pygame
from classes.monster import Monster
from classes.ghost import Ghost
from classes.item import Item
from classes.game_state import GameState
from classes.inventory import Inventory

class Arrow(GameObject):
    """It's just a arrow"""

    sprites = None
    luk_sound = None

    def __init__(self, x: int, y: int, horizontal_direction=0, vertical_direction=0):
        # Load sprite only once
        self.speed = 150
        self.horizontal_direction = horizontal_direction
        self.vertical_direction = vertical_direction
        self.st = 0
        Arrow.luk_sound = pygame.mixer.Sound('sounds/łuk_strzał.ogg')
        if Arrow.sprites is None:
            Arrow.sprites = [
                pygame.image.load('img/strzala_lewo.png').convert_alpha(),
                pygame.image.load('img/strzala_gora.png').convert_alpha(),
                pygame.image.load('img/strzala_prawo.png').convert_alpha(),
                pygame.image.load('img/strzala_dol.png').convert_alpha(),
            ]
        if horizontal_direction > 0:
            super().__init__(x, y, 8, 8, Arrow.sprites[0], 'arrow')
            self.st = 0
        elif horizontal_direction < 0:
            super().__init__(x, y, 8, 8, Arrow.sprites[2], 'arrow')
            self.st = 2
        elif vertical_direction < 0:
            super().__init__(x, y, 8, 8, Arrow.sprites[1], 'arrow')
            self.st = 1
        else:
            super().__init__(x, y, 8, 8, Arrow.sprites[3], 'arrow')
            self.st = 3
        self.set_sprite(self.image)

    def update(self, time_delta, objects=None):
        game_state = GameState.get_instance()
        self.set_x(self._x + self.speed * (time_delta/1000) * -self.horizontal_direction)
        self.set_y(self._y + self.speed * (time_delta/1000) * self.vertical_direction)
        if objects:
            for obj in  pygame.sprite.spritecollide(self, objects, dokill=False):
                if isinstance(obj, Ghost) or isinstance(obj, Monster):
                    if isinstance(obj, Monster) and obj.name == 'dr_pehape':
                            game_state.boss_hp -= 1
                            if game_state.boss_hp <= 0:
                                obj.kill()
                                for i in objects:
                                    if i.type == 'trellis':
                                        i.kill()
                            self.horizontal_direction = -self.horizontal_direction                            
                            self.vertical_direction = -self.vertical_direction
                            try:
                                self.image = Arrow.sprites[self.st+2]
                            except IndexError:
                                self.image = Arrow.sprites[self.st-2]
                            self.set_sprite(self.image)
                    elif self.horizontal_direction != 0 or self.vertical_direction != 0:
                        obj.sound.play()
                        obj.kill()
                        self.horizontal_direction = 0
                        self.vertical_direction = 0
                elif obj.type == 'wall' or obj.type == 'door' or obj.type == 'rock':
                    self.horizontal_direction = 0
                    self.vertical_direction = 0
        if self.get_y() <= 0 or self.get_y() >= 256  or self._width <= 0 or self._width >= 256:
            self.horizontal_direction = 0
            self.vertical_direction = 0
            self.set_x(self._x)
            self.set_y(self._y - 16 if self._y > 0 else self._y + 16)
        elif self._height <= 0 or self._height >= 256 or self.get_x() <= 0 or self.get_x() >= 256:
            self.horizontal_direction = 0
            self.vertical_direction = 0
            self.set_x(self._x - 16 if self._x > 0 else self._x + 16)
            self.set_y(self._y)

    @classmethod
    def shoot_arrow(self, horizontal, vertical):
        if Inventory.get_instance().get_arrow():
            player = Player.get_instance()
            arrow = Arrow(player.get_x() + (16 * horizontal), player.get_y() + (16 * vertical), -horizontal, vertical)
            for obj in  pygame.sprite.spritecollide(arrow, GameObject.all_objects, dokill=False):
                if obj.type == 'wall':
                    item = Item("arrow", "arrow", pygame.image.load('img/strzala_prawo.png'), 0, 0)
                    Inventory.get_instance().add_item(item)
                    return None
            self.luk_sound = Arrow.luk_sound.play()
            return arrow
