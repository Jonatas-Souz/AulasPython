import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#Declaração de cariaceis
#Informações tela
largura = 640
altura = 480
titulo_janela = "Snake Game"

#Informações Snake
x_snake = largura/2
y_snake = altura/2
width_snake = height_snake = 20
lista_snake = []

#Infomações maçã
x_maca = randint(40,600)
y_maca = randint(40,440)
width_maca = height_maca = 20

#Informações de pontuação
fonte = pygame.font.SysFont('arial', 15, True, False)
pontos = 0 

#Informações Movimento
velocidade = 10
movimento_x = velocidade
movimento_y = 0
key_a = key_s = key_w = False
key_d = True

def reiniciarJogo():
    global pontos, x_snake, y_snake, lista_cabeca_snake, lista_snake, x_maca,y_maca,morreu,velocidade,key_a,key_d,key_s,key_w
    
    pontos = 0
    velocidade = 5
    x_maca = randint(40,600)
    y_maca = randint(40,430)
    lista_cabeca_snake = []
    lista_snake = []
    x_snake = largura/2
    y_snake = largura/2
    key_a = key_s = key_w = False
    key_d - True
    morreu = False
    
#Informação 
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption(titulo_janela)

relogio = pygame.time.Clock()

while True:
    tela.fill((250,250,210)) #Cor de fundo da tela
    relogio.tick(30)#Time
    mensagem = f'Ponto: {pontos}'
    caixaDeTexto = fonte.render(mensagem, True,(0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
    #Movimentos continuos
        if event.type == KEYDOWN:
            if event.key == K_a and not(key_d):
                movimento_x = -velocidade
                movimento_y = 0
                key_w = key_s = key_d = False
                key_a = True
                
            elif event.key == K_d and not(key_a):
                movimento_x = velocidade
                movimento_y = 0
                key_a = key_s = key_w = False
                key_d = True
                                
            elif event.key == K_w and not(key_s):
                movimento_x = 0
                movimento_y = -velocidade
                key_a = key_s = key_d = False
                key_w = True
                
            elif event.key == K_s and not(key_w):
                movimento_x = 0
                movimento_y = +velocidade
                key_a = key_s = key_d = False
                key_s = True
                
            
                
    x_snake += movimento_x
    y_snake += movimento_y
    
    # #Teclado segurar tecla
    # if pygame.key.get_pressed()[K_a]:
    #     x_snake -= 10
    # elif pygame.key.get_pressed()[K_d]:
    #     x_snake += 10
    # elif pygame.key.get_pressed()[K_w]:
    #     y_snake -= 10
    # elif pygame.key.get_pressed()[K_s]:
    #     y_snake += 10
    
    if x_snake >= largura: #Delimitar a tela para objeto voltar do inicio
        x_snake = 0
    elif x_snake <= 0:
        x_snake = largura
        
    elif y_snake >= altura:
        y_snake = 0
    elif y_snake <= 0:
        y_snake = altura

    #Define caracteristicas da cobra e da maçã
    cobra = pygame.draw.rect(tela, (0,255,127), (x_snake,y_snake,width_snake,height_snake))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,width_maca,height_maca))
    
    #Colisão da cobra com a maçã        
    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(40,440)
        pontos += 1
        velocidade += 2
        
    if len(lista_snake) > pontos:
        del lista_snake[0]
    #Lista para guardar posição da cobra
    lista_cabeca_snake = []  
    lista_cabeca_snake.append(x_snake)
    lista_cabeca_snake.append(y_snake)
    
    lista_snake.append(lista_cabeca_snake)
    
    for XeY in lista_snake: #Posição x da cobra e y
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], width_snake, height_snake))
        
    if lista_snake.count(lista_cabeca_snake) > 1:
        morreu = True
        
        while morreu:
            tela.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        morreu == False
                        reiniciarJogo()
                    
            pygame.display.update()
    
    tela.blit(caixaDeTexto, (400,40))
    pygame.display.update()