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

    def move(self, keys):
        if keys[pygame.K_a] and self.pos[0] > 0:
            self.pos[0] -= self.speed
        if keys[pygame.K_d] and self.pos[0] < WIDTH - self.size:
            self.pos[0] += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (*self.pos, self.size, self.size))

# Create the enemy class
class Enemy:
    def __init__(self, size=50, speed=5):
        self.size = size
        self.speed = speed
        self.pos = [random.randint(0, WIDTH - size), 0]
    
    def move(self):
        self.pos[1] += self.speed
        if self.pos[1] > HEIGHT:
            self.pos[1] = 0
            self.pos[0] = random.randint(0, WIDTH - self.size)
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.pos, self.size, self.size))