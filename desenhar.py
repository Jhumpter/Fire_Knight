import pygame
from random import randint
pygame.init()
screen = pygame.display.set_mode((610, 360))
game = True
cor = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
posx = 305
posy = 180
screen.fill((0, 0, 0))
font = pygame.font.SysFont('Times New Roman', 15)
text = font.render('Aperte "C" para limpar e espaço para sortear outra cor', True, (255, 255, 255))
screen.blit(text, [0, 0])
clock = pygame.time.Clock()
while game:
    dt = clock.tick(80)
    # Habilitando o botão de fechar
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    # Desenhando quadrado
    quadrado = pygame.draw.rect(screen, cor, [posx, posy, 20, 20])
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if posy != 0:
            posy -= 1
    if keys[pygame.K_s]:
        if posy != 320:
            posy += 1
    if keys[pygame.K_a]:
        if posx != 0:
            posx -= 1
    if keys[pygame.K_d]:
        if posx != 580:
            posx += 1
    if keys[pygame.K_SPACE]:
        cor = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
    if keys[pygame.K_c]:
        screen.fill((0, 0, 0))
        screen.blit(text, [0, 0])
    pygame.display.flip()
