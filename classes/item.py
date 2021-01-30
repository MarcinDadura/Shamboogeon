from pygame.sprite import Sprite
from classes.game_object import GameObject


class Item(GameObject):
    """
        item class
    """

    def __init__(self, title: str, desc: str, sprite: Sprite, x: float, y: float):
        super().__init__(x, y, 16, 16, sprite)
        self.title = title
        self.desc = desc
        self.sprite = sprite

    def get_title(self):
        return self.title

    def get_sprite(self):
        return self.sprite

    def get_desc(self):
        return self.desc
