import pygame
from classes.game_state import GameState
from classes.room_manager import RoomManager
from classes.game_object import GameObject
from classes.player import Player
from classes.teleport import Teleport


# Initialize pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
#pygame.mixer.music.load('elo.ogg')
#pygame.mixer.music.play(-1)

# Title
pygame.display.set_caption("Shamboo")

def main_menu() -> bool:
    """Should return False player when player hits exit button"""
    # TODO
    return True

def game(screen):
    """Load levels"""
    game_state = GameState.get_instance()
    game_state.reset()

    room_manager = RoomManager.get_instance()
    room_manager.set_lvl(1)
    board = pygame.Surface((640, 640))
    player = Player.get_instance()
    player.set_x(128)
    player.set_y(128)

    while(not game_state.exit):
        objects_list = room_manager.get_objects()
        old_room_obj = room(screen, board, objects_list)
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
            play_room_animation(old_room_obj, room_manager.get_objects(), board)
        GameObject.clear_objects_list()
        if game_state.next_lvl:
            game_state.next_lvl = False
            room_manager.set_lvl(room_manager.get_lvl() + 1)

def play_room_animation(old_objects, new_objects, board):
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
            x.set_x(x.get_x() - 16 * 16 * direction)
    if not horizontal:
        for x in new_objects:
            x.set_y(x.get_y() - 16 * 16 * direction)


    objects_list = new_objects
    new_objects = pygame.sprite.Group()
    for o in objects_list:
        new_objects.add(o)

    player_group = pygame.sprite.Group()
    player_group.add(player)

    clock = pygame.time.Clock()
    game_state = GameState.get_instance()
    board = calculate_scale(screen.get_size(), board, True)
    move = 0
    while(True):
        time_delta = clock.tick(120)
        move += speed * (time_delta/1000) * game_state.get_board_scale()
        screen.fill((0, 0, 0))
        board.fill((0, 0, 0))
        new_objects.draw(board)
        old_objects.draw(board)
        player_group.draw(board)
        screen.blit(board, ((screen.get_size()[0] - board.get_size()[0])/2, 0))
        pygame.display.flip()
        if horizontal:
            for x in old_objects:
                x.set_x(x.get_x() + speed * (time_delta/1000) * game_state.get_board_scale() * direction)
            for x in new_objects:
                x.set_x(x.get_x() + speed * (time_delta/1000) * game_state.get_board_scale() * direction)
            player.set_x(player.get_x() + speed * (time_delta/1000) * game_state.get_board_scale()/(17.1/16) * direction)
        else:
            for x in old_objects:
                x.set_y(x.get_y() + speed * (time_delta/1000) * game_state.get_board_scale() * direction)
            for x in new_objects:
                x.set_y(x.get_y() + speed * (time_delta/1000) * game_state.get_board_scale() * direction)
            player.set_y(player.get_y() + speed * (time_delta/1000) * game_state.get_board_scale()/(17.1/16) * direction)

        if move >= 16 * 16:
            if horizontal:
                player.set_x(player.get_x() - direction)
            else:
                player.set_y(player.get_y() - direction)
            return


def room(screen, board, objects_list: list) -> pygame.sprite.Group:
    """
    Game loop
    Return objects to play animation 
    """
    objects = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    teleports = pygame.sprite.Group()
    for o in objects_list:
        if not isinstance(o, Teleport):
            objects.add(o)
        else:
            teleports.add(o)
    for obj in objects:
        if obj.type in ('ghost', 'rock'):
            enemies.add(obj)
    clock = pygame.time.Clock()
    game_state = GameState.get_instance()

    player = Player.get_instance()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # Make sure if scale of the board is correct
    board = calculate_scale(screen.get_size(), board, True)

    running = True
    while running:
        time_delta = clock.tick(120)
        # RGB from 0 to 255
        screen.fill((0, 0, 0))
        board.fill((0, 0, 0))
        objects.update(time_delta)
        teleports.update(time_delta)
        player.update(time_delta, objects)
        enemies.update(time_delta, objects)
        objects.draw(board)
        teleports.draw(board)
        player_group.draw(board)
        screen.blit(board, ((screen.get_size()[0] - board.get_size()[0])/2, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_state.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    game_state.exit = True
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                if width < 300:
                    width = 300
                    pygame.display.set_mode((width, height), pygame.RESIZABLE)
                if height < 300:
                    height = 300
                    pygame.display.set_mode((width, height), pygame.RESIZABLE)
                board = calculate_scale(event.size, board)
        if player.check_if_hit_border():
            for t in teleports:
                objects.add(t)
            return objects
        if pygame.sprite.spritecollideany(player, teleports):
            game_state.next_lvl = True
            running = False
        

def calculate_scale(size, board, force=False):
    game_state = GameState.get_instance()
    h_tiles = size[0] // 16
    v_tiles = size[1] // 16

    h_tiles //= 16
    v_tiles //= 16

    if h_tiles < v_tiles:
        v_tiles = h_tiles

    if game_state.get_board_scale() != v_tiles or force:
        game_state.set_board_scale(v_tiles)
        GameObject.rescale()
        board = pygame.transform.scale(board, (v_tiles * 16 * 16, v_tiles * 16 * 16))
    return board

while main_menu():
    game(screen)
    break
