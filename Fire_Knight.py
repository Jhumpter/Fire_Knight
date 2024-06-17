import os, sys
import pygame
import random
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
####

pygame.init()
drawGroup = pygame.sprite.Group()
hero = pygame.sprite.Sprite(drawGroup)  # Criando um sprite
backgound = pygame.image.load('imgs/background.png')
img = 'imgs/knight_R.png'
enemies = ['imgs/fire1.png', 'imgs/fire2.png', 'imgs/fire3.png', 'imgs/rat.png', 'imgs/mike.png']
enemy1 = pygame.sprite.Sprite(drawGroup)
enemy2 = pygame.sprite.Sprite(drawGroup)
enemy3 = pygame.sprite.Sprite(drawGroup)
enemy2.image = enemy3.image = pygame.image.load('imgs/empty.png')
enemy2.rect = enemy3.rect = pygame.Rect(0, 0, 60, 60)
posx = 450
posy = 320
screen = pygame.display.set_mode((1000, 500))
game = True
font = pygame.font.SysFont('Times New Roman', 85)
font_score = pygame.font.SysFont('Times New Roman', 35)
clock = pygame.time.Clock()
screen.blit(backgound, (0, 0))
stop = True
x = 1010
y = [random.randint(190, 410), random.randint(190, 410), random.randint(190, 410)]
obstacle = [random.choice(enemies), random.choice(enemies), random.choice(enemies)]
vel = 7
level = 1
score = 0
gameover = False
reset = False
while game:
    if reset:
        vel = 7
        level = 1
        score = 0
        gameover = False
        reset = False
        x = 1010
        posx = 450
        posy = 320
        y = [random.randint(190, 410), random.randint(190, 410), random.randint(190, 410)]
        obstacle = [random.choice(enemies), random.choice(enemies), random.choice(enemies)]
        stop = False
        screen.blit(backgound, (0, 0))
        enemy2.rect = pygame.Rect(x, y[1], 32, 32)
        enemy3.rect = pygame.Rect(x, y[2], 32, 32)
    dt = clock.tick(30)
    hero.image = pygame.image.load(img)  # Carregando a imagem no cavaleiro
    hero.image = pygame.transform.scale(hero.image, [80, 80])
    hero.rect = pygame.Rect(posx, posy, 32, 32)
    if x < -80:
        x = 1010
        y = [random.randint(190, 410), random.randint(190, 410), random.randint(190, 410)]
        obstacle = [random.choice(enemies), random.choice(enemies), random.choice(enemies)]
        score += 1
        if vel < 15:
            vel += 1
        level += 1
    enemy1.image = pygame.image.load(obstacle[0])  # Carregando os obstáculos
    enemy1.image = pygame.transform.scale(enemy1.image, [60, 60])
    enemy1.rect = pygame.Rect(x, y[0], 32, 32)
    if level > 1:
        enemy2.image = pygame.image.load(obstacle[1])  # Carregando os obstáculos
        enemy2.image = pygame.transform.scale(enemy2.image, [60, 60])
        enemy2.rect = pygame.Rect(x, y[1], 32, 32)
    if level > 2:
        enemy3.image = pygame.image.load(obstacle[2])  # Carregando os obstáculos
        enemy3.image = pygame.transform.scale(enemy3.image, [60, 60])
        enemy3.rect = pygame.Rect(x, y[2], 32, 32)
    if not stop:
        x -= vel
    # Habilitando o botão de fechar
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:
        if not gameover:
            if event.key == pygame.K_p:
                stop = not stop
        if event.key == pygame.K_r:
            reset = True
    keys = pygame.key.get_pressed()
    # Criando um menu para começar
    screen.blit(backgound, (0, 0))
    drawGroup.draw(screen)
    if stop:
        # Cria uma superfície transparente
        superficie_transparente = pygame.Surface((1000, 500), pygame.SRCALPHA)
        pygame.draw.rect(superficie_transparente, (0, 0, 0, 128), (0, 0, 1000, 500))
        screen.blit(superficie_transparente, (0, 0))
        if not gameover:
            # Texto de pause
            text = font.render('Pause', True, (255, 255, 255))
            screen.blit(text, [350, 225])
    # Movimento do cavaleiro
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if posx < 930 and not stop:
            posx += 7
            img = 'imgs/knight_R.png'
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if posx > 0 and not stop:
            posx -= 7
            img = 'imgs/knight_L.png'
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if posy > 190 and not stop:
            posy -= 7
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if posy < 410 and not stop:
            posy += 7
    text = font_score.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, [0, 0])
    if (pygame.sprite.collide_rect(hero, enemy1) or pygame.sprite.collide_rect(hero, enemy2)
            or pygame.sprite.collide_rect(hero, enemy3)):
        gameover = True
        stop = True
        text = font.render('Game Over', True, (255, 255, 255))
        screen.blit(text, [350, 225])
    pygame.display.flip()
