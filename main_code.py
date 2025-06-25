# Import libraries
import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup

WITDH, HEIGHT = 600 , 400
screen = pygame.display.set_mode((WITDH, HEIGHT))
pygame.display.set_caption("Dodge the red falling block.")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player setup
player_size = 50
player_pos = [WITDH // 2, HEIGHT - player_size]
player_speed = 5

# Enemy setup
enemy_size = 50
enemy_pos = [[random.randint(0 - WITDH - enemy_size), 0]]
enemy_speed = 5

# Game loop (shows the window)
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()