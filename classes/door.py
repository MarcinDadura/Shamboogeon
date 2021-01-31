from classes.game_object import GameObject
import pygame
from pygame.sprite import Sprite

class Door(GameObject):
    """It's just a door"""

    right_door_sprite = None
    left_door_sprite = None
    up_door_sprite = None
    down_door_sprite = None
    sound = None

    def __init__(self, x: int, y: int, side='left'):
        # Load sprite only once
        if side == 'left':
            if Door.left_door_sprite is None:
                Door.left_door_sprite = pygame.image.load('img/door_left.png').convert_alpha()
                Door.sound = pygame.mixer.Sound('sounds/drzwi_loch.ogg')
            super().__init__(x, y, 16, 16, Door.left_door_sprite, 'door')

        elif side == 'right':
            if Door.right_door_sprite is None:
                Door.right_door_sprite = pygame.image.load('img/door_right.png').convert_alpha()
                Door.sound = pygame.mixer.Sound('sounds/drzwi_loch.ogg')
            super().__init__(x, y, 16, 16, Door.right_door_sprite, 'door')

        elif side == 'up':
            if Door.right_door_sprite is None:
                Door.up_door_sprite = pygame.image.load('img/door_up.png').convert_alpha()
                Door.sound = pygame.mixer.Sound('sounds/drzwi_loch.ogg')
            super().__init__(x, y, 16, 16, Door.up_door_sprite, 'door')

        elif side == 'down':
            if Door.right_door_sprite is None:
                Door.down_door_sprite = pygame.image.load('img/door_down.png').convert_alpha()
                Door.sound = pygame.mixer.Sound('sounds/drzwi_loch.ogg')
            super().__init__(x, y, 16, 16, Door.down_door_sprite, 'door')
