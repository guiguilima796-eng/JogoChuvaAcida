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
    
    pygame.draw.rect(tela,(0,255,0),jogador)

pygame.quit()
