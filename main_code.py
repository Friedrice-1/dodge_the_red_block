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

# Clock and Font
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 35)

# Collision function
def detect_collision(player_pos, enemy_pos):
    player_x , player_y = player_pos
    enemy_x , enemy_y = enemy_pos
    
    return(enemy_x < player_x + enemy_size or enemy_x < player_x + player_size < enemy_x + enemy_size) and \
            (enemy_y < player_y + enemy_size or enemy_y < player_y + player_size < enemy_y + enemy_size)

# Game loop (shows the window)
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()