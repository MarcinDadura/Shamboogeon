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
        self.size = (48, 1024)
        self.x = 0
        self.y = 0
        self.i_y = 16
        self.count = 0
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
        x = 0 if self.count % 2 == 0 else 16
        self.i_y = self.i_y + 16 if self.count != 0 and self.count % 2 == 0 else self.i_y
        item.set_x(x)
        item.set_y(self.i_y)

        self.items.append(item)
        self.count += 1

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

    def unitKey(self):
        key1 = False
        key2 = False

        for o in self.items:
            if o.title == "key_1":
                key1 = True
            elif o.title == "key_2":
                key2 = True

        if key2 and key1:
            items = []
            for o in self.items:
                if o.title != "key_1" and o.title != "key_2":
                    items.append(o)

            self.items = items

            self.add_item(Item("key_unit", "key", pygame.image.load("img/klucz.png").convert_alpha(),  0, 0, 16, 16))

            self.itemsSize()
            print(self.items)

    def itemsSize(self):
        count = 0
        for o in self.items:
            x = 0 if count % 2 == 0 else 16
            y = 16
            y = y + 16 if count != 0 and self.count % 2 == 0 else y
            o.set_x(x)
            o.set_y(y)
            count = count + 1

    def checkKey(self):
        for o in self.items:
            if o.title == "key_unit":
                return True

        return False
