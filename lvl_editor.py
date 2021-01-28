import pygame
import sys
from pygame.locals import *

# Bajzel straszny ale działa :)
# Mess scary but cannons :)

pygame.init()

width = 800
height = 600

try:
    file_name = sys.argv[1]
except IndexError:
    print('''
Usage:
    python3 lvl_editor.py FILE_NAME

Example:
    python3 lvl_editor.py room1.txt
    ''')
    exit(0)

print('Shortcuts:\n\ts - save')

background = (0, 0, 0)

# Pixel size of one block
tile_size = 32

# Create empty map
game_map = [['0' for _ in range(10)] for _ in range(10)]

# Try to load level from file
try:
    with open(file_name, 'r') as filee:
        game_map = []
        for row in filee:
            game_map.append(list(row[:-1])) 
except FileNotFoundError:
    pass

window = pygame.display.set_mode((800, 600))

# All available objects
objects = {
    '#': pygame.transform.scale(pygame.image.load('img/wall.png'), (tile_size, tile_size)),
    '$': pygame.transform.scale(pygame.image.load('img/skull.png'), (tile_size, tile_size)),
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

def save_to_file():
    with open(file_name, 'w') as filee:
        for row in game_map:
            filee.write(''.join(row) + '\n')

palete_i = 0
running = True

pygame.display.set_caption(file_name)

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
            if event.key == K_UP:
                palete_i += 1
                if palete_i >= len(palete):
                    palete_i = 0
            elif event.key == K_DOWN:
                palete_i -= 1
                if palete_i < 0:
                    palete_i = len(palete) - 1 
            elif event.key == K_s:
                save_to_file()

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
