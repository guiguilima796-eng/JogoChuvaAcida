import pygame
import random
import sqlite3

def criar_banco():
    conexao = sqlite3.connect("ranking.db")
    cursor = conexao.cursor()
    cursor.execute("""create table if not exists jogadores(
        id integer primary key autoincrement,
        nome text unique,
        pontuacao integer default 0
    );""" 
    )
    conexao.commit()
    conexao.close()

def registrar_jogador(nome):
    conexao = sqlite3.connect("ranking.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO jogadores (nome,pontuacao) VALUES(?,0)",(nome,))
    conexao.commit()
    conexao.close()

def atualizar_pontuacao(nome,pontuacao):
    conexao = sqlite3.connect("ranking.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE jogadores set pontuacao = MAX(pontuacao,?) where nome = ?",(pontuacao,nome))
    conexao.commit()
    conexao.close()

def obter_ranking():
    conexao = sqlite3.connect("ranking.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT nome,pontuacao FROM jogadores order by pontuacao desc")
    ranking = cursor.fetchall()
    conexao.commit()
    conexao.close()
    return ranking
# inicializar o pygame
pygame.init()

# criacao da janela
largura, altura = 500, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Chuva ácida')

# frames per second (FPS)
relogio = pygame.time.Clock()

def reiniciar_jogo():
    # criação do jogador
    jogador = pygame.Rect((largura // 2) - 15, altura - 30, 30, 30)
    # criação de uma lista vazia de obstáculos
    obstaculos = []
    pontuacao = 0
    return jogador, obstaculos, pontuacao

def solicitar_nome():
    nome = ""
    ativo = True
    while ativo:
        tela.fill((30, 30, 30))
        texto_titulo = fonte_grande.render("Desvie da chuva", True, (0, 255, 0))
        tela.blit(texto_titulo, (largura // 2 - 160, 80))
        texto_instrucao = fonte.render("Digite seu nome e pressione ENTER:", True, (255,255,255))
        tela.blit(texto_instrucao, (50, 150))
        caixa = pygame.Rect(100, 200, 240, 40)
        pygame.draw.rect(tela, (255,255,255), caixa, 2)
        texto_nome = fonte.render(nome, True, (255,255,0))
        tela.blit(texto_nome, (caixa.x + 10, caixa.y + 5))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nome.strip() != "":
                    ativo = False   
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]
                elif len(nome) < 15:
                    nome += evento.unicode
    return nome



# estado inicial do jogo
criar_banco()
jogador, obstaculos, pontuacao = reiniciar_jogo()
velocidade_jogador = 3
fonte = pygame.font.Font(None, 30)
fonte_grande = pygame.font.Font(None, 48)
rodando = True
game_over = False
nome_jogador = solicitar_nome()
imagem_jogador=pygame.image.load('./imgs/boy.png').convert_alpha()
imagem_obstaculo=pygame.image.load('./imgs/gota.png').convert_alpha()
imagem_background=pygame.image.load('./imgs/background.jpg').convert_alpha()
imagem_jogador=pygame.transform.scale(imagem_jogador,(40,40))
imagem_obstaculo=pygame.transform.scale(imagem_obstaculo,(30,30))
imagem_background= pygame.transform.scale(imagem_background,(largura,altura))


# lógica de funcionamento do jogo
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if game_over and evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
            jogador, obstaculos, pontuacao = reiniciar_jogo()
            game_over = False

    if not game_over:
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador.x > 0:
            #jogador.x -= 3
            velocidade_jogador = -3
        if teclas[pygame.K_RIGHT] and jogador.x <= largura - jogador.width:
            #jogador.x += 3
            velocidade_jogador = 3

        if jogador.x < 0:
            jogador.x = 0
        elif jogador.x > largura - jogador.width:
            jogador.x = largura - jogador.width

        jogador.x += velocidade_jogador

        if random.randint(1,7) == 1:
            obstaculos.append(pygame.Rect(random.randint(0, largura - 30), 0, 30, 30))
        
        for obstaculo in obstaculos:
            obstaculo.y += 8
            if obstaculo.colliderect(jogador):
                game_over = True
        
        obstaculos = [obstaculo for obstaculo in obstaculos if obstaculo.y < altura]
        pontuacao += 1

    #tela.fill((30,30,30))
    tela.blit(imagem_background,(0,0))
    #pygame.draw.rect(tela,(0,255,0),jogador)
    tela.blit(imagem_jogador,jogador)
    # # desenhando o jogador
    # pygame.draw.rect(tela, (255,51,255), jogador)

    for obstaculo in obstaculos:
        pygame.draw.rect(tela, (255,0,0), obstaculo)
    
    texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, (255,255,255))
    tela.blit(texto_pontos, (largura - 130, 10))

    texto_nome = fonte.render(f"Jogador: {nome_jogador}", True, (255,255,255))
    tela.blit(texto_nome, (largura - 180, 40))

    if game_over:
        texto_game_over = fonte.render("GAME OVER!", True, (255, 255, 0))
        texto_reiniciar = fonte.render("Pressione R para reiniciar", True, (255, 255, 255))
        
        texto_final = fonte.render(f"Jogador: {nome_jogador} - Pontos: {pontuacao}", True, (0, 255, 0))
        
        tela.blit(texto_game_over, (largura // 2 - 80, altura // 2 - 30))
        tela.blit(texto_final, (largura // 2 - 130, altura // 2 - 10))
        tela.blit(texto_reiniciar, (largura // 2 - 150, altura // 2 + 10))

    # atualiza a tela
    pygame.display.flip()
    relogio.tick(30)

pygame.quit()