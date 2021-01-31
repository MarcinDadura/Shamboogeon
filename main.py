import pygame
import pygame_menu
from classes.game_state import GameState
from classes.room_manager import RoomManager
from classes.monster import Monster
from classes.game_object import GameObject
from classes.player import Player
from classes.teleport import Teleport
from classes.main_menu import  Menu
from classes.inventory import Inventory
from classes.item import Item
from classes.arrow import Arrow
from classes.saw import Saw
import sys


# Initialize pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

#pygame.mixer.music.load('elo.ogg')
#pygame.mixer.music.play(-1)
# pygame.mixer.music.load('elo.ogg')
# pygame.mixer.music.play(-1)

# Title
pygame.display.set_caption("Shamboo")

hearth = pygame.image.load('img/heart.png')
empty_heart = pygame.image.load('img/heart_empty.png')
hearths_board = pygame.Surface((48, 16))

welcome = pygame.image.load('img/history1.png')
lost = pygame.image.load('img/history2.png')
lost2 = pygame.image.load('img/history3.png')
lvl = 1

try:
    lvl = sys.argv[1]
except IndexError:
    lvl = 1

def main_menu() -> bool:
    """Should return False player when player hits exit button"""
    # TODO
    return True

room_manager = RoomManager.get_instance()

def game(screen):
    """Load levels"""
    global welcome, lost

    game_state = GameState.get_instance()
    inventory = Inventory.get_instance()
    inventory_board = pygame.Surface(screen.get_size())

    item = Item("arrow", "arrow", pygame.image.load('img/strzala_prawo.png'), 0, 0)
    item2 = Item("arrow", "arrow", pygame.image.load('img/strzala_prawo.png'), 0, 0)
    Inventory.get_instance().add_item(item)
    Inventory.get_instance().add_item(item2)

    game_state.reset()

    room_manager.set_lvl(lvl)

    """Sound"""

    game_menu.sound.stop()
    if (room_manager.get_lvl() == 1):
        print('test')
        game_sound = pygame.mixer.Sound('sounds/LOCHY-theme.ogg')
        game_sound.play(-1)
        game_sound.set_volume(0.15)


    board = pygame.Surface((640, 640))


    run = True
    counter = 0
    while run:
        counter += 1
        board, welcome_2 = calculate_scale(screen.get_size(), board, welcome, force=True)
        board.blit(welcome_2, (0, 0))
        screen.fill((0, 0, 0))
        screen.blit(board, ((screen.get_size()[0] - board.get_size()[0])/2, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and counter > 300:
                run = False


    player = Player.get_instance()
    player.set_x(128)
    player.set_y(128)

    show_s = True

    resett = True

    while(not game_state.exit):
        objects_list = room_manager.get_objects()
        old_room_obj = room(screen, board, objects_list, inventory, inventory_board)
        player = Player.get_instance()
        if player.get_y() < 0:
            room_manager.move_up()
        elif player.get_y() + player._height > 16 * 16:
            room_manager.move_down()
        elif player.get_x() < 0:
            room_manager.move_left()
        elif player.get_x() + player._width > 16 * 16:
            room_manager.move_right()
        if old_room_obj is not None:
            play_room_animation(old_room_obj, room_manager.get_objects(), board, inventory, inventory_board)
        GameObject.clear_objects_list()
        if game_state.next_lvl:
            game_state.next_lvl = False
            room_manager.set_lvl(room_manager.get_lvl() + 1)

        if (room_manager.get_lvl() == 2 and resett):
            resett = False
            game_sound.stop()
            game_sound = pygame.mixer.Sound('sounds/hepi-theme-final.ogg')
            game_sound.play(-1)
            game_sound.set_volume(0.95)

        run = True
        counter = 0
        while run and show_s and room_manager.get_lvl() == 2:
            counter += 1
            board, lost3 = calculate_scale(screen.get_size(), board, lost2, force=True)
            board.blit(lost3, (0, 0))
            screen.fill((0, 0, 0))
            screen.blit(board, ((screen.get_size()[0] - board.get_size()[0])/2, 0))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and counter > 300:
                    run = False
                    show_s = False

    run = True
    counter = 0
    while run:
        counter += 1
        board, lost_2 = calculate_scale(screen.get_size(), board, lost, force=True)
        board.blit(lost_2, (0, 0))
        screen.fill((0, 0, 0))
        screen.blit(board, ((screen.get_size()[0] - board.get_size()[0])/2, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT and counter > 300:
                run = False
            if event.type == pygame.KEYDOWN and counter > 300:
                run = False
    exit(0)

def play_room_animation(old_objects, new_objects, board, inventory: Inventory, inventory_board):
    global hearth, empty_heart, hearths_board
    speed = 150
    player = Player.get_instance()
    horizontal = True
    direction = -1
    if player.get_x() < 0:
        horizontal = True
        direction = 1
    elif player.get_y() < 0:
        horizontal = False
        direction = 1
    elif player.get_y() + player._height > 16 * 16:
        horizontal = False
        direction = -1

    if horizontal:
        for x in new_objects:
            if not x.cary:
                x.set_x(x.get_x() - 16 * 16 * direction)
    if not horizontal:
        for x in new_objects:
            if not x.cary:
                x.set_y(x.get_y() - 16 * 16 * direction)

    objects_list = new_objects
    new_objects = pygame.sprite.Group()
    inventory_g = pygame.sprite.Group()
    inventory_bar = pygame.sprite.Group()

    for o in objects_list:
        if not o.cary:
            new_objects.add(o)


    player_group = pygame.sprite.Group()
    player_group.add(player)
    inventory.rescale()
    inventory_bar.add(inventory)

    clock = pygame.time.Clock()
    game_state = GameState.get_instance()
    if RoomManager.get_instance().get_lvl() == 1:
        floor = pygame.image.load('img/no_floor.png')
    else:
        floor = pygame.image.load('img/no_floor.png')
    board, floor = calculate_scale(screen.get_size(), board, floor, force=True)
    move = 0

    while True:

        for o in inventory.get_items():
            o.rescale()
            inventory_g.add(o)

        inventory_board.fill((0, 0, 0))
        hearths_board.fill((0, 0, 0))
        for i in range(3):
            if i < player.hp:
                hearths_board.blit(hearth, (16*i * game_state.get_board_scale(), 0))
            else:
                hearths_board.blit(empty_heart, (16*i * game_state.get_board_scale(), 0))


        inventory_board.fill((0, 0, 0))
        inventory_bar.draw(inventory_board)
        inventory_g.draw(inventory_board)

        time_delta = clock.tick(120)
        move += speed * (time_delta/1000) * game_state.get_board_scale()
        screen.fill((0, 0, 0))

        board.fill((0, 255, 0))
        if floor:
            if horizontal:
                board.blit(floor, (move*2 * direction, 0))
                board.blit(floor, (move*2 * direction - (direction * 256 * GameState.get_instance().get_board_scale()), 0))
            else:
                board.blit(floor, (0, -move*2 * -direction))
                board.blit(floor, (0, -move*2 * -direction - (direction * 256 * GameState.get_instance().get_board_scale())))
        new_objects.draw(board)
        old_objects.draw(board)
        player_group.draw(board)
        screen.blit(inventory_board, (0, 0))
        screen.blit(hearths_board, (0, screen.get_size()[1]-16 * GameState.get_instance().get_board_scale()))
        screen.blit(board, ((screen.get_size()[0] - board.get_size()[0])/2, 0))
        pygame.display.flip()

        if horizontal:
            for x in old_objects:
                if not x.cary:
                    x.set_x(x.get_x() + speed * (time_delta/1000) * game_state.get_board_scale() * direction)
            for x in new_objects:
                if not x.cary:
                    x.set_x(x.get_x() + speed * (time_delta/1000) * game_state.get_board_scale() * direction)
            player.set_x(player.get_x() + speed * (time_delta/1000) * game_state.get_board_scale()/(17.3/16) * direction)
        else:
            for x in old_objects:
                if not x.cary:
                    x.set_y(x.get_y() + speed * (time_delta/1000) * game_state.get_board_scale() * direction)
            for x in new_objects:
                if not x.cary:
                    x.set_y(x.get_y() + speed * (time_delta/1000) * game_state.get_board_scale() * direction)
            player.set_y(player.get_y() + speed * (time_delta/1000) * game_state.get_board_scale()/(17.3/16) * direction)

        if move >= 16 * 16:
            if horizontal:
                player.set_x(player.get_x() - direction)
            else:
                player.set_y(player.get_y() - direction)
            return

def room(screen, board, objects_list: list, inventory: Inventory, inventory_board) -> pygame.sprite.Group:
    """
    Game loop
    Return objects to play animation 
    """
    global hearth, empty_heart, hearths_board
    objects = pygame.sprite.Group()
    monsters = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    teleports = pygame.sprite.Group()
    floor = None
    if RoomManager.get_instance().get_lvl() == 1:
        floor = pygame.image.load('img/no_floor.png')
    else:
        floor = pygame.image.load('img/no_floor.png')

    for o in objects_list:
        if not isinstance(o, Teleport) and not isinstance(o, Monster):
            objects.add(o)
        elif isinstance(o, Monster):
            monsters.add(o)
        elif not o.cary:
            teleports.add(o)
        elif o.cary:
            pass

    for obj in objects:
        if obj.type in ('ghost', 'rock', 'rainbow1', 'rainbow2', 'saw'):
            enemies.add(obj)

    for o in monsters:
        enemies.add(o)

    clock = pygame.time.Clock()
    game_state = GameState.get_instance()

    player = Player.get_instance()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    inventory_g = pygame.sprite.Group()
    inventory_bar = pygame.sprite.Group()
    inventory.rescale()
    inventory_bar.add(inventory)

    # Make sure if scale of the board is correct
    board, floor = calculate_scale(screen.get_size(), board, floor, force=True)

    all_objects = pygame.sprite.Group()
    for obj in objects:
        all_objects.add(obj)
    for obj in monsters:
        all_objects.add(obj)

    running = True
    while running:
    
        for i in game_state.resp:
            enemies.add(i)
            all_objects.add(i)
            game_state.resp.remove(i)

        hearths_board.fill((0, 0, 0))
        inventory_g = pygame.sprite.Group()
        for o in inventory.get_items():
            o.rescale()
            inventory_g.add(o)

        for i in range(3):
            if i < player.hp:
                hearths_board.blit(hearth, (16*i * game_state.get_board_scale(), 0))
            else:
                hearths_board.blit(empty_heart, (16*i * game_state.get_board_scale(), 0))

        time_delta = clock.tick(120)
        # RGB from 0 to 255
        screen.fill((0, 0, 0))
        inventory_board.fill((0, 0, 0))

        board.fill((0, 255, 0))
        if floor:
            board.blit(floor, (0, 0))

        objects.update(time_delta)
        teleports.update(time_delta)
        monsters.update(time_delta, objects)
        player.update(time_delta, all_objects, enemies)
        enemies.update(time_delta, all_objects)

        objects.draw(board)
        enemies.draw(board)
        teleports.draw(board)
        player_group.draw(board)
        monsters.draw(board)

        inventory_bar.draw(inventory_board)
        inventory_g.draw(inventory_board)

        screen.blit(inventory_board, (0, 0))
        screen.blit(hearths_board, (0, screen.get_size()[1]-16 * GameState.get_instance().get_board_scale()))
        screen.blit(board, ((screen.get_size()[0] - board.get_size()[0])/2, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_state.exit = True
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    game_state.exit = True
                    exit(0)

                arrow = None
                if event.key == pygame.K_UP:
                    arrow = Arrow.shoot_arrow(0, -1)
                elif event.key == pygame.K_DOWN:
                    arrow = Arrow.shoot_arrow(0, 1)
                elif event.key == pygame.K_LEFT:
                    arrow = Arrow.shoot_arrow(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    arrow = Arrow.shoot_arrow(1, 0)

                if arrow is not None:
                    enemies.add(arrow)
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                if width < 300:
                    width = 300
                    pygame.display.set_mode((width, height), pygame.RESIZABLE)
                if height < 300:
                    height = 300
                    pygame.display.set_mode((width, height), pygame.RESIZABLE)
                board, floor = calculate_scale(event.size, board, floor)
            elif event.type == pygame.KEYUP and event.key == pygame.K_e:
                if inventory.has_potion():
                    player.hp = player.hp + 1
                    inventory.dec_potion()

        if player.check_if_hit_border():
            for t in teleports:
                objects.add(t)
            Saw.stop_saws()
            return objects
        if pygame.sprite.spritecollideany(player, teleports):
            Saw.stop_saws()
            game_state.next_lvl = True
            running = False
        if player.hp == 0:
            Saw.stop_saws()
            running = False
            game_state.exit = True
        

def calculate_scale(size, board, floor=None, force=False):
    global hearth, empty_heart, hearths_board
    hearth = pygame.image.load('img/heart.png')
    empty_heart = pygame.image.load('img/heart_empty.png')
    hearths_board = pygame.Surface((48, 16))
    game_state = GameState.get_instance()
    h_tiles = size[0] // 16
    v_tiles = size[1] // 16

    h_tiles //= 16
    v_tiles //= 16

    if h_tiles < v_tiles:
        v_tiles = h_tiles

    hearths_board = pygame.transform.scale(hearths_board, (3 * 16 * v_tiles, 16 * v_tiles))
    empty_heart = pygame.transform.scale(empty_heart, (16 * v_tiles, 16 * v_tiles))
    hearth = pygame.transform.scale(hearth, (16 * v_tiles, 16 * v_tiles))
    if game_state.get_board_scale() != v_tiles or force:
        game_state.set_board_scale(v_tiles)
        GameObject.rescale()
        if floor:
            floor = pygame.transform.scale(floor, (v_tiles * 16 * 16, v_tiles * 16 * 16))
        board = pygame.transform.scale(board, (v_tiles * 16 * 16, v_tiles * 16 * 16))
    return board, floor


"""

Menu init

"""

game_menu = Menu(screen, 'sounds/menu-theme-final.ogg')
game_menu.add_button('Start', game)
game_menu.add_button("Quit", pygame_menu.events.EXIT)
check_size = screen.get_size()

while main_menu():
    game_menu.menu.mainloop(screen, disable_loop=main_menu())
    if(check_size != screen.get_size()):
        game_menu.response(screen.get_width(), screen.get_height())
        game_menu.add_button('Start', game)
        game_menu.add_button("Quit", pygame_menu.events.EXIT)
        check_size = screen.get_size()




