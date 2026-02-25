import pygame
import random

def mudar_cores():
    vermelho=random.randint(0,255)
    verde= random.randint(0,255)
    azul=random.randint(0,255)
    return (vermelho,verde,azul)
#inicializar pygame
pygame.init()
#variaveis para as cores
vermelho=0
verde=0
azul=0

#configurações da janela
LARGURA=800
ALTURA=600
tela= pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Exemplo com o python")

#definindo um clock para controlar FPS (Frames por segundo)
clock=pygame.time.Clock()
FPS= 60

#definindo a posição x e y no centro da tela
posicao_x_retangulo = LARGURA //2
posicao_y_retangulo= ALTURA//2
#definindo a velocidade em x e y do retangulo.
velocidade_x_retangulo= 5
velocidade_y_retangulo=5

rodando=True
while rodando:
    #preciso procurar o evento do usuario fechar a janela(inicio loop)
    for evento in pygame.event.get():
        #se o evento fechar o jogo existir
        if evento.type==pygame.QUIT:
            #muda a variavel rodando para False(encerra o loop)
            rodando=False

    #fim do loop de eventos
    #logica de movimentodo retangulo
    posicao_x_retangulo+=velocidade_x_retangulo
    posicao_y_retangulo+=velocidade_y_retangulo
#deteçção de colisao com as bordas da tela
    if posicao_x_retangulo>=LARGURA or posicao_x_retangulo<=0:
        velocidade_x_retangulo*=-1
        vermelho,verde,azul=mudar_cores()
    if posicao_y_retangulo>=ALTURA or posicao_y_retangulo<=0:
        velocidade_y_retangulo*=-1
        vermelho,verde,azul=mudar_cores()

    
    

    tela.fill((255,255,255)) #-- comando para pintar a tela(elemnentos gráficos)

    pygame.draw.rect(tela, (vermelho,verde,azul), (posicao_x_retangulo,posicao_y_retangulo,50,50))
#atualizando o fps
    pygame.display.flip() #atualiza a tela
    clock.tick(FPS)

pygame.quit()