from classes.game_object import GameObject
import pygame
from pygame.locals import *
from classes.item import Item
from classes.inventory import Inventory


class Player(GameObject):
    player_sprite = None

    _instance = None

    def __init__(self, x: int, y: int):
        Player._instance = self
        self.last_damage = 0
        self.speed = 100
        self.hp = 3
        self.sound = pygame.mixer.Sound('sounds/player_take_damage.ogg')
        self.sound.set_volume(1)
        # Load sprite only once
        if Player.player_sprite is None:

            Player.player_sprite_left = [pygame.image.load('img/hero-frame-0_1.png').convert_alpha(),
                                         pygame.image.load('img/hero-frame-0_2.png').convert_alpha(),
                                         pygame.image.load('img/hero-frame-0_3.png').convert_alpha()]
            Player.player_sprite_right = [pygame.image.load('img/hero-frame-0_4.png').convert_alpha(),
                                          pygame.image.load('img/hero-frame-0_5.png').convert_alpha(),
                                          pygame.image.load('img/hero-frame-0_6.png').convert_alpha()]
        super().__init__(x, y, 11, 14, Player.player_sprite_left[0], 'player')
        self.index = 0
        self.direction = 0

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            # Create instance
            cls(50, 50)
        return cls._instance

    def take_damage(self) -> bool:
        if self.last_damage > 300:
            self.last_damage = 0
            self.hp -= 1
            self.sound.play()
            return True
        return False

    def update(self, time_delta, objects, enemies=None):
        self.last_damage += 1
        if self.direction == 0:
            self.set_sprite(Player.player_sprite_right[0])
        else:
            self.set_sprite(Player.player_sprite_left[0])
        keys = pygame.key.get_pressed()
        old_x = self.get_x()
        old_y = self.get_y()
        horizontal_direction = 0
        if keys[K_d]:
            self.direction = 0
            horizontal_direction += 1
            self.set_sprite(Player.player_sprite_right[self.index // 10])
            self.index += 1
            if self.index > 20:
                self.index = 0
        if keys[K_a]:
            self.direction = 1
            horizontal_direction -= 1
            self.set_sprite(Player.player_sprite_left[self.index//10])
            self.index += 1
            if self.index > 20:
                self.index = 0

        self.set_x(self._x + self.speed * (time_delta/1000) * horizontal_direction)

        for obj in  pygame.sprite.spritecollide(self, objects, dokill=False):
            inventory = Inventory.get_instance()
            if obj.type == 'rock':
                if not obj.push(self.speed * (time_delta/1000) * horizontal_direction, 0, objects):
                    self.set_x(old_x)
                    break
            elif obj.type == 'rainbow1':
                if not obj.push(self.speed * (time_delta/1000) * horizontal_direction, 0, objects):
                    self.set_x(old_x)
                    break
            elif obj.type == 'rainbow2':
                if not obj.push(self.speed * (time_delta/1000) * horizontal_direction, 0, objects):
                    self.set_x(old_x)
                    break
            elif obj.type == 'key':
                item = Item("key_{}".format(obj.part), "key_{}".format(obj.part), pygame.image.load('img/key_{}.png'.format(obj.part)),0, 0)
                inventory.add_item(item)
                if inventory.check_engine():
                    pass
                obj.cary = True
                if obj.part in (1, 2):
                    inventory.unitKey()
                obj.kill()
            elif obj.type == 'door' and inventory.checkKey():
                obj.sound = obj.sound.play()
                obj.kill()
            elif obj.type == 'item':
                inventory.add_item(obj)
                obj.kill()
            elif obj.type in ('ghost', 'monster', 'saw'):
                self.take_damage()
            elif not obj.type == "background" and obj.type != 'button':
                self.set_x(old_x)
                break

        vertical_direction = 0

        if keys[K_s]:
            vertical_direction -= 1
            if self.direction == 0:
                self.set_sprite(Player.player_sprite_right[self.index // 10])
                self.index += 1
                if self.index > 20:
                    self.index = 0
            if self.direction == 1:
                self.set_sprite(Player.player_sprite_left[self.index // 10])
                self.index += 1
                if self.index > 20:
                    self.index = 0
        if keys[K_w]:
            vertical_direction += 1
            old_y = self.get_y()
            if self.direction == 0:
                self.set_sprite(Player.player_sprite_right[self.index // 10])
                self.index += 1
                if self.index > 20:
                    self.index = 0
            if self.direction == 1:
                self.set_sprite(Player.player_sprite_left[self.index // 10])
                self.index += 1
                if self.index > 20:
                    self.index = 0
        self.set_y(self._y - self.speed * (time_delta/1000) * vertical_direction)

        inventory = Inventory.get_instance()
        for obj in  pygame.sprite.spritecollide(self, objects, dokill=False):
            if obj.type == 'rock':
                if not obj.push(0, self.speed * (time_delta/1000) * -vertical_direction, objects):
                    self.set_y(old_y)
                    break
            elif obj.type == 'rainbow1':
                if not obj.push(0, self.speed * (time_delta/1000) * -vertical_direction, objects):
                    self.set_y(old_y)
                    break
            elif obj.type == 'rainbow2':
                if not obj.push(0, self.speed * (time_delta/1000) * -vertical_direction, objects):
                    self.set_y(old_y)
            elif obj.type == 'key':
                item = Item("key_{}".format(obj.part), "key_{}".format(obj.part), pygame.image.load('img/key_{}.png'.format(obj.part)), 0, 0)
                inventory.add_item(item)
                if inventory.check_engine():
                    pass

                obj.cary = True
                inventory.unitKey()
                obj.kill()
            elif obj.type == 'item':
                inventory.add_item(obj)
                obj.kill()

            elif obj.type == 'door' and inventory.checkKey():
                obj.sound = obj.sound.play()
                obj.kill()

            elif obj.type in ('ghost', 'monster', 'saw'):
                self.take_damage()
            elif not obj.type == "background" and obj.type != 'button':
                self.set_y(old_y)
                break

        if enemies is not None:
            for obj in  pygame.sprite.spritecollide(self, enemies, dokill=False):
                if obj.type == 'arrow':
                    if obj.horizontal_direction != 0 or obj.vertical_direction != 0:
                        self.take_damage()
                    item = Item("arrow", "arrow", pygame.image.load('img/strzala_prawo.png'), 0, 0)
                    inventory.add_item(item)
                    obj.cary = True
                    obj.kill()

    def check_if_hit_border(self) -> bool:
        if self._x < 0 or self._y < 0 or (self._x + self._width) > (16*16) or (self._y + self._height) > (16*16):
            return True
        return False
