import time
import pygame
# definindo cores em RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()  # Inicializando módulos
screen = pygame.display.set_mode([640, 480])  # Criando superfície para janela (screen) do tamanho indicado
font = pygame.font.SysFont('None', 55)  # Carregando fonte
pygame.display.set_caption('Olá mundo')  # Nomeando a janela
screen.fill(BLACK)  # Preenchendo a janela com uma cor (preto)
# Desenhando na superfície. No pygame, para o plano de desenho, o y cresce pra baixo e o x pra direita
# draw.line(superfície, cor, [coordenadas início], [coordenadas fim], largura(pixels))
# draw.rect(superfície, cor, [x(início), y(início), largura, altura])
# draw.ellipse(superfície, cor, [x(início), y(início), largura, altura])
# draw.polygon(superfície, cor, [[cordenada1], [coordenada2], [coordenadaN]...])
pygame.draw.line(screen, WHITE, [10, 100], [630, 100], 5)
pygame.draw.rect(screen, BLUE, [200, 210, 40, 20])
pygame.draw.ellipse(screen, RED, [300, 200, 40, 40])
pygame.draw.polygon(screen, GREEN, [[420, 200], [440, 240], [400, 240]])
pygame.display.flip()  # Atualiza a janela com o conteúdo da superfície
time.sleep(5)  # Faz o programa esperar 5s pra fechar
screen.fill(BLACK)
# Definindo o texto com font.render(texto, antialias(T/F), cor)
# Antialias suaviza o contorno do texto
text = font.render('pygame', True, WHITE)
screen.blit(text, [250, 200])
pygame.display.flip()
time.sleep(5)
