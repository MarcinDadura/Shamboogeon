from classes.game_object import GameObject
import pygame


class Player(GameObject):
    player_sprite = None

    _instance = None

    def __init__(self, x: int, y: int):
        Player._instance = self
        # Load sprite only once
        if Player.player_sprite is None:
            Player.player_sprite = pygame.image.load('img/skull.png').convert_alpha()
        super().__init__(x, y, Player.player_sprite)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # Create instance
            cls(50, 50)
        return cls._instance
