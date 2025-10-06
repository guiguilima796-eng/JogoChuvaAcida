import pygame

pygame.init()

largura,altura = 500,400
tela =pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Chuva ácida')

relogio = pygame.time.Clock()

jogador = pygame.Rect((largura//2) - 15,altura -30,30,30)


rodando = True 

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
        if jogador.x <= largura - 3:
            jogador.x += 3
    if teclas[pygame.K_DOWN]:
        if jogador.y <= altura - 3:
            jogador.y += 3
    if teclas[pygame.K_AT]:
        if jogador.y >= 3:
            jogador.y += 3
    tela.fill((30,30,30))    
    pygame.draw.rect(tela,(0,255,0),jogador)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
