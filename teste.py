import time
import pygame
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Velocity')
position_x = 0
# 100 pixels por segundo
velocity_x = 100
# captura o tempo inicial
ti = time.time()
while True:
    # captura o tempo deste ciclo
    tf = time.time()
    # calcula o delta
    dt = (tf - ti)
    # atribui o tempo final como tempo inicial
    ti = tf
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    # move o quadrado na velocidade média definida
    position_x += velocity_x * dt
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [position_x, 230, 20, 20])
    pygame.display.flip()
