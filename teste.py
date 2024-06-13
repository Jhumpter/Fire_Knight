import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
cores = [BLACK, BLUE, GREEN, RED]
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Game Loop')
position_x = 500
position_y = 300
velocity_y = 1
color1 = random.choice(cores)
color2 = random.choice(cores)
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    position_y += velocity_y
    if position_y > 440:
        velocity_y = -1
        color1 = random.choice(cores)
        color2 = random.choice(cores)
    elif position_y <= 0:
        velocity_y = 1
        color1 = random.choice(cores)
        color2 = random.choice(cores)
    screen.fill(WHITE)
    pygame.draw.ellipse(screen, color1, [position_x, position_y, 40, 40])
    pygame.draw.ellipse(screen, color2, [position_x-200, position_y, 40, 40])
    pygame.display.flip()
