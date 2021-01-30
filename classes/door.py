from classes.game_object import GameObject
import pygame


class Door(GameObject):
    """It's just a door"""

    right_door_sprite = None
    left_door_sprite = None
    sound = None

    def __init__(self, x: int, y: int, side='left'):
        # Load sprite only once
        if side == 'left':
            if Door.left_door_sprite is None:
                Door.left_door_sprite = pygame.image.load('img/door_left.png').convert_alpha()
                Door.sound = pygame.mixer.Sound('sounds/drzwi_loch.ogg')
            super().__init__(x, y, 16, 16, Door.left_door_sprite, 'door')
        else:
            if Door.right_door_sprite is None:
                Door.right_door_sprite = pygame.image.load('img/door_right.png').convert_alpha()
                Door.sound = pygame.mixer.Sound('sounds/drzwi_loch.ogg')
            super().__init__(x, y, 16, 16, Door.right_door_sprite, 'door')
