from classes.wall import Wall
from classes.teleport import Teleport
from classes.door import Door
from classes.rock import Rock
from classes.key import Key


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
        self._y = 10
        # Clear rooms
        self.rooms = [ [None for _ in range(21)] for _ in range(21) ]

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
                elif tile == 'r':
                    objects.append(
                        Rock(x*16, y*16)
                    ) 
                elif tile == 'k':
                    objects.append(
                        Key(x*16, y*16, 1)
                    ) 
                elif tile == 'l':
                    objects.append(
                        Key(x*16, y*16, 2)
                    ) 
        return objects
