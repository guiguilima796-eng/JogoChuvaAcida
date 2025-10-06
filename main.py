import pygame

pygame.init()

largura,altura = 500,400
tela =pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Chuva ácida')

relogio = pygame.time.Clock()

rodando = True 

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


