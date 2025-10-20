import pygame
import random
pygame.init()


largura,altura=500,400
tela=pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Chuva ácida')

relogio=pygame.time.Clock()
def reiniciar_jogo():
    jogador=pygame.Rect((largura//2)-15,altura -30,30,30)
    obstaculos=[]
    pontuacao=0
    return jogador,obstaculos,pontuacao
jogador,obstaculos,pontuacao=reiniciar_jogo()
fonte=pygame.font.Font(None,30)
rodando= True
game_over=False
while rodando:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            rodando=False

        if game_over and evento.type== pygame.KEYDOWN and evento.key== pygame.K_r:
            jogador,obstaculo,pontuacao = reiniciar_jogo()
            game_over= False 
        
    if not game_over:  
        teclas=pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador.x>0:
            jogador.x-=3
        if teclas[pygame.K_RIGHT] and jogador.x<=largura-jogador.width:
            jogador.x+=3

        if random.randint(1,10)==1:
            obstaculos.append(pygame.Rect(random.randint(0,largura-30),0,30,30))
            
        for obstaculo in obstaculos:
            obstaculo.y+=8
            if obstaculo.colliderect(jogador):
                game_over= True

        obstaculos=[obstaculo for obstaculo in obstaculos if obstaculo.y<altura]
        pontuacao +=1
    
    tela.fill((30,30,30))
    pygame.draw.rect(tela,(0,255,0),jogador)

    for obstaculo in obstaculos:
        pygame.draw.rect(tela,(255,0,0),obstaculo)
    texto_pontos= fonte.render(f'pontos:{pontuacao}',True,(255,255,255)) 
    tela.blit(texto_pontos,(largura-130,10))     
    if game_over:
        texto_game_over= fonte.render("GAME OVER!", True,(0,255,0)) 
        texto_reiniciar= fonte.render("Pressione R para reiniciar",True,(255,255,255))
        tela.blit(texto_game_over,(largura//2-80,altura//2-30))
        tela.blit(texto_reiniciar,(largura//2-150,altura//22-10))
    pygame.display.flip()
    relogio.tick(30)
      
pygame.quit()