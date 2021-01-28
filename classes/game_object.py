import pygame
from pygame.sprite import Sprite
from classes.game_state import GameState


class GameObject(Sprite):
    """
    Represents objects in the game
    """

    # Store all created game objects
    all_objects = pygame.sprite.Group()

    def __init__(self, x: float, y: float, sprite: Sprite):
        super().__init__()
        GameObject.all_objects.add(self)
        self._x = x
        self._y = y
        self.image = sprite
        game_state = GameState.get_instance()
        self.rect = (x * game_state.get_board_scale(), y * game_state.get_board_scale())

    @classmethod
    def rescale(cls):
        """
        Change size and position of game objects sprites
        after changing window size
        """
        for obj in cls.all_objects:
            obj.set_x(obj.get_x())
            obj.set_y(obj.get_y())
            obj.image = pygame.transform.scale(obj.image, (16, 16))
            obj.image = pygame.transform.scale(obj.image,
                (
                    16 * GameState.get_instance().get_board_scale(),
                    16 * GameState.get_instance().get_board_scale(),
                )
            )

    @classmethod
    def clear_objects_list(cls):
        cls.all_objects = pygame.sprite.Group()

    def set_x(self, x:int):
        # Change spirte position
        self.rect = (x * GameState.get_instance().get_board_scale(), self.rect[1])
        self._x = x

    def get_x(self) -> int:
        return self._x

    def set_y(self, y:int):
        # Change spirte position
        self.rect = (self.rect[0], y * GameState.get_instance().get_board_scale())
        self._y = y

    def get_y(self) -> int:
        return self._y
