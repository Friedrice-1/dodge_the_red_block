# Entities such as player and the enemy

# Import the libraries
import pygame
import random
# Import the constants
WIDTH, HEIGHT = 600 , 400
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create a player class
class Player:
    def __init__(self, size = 50, speed = 5):
        self.size = size
        self.speed = speed
        self.pos = [WIDTH // 2, HEIGHT - size]
# Create the enemy class