import pygame
from pygame import Rect
from pygame.sprite import Sprite
from classes.game_state import GameState


class GameObject(Sprite):
    """
    Represents objects in the game
    """

    # Store all created game objects
    all_objects = pygame.sprite.Group()

    def __init__(self, x: float, y: float, width: int, height: int, sprite: Sprite, object_type=''):
        super().__init__()
        GameObject.all_objects.add(self)
        self._x = x
        self._y = y
        self._width = width 
        self._height = height 
        self.image = sprite
        self.type = object_type
        self.cary = False
        scale = GameState.get_instance().get_board_scale()
        self.rect = Rect((x * scale, y * scale, width * scale, height * scale))

    @classmethod
    def rescale(cls):
        """
        Change size and position of game objects sprites
        after changing window size
        """
        for obj in cls.all_objects:
            obj.set_x(obj.get_x())
            obj.set_y(obj.get_y())
            obj.image = pygame.transform.scale(obj.image, (obj._width, obj._height))
            obj.image = pygame.transform.scale(obj.image,
                (
                    obj._width * GameState.get_instance().get_board_scale(),
                    obj._height * GameState.get_instance().get_board_scale(),
                )
            )

    @classmethod
    def remove_object(cls, obj):
        cls.all_objects.remove(obj)

    @classmethod
    def clear_objects_list(cls):
        old = cls.all_objects
        cls.all_objects = pygame.sprite.Group()
        for x in old:
            if x.type == 'player':
                cls.all_objects.add(x)

    def set_x(self, x: float):
        # Change spirte position
        scale = GameState.get_instance().get_board_scale()
        self.rect = Rect(x * scale, self._y * scale, self._width * scale, self._height * scale)
        self._x = x

    def get_x(self) -> int:
        return self._x

    def set_y(self, y: float):
        # Change sprite position
        scale = GameState.get_instance().get_board_scale()
        self.rect = Rect(self._x * scale, y * scale, self._width * scale, self._height * scale)
        self._y = y

    def get_y(self) -> int:
        return self._y

    def set_sprite(self, sprite):
        self.image = sprite
        self.set_x(self.get_x())
        self.set_y(self.get_y())
        self.image = pygame.transform.scale(self.image, (self._width, self._height))
        self.image = pygame.transform.scale(self.image,
                                           (
                                               self._width * GameState.get_instance().get_board_scale(),
                                               self._height * GameState.get_instance().get_board_scale(),
                                           )
                                           )
