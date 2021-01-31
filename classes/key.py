from classes.game_object import GameObject
import pygame


class Key(GameObject):
    """It's just a key"""
    part = None
    key_sprite_1 = None
    key_sprite_2 = None
    key_sprite_3 = None
    key_sprite_4 = None

    def __init__(self, x: int, y: int, part: int):
        # Load sprite only once
        self.part = part
        if self.part == 1:
            if Key.key_sprite_1 is None:
                Key.key_sprite_1 = pygame.image.load('img/key_1.png').convert_alpha()
            super().__init__(x, y, 16, 16, Key.key_sprite_1, 'key')
        elif self.part == 2:
            if Key.key_sprite_2 is None:
                Key.key_sprite_2 = pygame.image.load('img/key_2.png').convert_alpha()
            super().__init__(x, y, 16, 16, Key.key_sprite_2, 'key')
        elif self.part == 3:
            if Key.key_sprite_3 is None:
                Key.key_sprite_3 = pygame.image.load('img/key_3.png').convert_alpha()
            super().__init__(x, y, 16, 16, Key.key_sprite_3, 'key')
        else:
            if Key.key_sprite_4 is None:
                Key.key_sprite_4 = pygame.image.load('img/key_4.png').convert_alpha()
            super().__init__(x, y, 16, 16, Key.key_sprite_4, 'key')
