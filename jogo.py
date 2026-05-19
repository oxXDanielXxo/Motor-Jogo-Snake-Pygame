import pygame
import random
import sys

# 1. Inicializa o motor do Pygame e o motor de Textos
pygame.init()
pygame.font.init()

# 2. Configurações da Tela e Cores
LARGURA = 600
ALTURA = 400
TAMANHO_BLOCO = 20

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL_CLARO = (50, 153, 213)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Operação Serpente - CEO")
relogio = pygame.time.Clock()

# CORREÇÃO TÁTICA: Usar 'None' garante que o motor utilize a fonte padrão inquebrável
fonte_texto = pygame.font.Font(None, 28)
fonte_placar = pygame.font.Font(None, 35)

def mostrar_placar(pontos):
    texto = fonte_placar.render(f"Pontos: {pontos}", True, AZUL_CLARO)
    tela.blit(texto, [10, 10])

def mensagem_game_over(msg, cor):
    texto = fonte_texto.render(msg, True, cor)
    tela.blit(texto, [LARGURA / 8, ALTURA / 3])

def rodar_jogo():
    fim_jogo = False
    tela_game_over = False 
    
    x = LARGURA / 2
    y = ALTURA / 2
    velocidade_x = 0
    velocidade_y = 0
    
    pixels = []
    tamanho_cobra = 1
    
    comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / 20.0) * 20.0
    comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / 20.0) * 20.0

    while not fim_jogo:
        
        while tela_game_over:
            tela.fill(PRETO)
            mensagem_game_over("VOCÊ FOI DESTRUÍDO! [C] Continuar ou [S] Sair", VERMELHO)
            mostrar_placar(tamanho_cobra - 1)
            pygame.display.update()
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                    tela_game_over = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        fim_jogo = True
                        tela_game_over = False
                    if evento.key == pygame.K_c:
                        rodar_jogo()
                        return # CORREÇÃO: Mata a instância antiga para evitar vazamento de memória

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidade_x == 0:
                    velocidade_x = -TAMANHO_BLOCO
                    velocidade_y = 0
                elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                    velocidade_x = TAMANHO_BLOCO
                    velocidade_y = 0
                elif evento.key == pygame.K_UP and velocidade_y == 0:
                    velocidade_y = -TAMANHO_BLOCO
                    velocidade_x = 0
                elif evento.key == pygame.K_DOWN and velocidade_y == 0:
                    velocidade_y = TAMANHO_BLOCO
                    velocidade_x = 0

        # Física e Movimentação
        x += velocidade_x
        y += velocidade_y

        if x >= LARGURA or x < 0 or y >= ALTURA or y < 0:
            tela_game_over = True

        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])
        
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                tela_game_over = True

        for pixel in pixels:
            pygame.draw.rect(tela, VERDE, [pixel[0], pixel[1], TAMANHO_BLOCO, TAMANHO_BLOCO])

        mostrar_placar(tamanho_cobra - 1)
        pygame.display.update()

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x = round(random.randrange(0, LARGURA - TAMANHO_BLOCO) / 20.0) * 20.0
            comida_y = round(random.randrange(0, ALTURA - TAMANHO_BLOCO) / 20.0) * 20.0

        relogio.tick(10)

    pygame.quit()
    sys.exit() # Garante o encerramento limpo da aplicação

rodar_jogo()