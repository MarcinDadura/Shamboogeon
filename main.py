import pygame
from classes.game_state import GameState
from classes.room_manager import RoomManager
from classes.game_object import GameObject
from classes.player import Player

# Initialize pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

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

    objects_list = room_manager.get_objects()
    room(screen, objects_list)


def room(screen, objects_list: list):
    """Game loop"""
    objects = pygame.sprite.Group()
    for o in objects_list:
        objects.add(o)
    board = pygame.Surface((640, 640))
    clock = pygame.time.Clock()

    player = Player.get_instance()
    player.set_x(32)
    player.set_y(32)
    player_group = pygame.sprite.Group()
    player_group.add(player)

    # Make sure if scale of the board is correct
    board = calculate_scale(screen.get_size(), board)

    running = True
    while running:
        time_delta = clock.tick(120)
        # RGB from 0 to 255
        screen.fill((0, 0, 34))
        board.fill((0, 0, 0))
        objects.update(time_delta)
        objects.draw(board)
        player_group.draw(board)
        screen.blit(board, ((screen.get_size()[0] - board.get_size()[0])/2, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                if width < 300:
                    width = 300
                    pygame.display.set_mode((width, height), pygame.RESIZABLE)
                if height < 300:
                    height = 300
                    pygame.display.set_mode((width, height), pygame.RESIZABLE)
                board = calculate_scale(event.size, board)

def calculate_scale(size, board):
    game_state = GameState.get_instance()
    h_tiles = size[0] // 16
    v_tiles = size[1] // 16

    h_tiles //= 16
    v_tiles //= 16

    if h_tiles < v_tiles:
        v_tiles = h_tiles

    if game_state.get_board_scale() != v_tiles:
        game_state.set_board_scale(v_tiles)
        GameObject.rescale()
        board = pygame.transform.scale(board, (v_tiles * 16 * 16, v_tiles * 16 * 16))
    return board

while main_menu():
    game(screen)
    break
