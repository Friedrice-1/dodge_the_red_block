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
def detect_collision(p_pos, e_pos, size):
    px, py = p_pos
    ex, ey = e_pos
    return (ex < px < ex + size or ex < px + size < ex + size) and \
           (ey < py < ey + size or ey < py + size < ey + size)

# Create entities
player = Player()
enemy = Enemy()

# Game loop
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    enemy.move()
    
    if detect_collision(player.pos, enemy.pos, player.size):
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        running = False
    
    player.draw(screen)
    enemy.draw(screen)

    pygame.display.update()
    clock.tick(30)

pygame.quit()