from classes.game_object import GameObject
import pygame


class Button_rainbow1(GameObject):
    """It's just a rainbow button"""

    button_sprite = None

    def __init__(self, x: int, y: int):
        # Load sprite only once
        self.speed = 10
        if Button_rainbow1.button_sprite is None:
            Button_rainbow1.button_sprite = pygame.image.load('img/button.png').convert_alpha()
        super().__init__(x, y, 16, 16, Button_rainbow1.button_sprite, 'button_rainbow1')

    def is_pushed(self):
        for x in  pygame.sprite.spritecollide(self, GameObject.all_objects, dokill=False):
            if x.type == 'rainbow1':
                return True
        return False
