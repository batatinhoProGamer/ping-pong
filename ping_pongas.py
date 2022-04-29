import pygame
from pygame.locals import *
from sys import exit

pygame.init()

info = pygame.display.Info()
largura = info.current_w
altura = info.current_h
janela = pygame.display.set_mode((largura, altura))

altura_parede_esquerda = 0
altura_parede_direita = 0

x_bola = 45
y_bola = 75
velocidade_bola_y = 7
velocidade_bola_x = 7

relogio = pygame.time.Clock()

inicio = False
while True:
    relogio.tick(60)
    janela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    parede_esquerda = pygame.draw.rect(janela, (255, 255, 255), (20, altura_parede_esquerda, 10, 150))
    parede_direita = pygame.draw.rect(janela, (255, 255, 255), (largura - 30, altura_parede_direita, 10, 150))

    bola = pygame.draw.circle(janela, (123, 123, 123), (x_bola, y_bola), 15)

    if pygame.key.get_pressed()[K_w] and altura_parede_esquerda > 0:
        altura_parede_esquerda -= 10
    if pygame.key.get_pressed()[K_s] and altura_parede_esquerda < altura - 150:
        if not inicio:
            inicio = True
        altura_parede_esquerda += 10

    if pygame.key.get_pressed()[K_UP] and altura_parede_direita > 0:
        altura_parede_direita -= 10
    if pygame.key.get_pressed()[K_DOWN] and altura_parede_direita < altura - 150:
        if not inicio:
            inicio = True
        altura_parede_direita += 10

    if inicio:
        if x_bola < 0 or x_bola > largura:
            x_bola = 45
            y_bola = 75
            inicio = False
            altura_parede_esquerda = 0
            altura_parede_direita = 0
        
        if bola.colliderect(parede_esquerda) and velocidade_bola_x > 0 or bola.colliderect(parede_direita) and velocidade_bola_x < 0:
            x_bola = 45
            y_bola = 75
            inicio = False
            altura_parede_esquerda = 0
            altura_parede_direita = 0

        if y_bola <= 15 or y_bola >= 690:
            velocidade_bola_y *= -1

        if bola.colliderect(parede_esquerda) or bola.colliderect(parede_direita):
            velocidade_bola_x *= -1
        
        if inicio:
            y_bola += velocidade_bola_y
            x_bola += velocidade_bola_x

    """if bola.collidedictall(parede_esquerda):
        x_bola """

    pygame.display.update()
