import pygame
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill(BLACK)
pygame.display.set_caption('Inputs')
font = pygame.font.SysFont('None', 55)
game = True
while game:
    # pygame.event.pool() retorna apenas um evento por vez, enquanto pygame.event.get() retorna uma lista de eventos
    for event in pygame.event.get():
        # Verificando se o botão de sair é pressionado para fechar o programa
        if event.type == pygame.QUIT:
            game = False
        # Verificando se o evento é de tecla pressionada
        if event.type == pygame.KEYDOWN:
            # Verificando se a tecla pressionada é a tecla 'w'
            if event.key == pygame.K_w:
                screen.fill(BLACK)
                text = font.render('Apertou W', True, WHITE)
                screen.blit(text, [250, 200])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                screen.fill(BLACK)
                text = font.render('Soltou W', True, WHITE)
                screen.blit(text, [250, 200])
    pygame.display.flip()
    # pygame.display.flip() é utilizado para alterar a maior parte da tela,
    # ja pygame.display.update() é utilizado para partes específicas.
    # Outro jeito de avaliar se uma tecla está pressionada é com pygame.key.get_pressed()
    keys = pygame.key.get_pressed()
    # Cria um dicionário que retorna o índice da tecla pressionada (pygame.K_tecla) como booleano
    if keys[pygame.K_k]:
        screen.fill(BLACK)
        text = font.render('Apertou K', True, WHITE)
        screen.blit(text, [250, 100])
    pygame.display.flip()