import pygame #Importante instalar pygame no
from random import randint
from pygame.locals import *
from sys import exit #Importa do sistema
pygame.init()

pontos = 0
#Declaração de variaveis
altura = 480
largura = 640
tituloJanela = "Primeiro Jogo"
#Informações Circulo
pos_x_circ = 400
pos_y_circ = 100
radius_circ = 20 #Raio do circulo
rgb_circle = (40, 100, 255)

#Informações Retangulo
pos_x_rect = 500
pos_y_rect = 200
width_rect = 25 #altura do objeto
ehight_rect = 25 #largura do objeto

#Fonte Utilizada
fonte = pygame.font.SysFont('arial', 40, True, False)

tela = pygame.display.set_mode((largura,altura)) #Dentro da chave utiliza Tupla, Dentro tem as informações de medida de tela
pygame.display.set_caption(tituloJanela)
relogio = pygame.time.Clock()#Muda o tempo do Clock

while True:
    relogio.tick(30)#30% do clock interno
    tela.fill((0,0,0))#Pinta a tela de preto onde o objeto passou
    mensagem = f'Pontos: {pontos}' #Pontos do jogo
    caixaTexto = fonte.render(mensagem, False, (255,255,255))
    
    for event in pygame.event.get(): #Monitorar botão, mouser e tela 
        
        if event.type == QUIT: #Quando apertar o "X" da janela
            pygame.quit()
            exit() #Fecha o jogo

        # if event.type == KEYDOWN: #Click teclado
            # if event.key == K_a or event.key == K_LEFT: #Se aperta tecla "A"
            #     pos_x_circ -= 5
            # if event.key == K_d or event.key == K_RIGHT: #Se aperta tecla "D"
            #     pos_x_circ += 5
            # if event.key == K_w or event.key == K_UP: #Se aperta tecla "W"
            #     pos_y_circ -= 5
            # if event.key == K_s or event.key == K_DOWN: #Se aperta tecla "S"
            #     pos_y_circ += 5
            
    #Manter teclado precionado
    if pygame.key.get_pressed()[K_a]:
        pos_x_circ -= 10
    elif pygame.key.get_pressed()[K_d]:
        pos_x_circ += 10
    elif pygame.key.get_pressed()[K_w]:
        pos_y_circ -= 10
    elif pygame.key.get_pressed()[K_s]:
        pos_y_circ += 10
        
    if pos_x_circ >= largura: #Delimitar a tela para objeto voltar do inicio
        pos_x_circ = 0
    elif pos_x_circ <= 0:
        pos_x_circ = largura
    elif pos_y_circ >= altura:
        pos_y_circ = 0
    elif pos_y_circ <= 0:
        pos_y_circ = altura
        
    #Criando um retangulo   #RGB 0-255   #Cordenada (X Y) e medida do objeto
    retangulo = pygame.draw.rect(tela, (255, 0, 0), (pos_x_rect,pos_y_rect,width_rect,ehight_rect))
    
    #Crindo um Circulo        #RGB             #Cordenada (X Y), e raio do circulo
    circulo = pygame.draw.circle(tela, (rgb_circle), (pos_x_circ,pos_y_circ), radius_circ)
    
    if retangulo.colliderect(circulo):
        pos_x_rect = randint(0,640)
        pos_y_rect = randint(0,480)
        pontos += 1
        
                           #Exio x e y
    tela.blit(caixaTexto, (400,40)) #Caixa de texto pontos
    pygame.display.update()#Manter a janela do jogo
