from pygame.sprite import Sprite


class GameObject(Sprite):
    def __init__(self, x: int, y:int, height: int, width: int, sprite: Sprite):
        super().__init__()
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._sprite = sprite

    def set_x(self, x:int):
        self._x = x

    def get_x(self) -> int:
        return self._x

    def set_y(self, y:int):
        self._y = y

    def get_y(self) -> int:
        return self._y

    def set_width(self, width:int):
        self._width = width 

    def get_width(self) -> int:
        return self._width

    def set_height(self, height:int):
        self._height = height

    def get_hieght(self) -> int:
        return self._height
