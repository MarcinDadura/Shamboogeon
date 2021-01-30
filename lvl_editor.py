import pygame
import sys
from pygame.locals import *

# Bajzel straszny ale działa :)
# Mess scary but cannons :)

pygame.init()

width = 800
height = 600

try:
    lvl = sys.argv[1]
except IndexError:
    print('''
Usage:
    python3 lvl_editor.py LVL

Example:
    python3 lvl_editor.py 1
    ''')
    exit(0)

print('''
Shortcuts:
    p - save
    w/a/s/d - change room
    q/e - change current object
''')

background = (0, 0, 0)

# Pixel size of one block
tile_size = 32

# Create empty map
game_map = [['0' for _ in range(16)] for _ in range(16)]

# Try to load level from file
try:
    with open('levels/{}/10_10.txt'.format(lvl), 'r') as filee:
        game_map = []
        for row in filee:
            game_map.append(list(row[:-1])) 
except FileNotFoundError:
    pass

window = pygame.display.set_mode((800, 600))

# All available objects
objects = {
    '#': pygame.transform.scale(pygame.image.load('img/wall.png'), (tile_size, tile_size)),
    '$': pygame.transform.scale(pygame.image.load('img/teleport.png'), (tile_size, tile_size)),
    '{': pygame.transform.scale(pygame.image.load('img/door_left.png'), (tile_size, tile_size)),
    '}': pygame.transform.scale(pygame.image.load('img/door_right.png'), (tile_size, tile_size)),
    'r': pygame.transform.scale(pygame.image.load('img/kamien.png'), (tile_size, tile_size)),
    'k': pygame.transform.scale(pygame.image.load('img/key_1.png'), (tile_size, tile_size)),
    'l': pygame.transform.scale(pygame.image.load('img/key_2.png'), (tile_size, tile_size)),
    'g': pygame.transform.scale(pygame.image.load('img/ghost_0.png'), (tile_size, tile_size)),
    'b': pygame.transform.scale(pygame.image.load('img/button.png'), (tile_size, tile_size)),
    't': pygame.transform.scale(pygame.image.load('img/trellis.png'), (tile_size, tile_size)),
    'd': pygame.transform.scale(pygame.image.load('img/demon_0.png'), (tile_size, tile_size)),
}

palete = [sign for sign in objects]
arrow = pygame.transform.scale(pygame.image.load('img/arrow.png'), (tile_size, tile_size))

def get_grid_pos(click_pos):
    x = (click_pos[0]-20) // tile_size
    y = (click_pos[1]-20) // tile_size
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    return (x, y)

def save_to_file(pos_x, pos_y):
    with open('levels/{}/{}_{}.txt'.format(lvl, pos_x, pos_y), 'w') as filee:
        for row in game_map:
            filee.write(''.join(row) + '\n')

palete_i = 0
running = True


pos_x = 10
pos_y = 10

pygame.display.set_caption('LVL {} - {}:{}'.format(lvl, pos_x, pos_y))

def load_room(pos_x, pos_y):
    pygame.display.set_caption('LVL {} - {}:{}'.format(lvl, pos_x, pos_y))
    # Create empty map
    game_map = [['0' for _ in range(16)] for _ in range(16)]

    # Try to load level from file
    try:
        with open('levels/{}/{}_{}.txt'.format(lvl, pos_x, pos_y), 'r') as filee:
            game_map = []
            for row in filee:
                game_map.append(list(row[:-1])) 
    except FileNotFoundError:
        pass
    return game_map

while running:
    window.fill(background)
    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            if tile != '0':
                window.blit(objects[tile], (20 + x*tile_size, 20 + y*tile_size)) 
    # Display palete
    for i in range(len(palete)):
        window.blit(objects[palete[i]], (width-tile_size, i*tile_size)) 
    window.blit(arrow, (width-(tile_size*2), palete_i*tile_size)) 

    try:
        mouse_pos = pygame.mouse.get_pos()
        grid_pos = get_grid_pos(mouse_pos)
        window.blit(objects[palete[palete_i]], (20 + (grid_pos[0])*tile_size, 20 + (grid_pos[1])*tile_size)) 
    except IndexError:
        pass
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_q:
                palete_i += 1
                if palete_i >= len(palete):
                    palete_i = 0
            elif event.key == K_e:
                palete_i -= 1
                if palete_i < 0:
                    palete_i = len(palete) - 1 
            elif event.key == K_p:
                save_to_file(pos_x, pos_y)
            elif event.key == K_w:
                pos_y -= 1
                game_map = load_room(pos_x, pos_y)
            elif event.key == K_s:
                pos_y += 1
                game_map = load_room(pos_x, pos_y)
            elif event.key == K_a:
                pos_x -= 1
                game_map = load_room(pos_x, pos_y)
            elif event.key == K_d:
                pos_x += 1
                game_map = load_room(pos_x, pos_y)

    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        click_pos = pygame.mouse.get_pos()
        if click_pos[0] >= (width - tile_size):
            palete_i = click_pos[1] // tile_size
        else:
            grid_pos = get_grid_pos(click_pos)
            try:
                game_map[grid_pos[1]][grid_pos[0]] = palete[palete_i]
            except IndexError:
                pass
    if buttons[2]:
        click_pos = pygame.mouse.get_pos()
        if click_pos[0] >= (width - tile_size):
            palete_i = click_pos[1] // tile_size
        else:
            grid_pos = get_grid_pos(click_pos)
            try:
                game_map[grid_pos[1]][grid_pos[0]] = '0'
            except IndexError:
                pass
