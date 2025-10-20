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

def solicitarNome():
    nome = ""
    ativo = True

    while ativo:
        tela.fill((30,30,30))
        texto_titulo = fonteG.render("Desvie da Chuva",True,(0,255,0))
        tela.blit(texto_titulo,(largura // 2 - 160,80))
        
        texto_instrucao = fonte.render("Digite seu Nome e dê um Enter:",True,(254,123,152))
        tela.blit(texto_instrucao,(30,150))

        caixa = pygame.Rect(80,200,240,40)
        pygame.draw.rect(tela,(255,255,255),caixa,2)
        texto_nome = fonte.render(nome,True,(255,255,0))
        tela.blit(caixa.x + 10,caixa.y + 5)

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nome.strip() != "":
                    ativo = False
                elif evento.Key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                elif len(nome) <15:
                    nome += evento.unicode
    return nome

jogador,obstaculos,pontuacao = reiniciar_jogo()
fonte = pygame.font.Font(None,30)
fonteG = pygame.font.Font(None,48)
rodando = True
game_over = False
velJogador = 3
while rodando:
    # solicitarNome()
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            rodando=False

        if game_over and evento.type== pygame.KEYDOWN and evento.key== pygame.K_KP_ENTER:
            jogador,obstaculos,pontuacao = reiniciar_jogo()
            game_over = False 
        
    if not game_over:  
        teclas=pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador.x>0:
            # jogador.x -= velJogador
            velJogador -= 3
        if teclas[pygame.K_RIGHT] and jogador.x<=largura-jogador.width:
            # jogador.x += velJogador
            velJogador += 3

        if jogador.x <= 0:
            jogador.x = 0
        elif jogador.x >= largura - jogador.width:
            jogador.x = largura - jogador.width
        jogador.x += velJogador

        if random.randint(1,10)==1:
            obstaculos.append(pygame.Rect(random.randint(0,largura-30),0,30,30))
            
        for obstaculo in obstaculos:
            obstaculo.y+=8
            if obstaculo.colliderect(jogador):
                game_over= True

        obstaculos=[obstaculo for obstaculo in obstaculos if obstaculo.y<altura]
        pontuacao += 1 
    
    tela.fill((30,30,30))
    pygame.draw.rect(tela,(0,255,0),jogador)

    for obstaculo in obstaculos:
        pygame.draw.rect(tela,(255,0,0),obstaculo)
    texto_pontos= fonte.render(f'pontos:{pontuacao}',True,(255,255,255)) 
    tela.blit(texto_pontos,(largura-130,10))     
    if game_over:
        texto_game_over= fonte.render("GAME OVER!", True,(0,255,0)) 
        texto_reiniciar= fonte.render("Pressione ENTER para reiniciar",True,(255,255,255))
        tela.blit(texto_game_over,(largura//2-80,altura//2-30))
        tela.blit(texto_reiniciar,(largura//2-150,altura//22-10))
    pygame.display.flip()
    relogio.tick(30)
      
pygame.quit()