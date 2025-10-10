import pygame
import random

pygame.init()

largura,altura = 500,400
tela =pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Chuva ácida')

relogio = pygame.time.Clock()



def reiniciar_jogo():
    jogador = pygame.Rect((largura//2) - 15,altura -30,30,30)
    obstaculos = []
    pontuacao = 0
    return jogador,obstaculos,pontuacao

jogador,obstaculos,pontuacao = reiniciar_jogo()
fonte = pygame.font.Font(None,30)
rodando = True 
game_over = False

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    

    # imagem = __file__('imgs/dowload.png')
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        if jogador.x >= 3:
            jogador.x -= 3
    if teclas[pygame.K_RIGHT]:
        if jogador.x <= (largura - jogador.width):
            jogador.x += 3
    # if teclas[pygame.K_DOWN]:
    #     if jogador.y <= (altura - jogador.width):
    #         jogador.y += 3
    # if teclas[pygame.K_]:
    #     if jogador.y >= (altura + 3):
    #         jogador.y += 3

    if(random.randint(1,20) == 1):
        obstaculos.append(pygame.Rect(random.randint(0,largura - 30),0,30,30))

    for obstaculo in obstaculos:
            obstaculo.y +=8
            if obstaculo.colliderect(jogador):
                rodando = False

    
    tela.fill((30,30,30))    

    pygame.draw.rect(tela,(0,255,0),jogador)

    for obstaculo in obstaculos:
        pygame.draw.rect(tela,(255,0,0),obstaculo)
    
    obstaculos = [obstaculo for obstaculo in obstaculos if obstaculo.y < altura]



    pygame.display.flip()

    pygame.time.Clock().tick(60)



pygame.quit()
