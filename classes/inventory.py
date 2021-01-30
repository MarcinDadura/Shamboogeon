from classes.item import Item
from pygame import Rect
import pygame
from classes.game_object import GameObject


class Inventory(GameObject):
    """
    Inventory Class
    """
    _instance = None

    def __init__(self):
        self.sprite = pygame.image.load('img/inventory_up.png').convert_alpha()
        super().__init__(0, 0, 48, 16, self.sprite)
        self.items = []
        self.size = (96, 128)
        self.x = 0
        self.y = 0
        Inventory._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # Create instance
            cls()
        return cls._instance

    def get_items(self):
        return self.items

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def set_size(self, size: tuple):
        self.size = size

    def get_size(self):
        return self.size

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_sprite(self):
        return self.sprite
