import pygame

# Initialize pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("Shamboo")

# Game loop
running = True
while running:
    # RGB from 0 to 255
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
