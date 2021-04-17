import pygame, sys


class Menu():
    def __init__(self, Jogo):
        #Importa as Funções do Jogo
        self.Jogo = Jogo

        #Sprites
        self.s_menu = pygame.image.load('data/Sprites/Menu_sem.png')
        self.s_titulo = pygame.image.load('data/Sprites/Menu_com.png')
        self.pok1 = pygame.image.load('data/Sprites/Escolha_Pokemon1.png')
        self.pok2 = pygame.image.load('data/Sprites/Escolha_Pokemon2.png.')
        self.s_pokebola = pygame.image.load('data/Sprites/Pokeball.png')
        self.s_controles = pygame.image.load('data/Sprites/Controles.png')

        #Sons e Musicas
        self.m_selecionar = pygame.mixer.Sound('data/Sons/selecionar.wav')
        self.m_abertura = pygame.mixer.Sound('data/Sons/fireRedAbertura.wav')

    def escolher_pokemons(self):
        #Escolha do Pokemon 1
        self.Pok1 = self.escolha(self.pok1)

        #Escolha do Pokemon 2
        self.Pok2 = self.escolha(self.pok2)

    def escolha(self, pok):
        Pok = 0

        while True:
            self.Jogo.checar_eventos()
            Pok_atual = Pok

            #Selecao para baixo
            if self.Jogo.baixo and Pok >= 6: Pok = 1
            elif self.Jogo.baixo: Pok += 1
            
            #Selecao para cima
            if self.Jogo.cima and Pok <= 1: Pok = 6
            elif self.Jogo.cima: Pok -= 1

            #Efeito Sonoro
            if Pok != Pok_atual:
                self.Jogo.tocar_som(self.m_selecionar)

            #Seleciona opcao atual
            if self.Jogo.ENTER and Pok != 0:
                self.Jogo.tocar_som(self.m_selecionar)
                if Pok == 6:
                    self.controles()
                else:
                    self.Jogo.resetar_teclas()
                    return Pok

            #Reseta as pokebolas
            self.fundo_da_selecao(pok)

            #Coloca as pokebolas na opcao selecionada atualmente
            if Pok == 1: #Eevee
                self.Jogo.imprimir_imagem(self.s_pokebola, self.Ex-25, 162)
                self.Jogo.imprimir_imagem(self.s_pokebola, 825-self.Ex, 162)
            if Pok == 2: #Pikachu
                self.Jogo.imprimir_imagem(self.s_pokebola, self.Px-25, 242)
                self.Jogo.imprimir_imagem(self.s_pokebola, 825-self.Px, 242)
            if Pok == 3: #Bulbassauro
                self.Jogo.imprimir_imagem(self.s_pokebola, self.Bx-25, 322)
                self.Jogo.imprimir_imagem(self.s_pokebola, 825-self.Bx, 322)
            if Pok == 4: #Mr. Mime
                self.Jogo.imprimir_imagem(self.s_pokebola, self.Mx-25, 402)
                self.Jogo.imprimir_imagem(self.s_pokebola, 825-self.Mx, 402)
            if Pok == 5: #Vileplume
                self.Jogo.imprimir_imagem(self.s_pokebola, self.Vx-25, 482)
                self.Jogo.imprimir_imagem(self.s_pokebola, 825-self.Vx, 482)
            if Pok == 6: #Controles
                self.Jogo.imprimir_imagem(self.s_pokebola, self.Ox-25, 572)
                self.Jogo.imprimir_imagem(self.s_pokebola, 825-self.Ox, 572)

            pygame.display.update()
            self.Jogo.resetar_teclas()

    def fundo_da_selecao(self, pok):
        #Recoloca o fundo do ambiente de selecao de pokemon, para resetar as pokebolas que indicam a escolha do jogador
        self.Jogo.janela.fill((0,0,0))
        self.Jogo.imprimir_imagem(pok, 400, 310)

        self.Ex = self.Jogo.escrever_texto("EEVEE", 50, (197,152,96), 400, 160, 'centro')[0]
        self.Px = self.Jogo.escrever_texto("PIKACHU", 50, (238,215,77), 400, 240, 'centro')[0]
        self.Bx = self.Jogo.escrever_texto("BULBASSAURO", 50, (139,203,182), 400, 320, 'centro')[0]
        self.Mx = self.Jogo.escrever_texto("MR. MIME", 50, (226,96,116), 400, 400, 'centro')[0]
        self.Vx = self.Jogo.escrever_texto("VILEPLUME", 50, (133,146,185), 400, 480, 'centro')[0]
        self.Ox = self.Jogo.escrever_texto("CONTROLES", 40, (255,255,255), 400, 570, 'centro')[0]
        #Os valores de x do retangulo são registrados para a localizacao das pokebolas

    def controles(self):
        #Mostra os Controles do Jogo
        while True:
            self.Jogo.checar_eventos()

            self.Jogo.imprimir_imagem(self.s_controles)
            pygame.display.update()

            if self.Jogo.ESC:
                self.Jogo.tocar_som(self.m_selecionar)
                break

    def main_menu(self):
        self.Menu_Aberto = True

        #Animação de Abertura
        self.Jogo.tocar_som(self.m_abertura, -1)
        self.Jogo.imprimir_imagem(self.s_menu)
        pygame.display.update()

        pygame.time.delay(4500) #Atraso para o titulo aparecer com o drop da musica :)
        pygame.event.get()

        pygame.display.set_caption('Pokémon: Okynaua Edition')
        pygame.display.set_icon(pygame.image.load('data/Sprites/icon.png'))
        self.Jogo.imprimir_imagem(self.s_titulo)
        self.Jogo.escrever_texto("Pressione Enter para iniciar", 30, (255,255,255), 400, 545, 'centro')
        pygame.display.update()
        pygame.time.delay(100)

        #Loop do Menu
        while self.Menu_Aberto:
            self.Jogo.checar_eventos()

            #Imprime o fundo do menu
            self.Jogo.imprimir_imagem(self.s_menu)
            self.Jogo.imprimir_imagem(self.s_titulo)
            self.Jogo.escrever_texto("Pressione Enter para iniciar", 30, (255,255,255), 400, 545, 'centro')
            pygame.display.update()

            if self.Jogo.ENTER:
                self.Jogo.tocar_som(self.m_selecionar)
                self.Jogo.resetar_teclas()

                #Escolha dos Pokémons
                self.escolher_pokemons()

                self.m_abertura.stop()
                #Retorna os Pokemons escolhidos para iniciar a batalha
                return self.Pok1, self.Pok2