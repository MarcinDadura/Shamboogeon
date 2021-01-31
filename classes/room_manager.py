from classes.wall import Wall
from classes.teleport import Teleport
from classes.door import Door
from classes.rock import Rock
from classes.key import Key
from classes.ghost import Ghost
from classes.button import Button
from classes.trellis import Trellis
from classes.monster import Monster
from classes.inventory import Inventory
from classes.background import Background
import pygame

class RoomManager:
    _instance = None

    def __init__(self):
        self.lvl = 0
        self._x = 10
        self._y = 10
        self.rooms = None
        RoomManager._instance = self

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # Create instance
            cls()
        return cls._instance

    def set_lvl(self, lvl: int):
        self.lvl = lvl
        self._x = 10
        self._y = 12
        # Clear rooms
        self.rooms = [[None for _ in range(21)] for _ in range(21)]

    def get_lvl(self):
        return self.lvl

    def load_room(self, x: int, y: int):
        self.rooms[y][x] = []
        with open('levels/{}/{}_{}.txt'.format(self.lvl, x, y), 'r') as filee:
            for row in filee:
                self.rooms[y][x].append(list(row[:-1])) 

    def get_curr_position(self) -> tuple:
        return (self._x, self._y)

    def move_left(self):
        self._x -= 1

    def move_down(self):
        self._y += 1

    def move_right(self):
        self._x += 1

    def move_up(self):
        self._y -= 1

    def get_objects(self) -> list:
        """Return all objects in current room"""
        if self.rooms[self._y][self._x] is None:
            self.load_room(self._x, self._y)
        # TODO: refactor :)
        objects = []
        for y, row in enumerate(self.rooms[self._y][self._x]):
            for x, tile in enumerate(row):
                if tile == '#':
                    objects.append(
                        Wall(x*16, y*16)
                    ) 
                elif tile == '$':
                    objects.append(
                        Teleport(x*16, y*16)
                    ) 
                elif tile == '{':
                    objects.append(
                        Door(x*16, y*16)
                    ) 
                elif tile == '}':
                    objects.append(
                        Door(x*16, y*16, 'right')
                    )
                elif tile == ']':
                    objects.append(
                        Door(x*16, y*16, 'up')
                    )
                elif tile == '[':
                    objects.append(
                        Door(x*16, y*16, 'down')
                    )
                elif tile == 'r':
                    objects.append(
                        Rock(x*16 + 1, y*16 + 1)
                    ) 
                elif tile == 'k':
                    inventory = Inventory.get_instance()
                    if not inventory.checkKey():
                        objects.append(
                            Key(x*16, y*16, 1)
                        )
                elif tile == 'l':
                    objects.append(
                        Key(x*16, y*16, 2)
                    ) 
                elif tile == 'g':
                    objects.append(
                        Ghost(x*16, y*16)
                    ) 
                elif tile == 'b':
                    objects.append(
                        Button(x*16, y*16)
                    ) 
                elif tile == 't':
                    objects.append(
                        Trellis(x*16, y*16)
                    )

                elif tile == 'e':
                    objects.append(
                        Wall(x*16, y*16, pygame.image.load('img/dungeon_wall_broken.png').convert_alpha())
                    )
                elif tile == 'j':
                    objects.append(
                        Wall(x*16, y*16, pygame.image.load('img/dungeon_spiders_web.png').convert_alpha())
                    )
                elif tile == 'a':
                    objects.append(
                        Wall(x*16, y*16, pygame.image.load('img/dungeon_bones.png').convert_alpha())
                    )
                elif tile == 'c':
                    objects.append(
                        Wall(x*16, y*16, pygame.image.load('img/dungeon_skull.png').convert_alpha())
                    )
                elif tile == 'h':
                    objects.append(
                        Background(x*16, y*16, pygame.image.load('img/candy_rainbow_wall.png').convert_alpha())
                    )
                elif tile == 'm':
                    objects.append(
                        Wall(x*16, y*16, pygame.image.load('img/candy_wall.png').convert_alpha())
                    )
                elif tile == 'd':
                    objects.append(
                        Monster(x * 16, y * 16, 5, 'sounds/demon.ogg', 'img/demon_0.png', 'demon', 5)
                    )

                elif tile == 'n':
                    objects.append(
                        Monster(x * 16, y * 16, 5, 'sounds/demon.ogg', 'img/candy_mob_0.png', 'candy_mob', 0)
                    )

                elif tile == 'o':
                    objects.append(
                        Monster(x * 16, y * 16, 5, 'sounds/demon.ogg', 'img/rainbow_mob_0.png', 'rainbow_mob', 2)
                    )
                elif tile == 'z':
                    objects.append(
                        Background(x * 16, y * 16, pygame.image.load('img/dungeon_background2.png').convert_alpha())
                    )
                elif tile == 'f':
                    objects.append(
                        Background(x * 16, y * 16)
                    )
        return objects
