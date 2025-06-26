# run.py

# Import from the Player and Enemy class file and import pygame 
from player_and_enemy import Player, Enemy
import pygame

# Initialize pygame
pygame.init()

# Screen and color setup
WIDTH, HEIGHT = 600, 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the red falling block.")

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 35)

# Collision detection
# Create entities
# Game loop