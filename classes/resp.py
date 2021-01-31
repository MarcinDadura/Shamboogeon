from classes.game_object import GameObject
from classes.game_state import GameState
from classes.ghost import Ghost
import pygame
from pygame.sprite import Sprite


class Resp(GameObject):
    """It's just a resp"""

    resp_sprite = None

    def __init__(self, x: int, y: int, sprite: Sprite = None):
        # Load sprite only once
        self.resp_sprite = pygame.image.load('img/skull.png').convert_alpha()
        super().__init__(x, y, 16, 16, self.resp_sprite, 'background')
        self.last_resp = 0

    def update(self, time_delta, objects=None):
        game_state = GameState.get_instance()
        self.last_resp += time_delta
        if self.last_resp >= 4000:
            self.last_resp = 0
            game_state.resp.append(Ghost(self.get_x(), self.get_y()))
