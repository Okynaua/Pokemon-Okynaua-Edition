import pygame, sys
from data.menu import *
from data.batalha import *


class Jogo:
    def __init__(self):
        #Iniciando o pygame
        pygame.init()

        #Importa o Menu para o Jogo
        self.menu = Menu(self)

        #Importa a Batalha para o Jogo
        self.batalha = Batalha(self)

        #Configurando a Janela
        self.largura, self.altura = 800, 600
        self.janela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Pokémon')
        pygame.display.set_icon(pygame.image.load('data/Sprites/pokeball.png'))

        #Definindo o Nome da Fonte e as Teclas Usadas
        self.fonte = 'data/Fontes/joystix_monospace.ttf'
        self.ENTER, self.cima, self.baixo, self.esquerda, self.direita, self.ESC = False, False, False, False, False, False

    def checar_eventos(self):
        for event in pygame.event.get():

            #Fecha o Jogo se o Usuario Aperta o X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Aciona as Teclas de Ação se pressionadas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: self.ENTER = True
                if event.key == pygame.K_UP: self.cima = True
                if event.key == pygame.K_DOWN: self.baixo = True
                if event.key == pygame.K_LEFT: self.esquerda = True
                if event.key == pygame.K_RIGHT: self.direita = True
                if event.key == pygame.K_ESCAPE: self.ESC = True

                #Tela Cheia
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()

    def resetar_teclas(self):
        #Reseta as Teclas de Ação
        self.ENTER, self.cima, self.baixo, self.esquerda, self.direita, self.ESC = False, False, False, False, False, False

    def imprimir_imagem(self, imagem, x=400, y=300):
        #Imprime na tela imagem em suas determinadas coordenadas 
        imagem_rect = imagem.get_rect()
        imagem_rect.center = (x,y)
        self.janela.blit(imagem, imagem_rect)

    def escrever_texto(self, texto, tamanho, cor, x, y, orientacao):
        #Escreve texto com suas determinadas caracteristicas
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto_superf = fonte.render(texto, True, (cor))
        texto_rect = texto_superf.get_rect()
        if orientacao == 'centro': texto_rect.center = (x,y)
        if orientacao == 'sup_esq': texto_rect.topleft = (x,y)
        self.janela.blit(texto_superf, texto_rect)

        #Retorna as coordenadas do retangulo para a localizacao das pokebolas na selecao de pokemon em Menu.escolher_pokemons
        return texto_rect

    def tocar_som(self, som, vezes=0, altura=0.1):
        #Toca um Som ou uma Musica com o volume adequado
        som.play(vezes)
        som.set_volume(altura)

    def conserta_enter_adiantado(self):
        #Conserta o Problema do Enter Adiantado (Melhor explicado em README.txt)
        while True:
            self.checar_eventos()
            if self.ENTER:
                self.resetar_teclas()
            else: break

    def loop(self):
        #Abre o Menu do Jogo e pega os Pokémons do jogo
        Pok1, Pok2 = self.menu.main_menu()

        #Inicia a Batalha com os determinados Pokémons
        self.batalha.loop(Pok1, Pok2)