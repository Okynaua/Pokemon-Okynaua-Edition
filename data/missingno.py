import pygame, sys
import random
from data.ataques import ataque

class Missingno():
    def __init__(self, Jogo, Batalha):
        #Importa as Funções do Jogo
        self.Jogo = Jogo

        #Importa as Funções, os Sprites e os Audios da Batalha
        self.Bat = Batalha

        #Música
        self.m_musica = pygame.mixer.Sound('data/Sons/Dark, Darker, Yet Darker.wav')

        #Efeitos Sonoros
        self.m_bug1 = pygame.mixer.Sound('data/Sons/Glitch1.wav')
        self.m_bug2 = pygame.mixer.Sound('data/Sons/Glitch2.wav')
        self.m_error = pygame.mixer.Sound('data/Sons/Error.wav')
        self.m_alarm = pygame.mixer.Sound('data/Sons/Alarm.wav')
        self.m_chaos = pygame.mixer.Sound('data/Sons/Chaos.wav')
        self.m_unfinished = pygame.mixer.Sound('data/Sons/Unfinished.wav')
        self.m_denial = pygame.mixer.Sound('data/Sons/Denial.wav')
        self.m_nothing = pygame.mixer.Sound('data/Sons/Nothing.wav')
        self.m_an_ending = pygame.mixer.Sound('data/Sons/An_Ending.wav')

        #Sprites
        self.s_barra_menor = pygame.image.load('data/Sprites/barra_2_menor.png')
        self.s_error = pygame.image.load('data/Sprites/Error2.png')
        self.s_error2 = pygame.image.load('data/Sprites/Error.png')
        self.s_alarm = pygame.image.load('data/Sprites/Alarm.png')
        self.s_unfinished = pygame.image.load('data/Sprites/Unfinished.png')

        #Missingno
        self.Pok_alvo = {
        'nome': "Missingno.",
        'sprite': pygame.image.load('data/Sprites/Missingno.png'),
        'ataques': [
        ataque('Error', 'Missingno', 100, 100, 100, 100),
        ataque('Alarm', 'Missingno', 90, 100, 100, 100),
        ataque('Chaos', 'Missingno', 180, 100, 100, 100),
        ataque('Unfinished', 'Missingno', 150, 100, 100, 100),
        ataque('Denial', 'Missingno', None, 100, 100, 100)]}
    
    def vida(self):
        #Calcula as vidas e como estao as barras de vida

        #Valores das Vidas
        if self.Pok1['vida'] > 50: self.Pok1['vida'] = 50
        if self.Pok2['vida'] > 50: self.Pok2['vida'] = 50
        if self.Pok_alvo['vida'] > 100: self.Pok_alvo = 100

        if self.Pok1['vida_atual'] > self.Pok1['vida']:
            self.Pok1['vida_atual'] -= 1
        if self.Pok1['vida_atual'] < self.Pok1['vida']:
            self.Pok1['vida_atual'] += 1

        if self.Pok2['vida_atual'] > self.Pok2['vida']:
            self.Pok2['vida_atual'] -= 1
        if self.Pok2['vida_atual'] < self.Pok2['vida']:
            self.Pok2['vida_atual'] += 1

        if self.Pok_alvo['vida_atual'] > self.Pok_alvo['vida']:
            self.Pok_alvo['vida_atual'] -= 1
        if self.Pok_alvo['vida_atual'] < self.Pok_alvo['vida']:
            self.Pok_alvo['vida_atual'] += 1

        if self.Pok1['vida'] < 0: self.Pok1['vida'] = 0
        if self.Pok2['vida'] < 0: self.Pok2['vida'] = 0
        if self.Pok_alvo['vida'] < 0: self.Pok_alvo['vida'] = 0

        #Cores das Barras de Vida
        if self.Pok1['vida_atual'] > 25: #Verde
            self.Pok1['vida_cor'] = (100,229,149)
        if self.Pok1['vida_atual'] <= 25: #Amarelo
            self.Pok1['vida_cor'] = (248,217,58)
        if self.Pok1['vida_atual'] <= 10: #Vermelho
            self.Pok1['vida_cor'] = (255,109,82)

        if self.Pok2['vida_atual'] > 25: #Verde
            self.Pok2['vida_cor'] = (100,229,149)
        if self.Pok2['vida_atual'] <= 25: #Amarelo
            self.Pok2['vida_cor'] = (248,217,58)
        if self.Pok2['vida_atual'] <= 10: #Vermelho
            self.Pok2['vida_cor'] = (255,109,82)

        if self.Pok_alvo['vida_atual'] > 50: #Verde
            self.Pok_alvo['vida_cor'] = (100,229,149)
        if self.Pok_alvo['vida_atual'] <= 50: #Amarelo
            self.Pok_alvo['vida_cor'] = (248,217,58)
        if self.Pok_alvo['vida_atual'] <= 20: #Vermelho
            self.Pok_alvo['vida_cor'] = (255,109,82)

        #Larguras das Barras de Vida
        self.Pok1['largura'] = self.Pok1['vida_atual']/50 * 160
        self.Pok2['largura'] = self.Pok2['vida_atual']/50 * 160
        self.Pok_alvo['largura'] = self.Pok_alvo['vida_atual']/100 * 160

        #Defina quais Pokemons estao vivos
        if self.Pok1['vida_atual'] > 0: self.Pok1['vivo'] = True
        else: self.Pok1['vivo'] = False
        if self.Pok2['vida_atual'] > 0: self.Pok2['vivo'] = True
        else: self.Pok2['vivo'] = False

        self.Pok_alvo['vivo'] = True
   
    def checar_vida(self):
        #Checa se a animação de vida acabou, para prosseguir com a batalha
        d1 = abs(self.Pok1['vida'] - self.Pok1['vida_atual'])
        d2 = abs(self.Pok2['vida'] - self.Pok2['vida_atual'])
        d3 = abs(self.Pok_alvo['vida'] - self.Pok_alvo['vida_atual'])
        if d1 < 1 and d2 < 1 and d3 < 1: self.vidas_certas = True
        else: self.vidas_certas = False

    def atualizar_vida(self):
        #Realiza a animacao da vida até os valores estarem corretos
        self.checar_vida()
        while self.vidas_certas == False:
            self.Jogo.imprimir_imagem(self.Bat.s_fundo)
            self.Jogo.imprimir_imagem(self.Pok1['sprite_costas'], 330, 290) if self.Pok1['vivo'] == True else None
            self.Jogo.imprimir_imagem(self.Pok2['sprite_costas'], 130, 290) if self.Pok2['vivo'] == True else None
            self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
            self.fundo_basico()
            pygame.display.update()
            pygame.time.delay(10)        

    def fundo_da_batalha(self, anima=True):
        #Dispõe todos os elementos do fundo da batalha durante a escolha das opcoes
        self.Jogo.imprimir_imagem(self.Bat.s_fundo)
        self.Jogo.imprimir_imagem(self.Pok1['sprite_costas'], 330, 290) if self.Pok1['vivo'] == True else None
        self.Jogo.imprimir_imagem(self.Pok2['sprite_costas'], 130, 290) if self.Pok2['vivo'] == True else None
        self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
        self.Jogo.imprimir_imagem(self.Bat.s_texto)
        self.Jogo.imprimir_imagem(self.Bat.s_opcoes)

        self.fundo_basico()

        self.Bat.escrever_caixa_de_texto("O quê fará", self.Cima, anima)
        self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']}?", self.Baixo, anima)

    def fundo_basico(self):
        #Fundo basico que pode ser usado em diversos momentos
        self.vida()
        self.checar_vida()
        pygame.draw.rect(self.Jogo.janela, self.Pok2['vida_cor'], (591, 301, self.Pok2['largura'], 13))
        pygame.draw.rect(self.Jogo.janela, self.Pok1['vida_cor'], (624, 387, self.Pok1['largura'], 13))
        pygame.draw.rect(self.Jogo.janela, self.Pok_alvo['vida_cor'], (172, 119, self.Pok_alvo['largura'], 13))
        self.Jogo.imprimir_imagem(self.s_barra_menor)
        self.Jogo.imprimir_imagem(self.Bat.s_vidaadv)
        self.Jogo.escrever_texto(f"{self.Pok_alvo['vida_atual']}/100", 25, (0,0,0), 190, 137, 'sup_esq')
        self.Jogo.escrever_texto(self.Pok2['nome'], 25, (0,0,0), 479, 255, 'sup_esq')
        self.Jogo.escrever_texto(self.Pok1['nome'], 25, (0,0,0), 513, 343, 'sup_esq')
        self.Jogo.escrever_texto(self.Pok_alvo['nome'], 25, (0,0,0), 60, 72, 'sup_esq')

    def animacoes(self, qual):
        #Animacoes de todos os ataques (sao muitas, eu sei :P)

        #"if self.Pok_out['vivo'] == True else None" checa se o Pokemon que nao esta sendo atacado esta vivo,
        #se ele nao estiver, seu sprite nao sera imprimido
        def Investida():
            x = self.Pok_atq['x']
            while x < self.Pok_atq['x'] + 150:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x += 20
            
            self.Jogo.tocar_som(self.Bat.m_tackle)

            while x > self.Pok_atq['x']:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x -= 20

            for x in range(2):
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.fundo_basico()
                pygame.display.update()
                pygame.time.delay(300)

        def Atq_Rapido():
            self.Jogo.tocar_som(self.Bat.m_quick_atack)
            x = self.Pok_atq['x']
            while x < self.Pok_atq['x'] + 150:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x += 30

            while x > 200:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x -= 30

            for x in range(2):
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.fundo_basico()
                pygame.display.update()
                pygame.time.delay(300)

        def Derrubada():
            x = self.Pok_atq['x']
            while x > self.Pok_atq['x'] - 150:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x -= 5

            while x < self.Pok_atq['x']:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.Jogo.imprimir_imagem(self.Bat.s_slam, 590, 140)

                self.fundo_basico()
                pygame.display.update()
                x += 25

            self.Jogo.tocar_som(self.Bat.m_tackle)
            self.Jogo.imprimir_imagem(self.Bat.s_slam, 590, 140)
            pygame.display.update()

            for x in range(2):
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.fundo_basico()
                pygame.display.update()
                pygame.time.delay(300)
        
        def Mordida():
            x = self.Pok_atq['x']
            while x < self.Pok_atq['x'] + 150:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x += 30
            
            self.Jogo.tocar_som(self.Bat.m_bite)
            self.Jogo.imprimir_imagem(self.Bat.s_bite, 590, 140)
            pygame.display.update()

            while x > self.Pok_atq['x']:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.Jogo.imprimir_imagem(self.Bat.s_bite, 590, 140)

                self.fundo_basico()
                pygame.display.update()
                x -= 20

            for x in range(2):
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.fundo_basico()
                pygame.display.update()
                pygame.time.delay(300)

        def Atq_Areia():
            x = self.Pok_atq['x']
            while x > self.Pok_atq['x'] - 100:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None        

                self.fundo_basico()
                pygame.display.update()
                x -= 10

            while x < self.Pok_atq['x']:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.Jogo.imprimir_imagem(self.Bat.s_sand, 590, 140)

                self.fundo_basico()
                pygame.display.update()
                x += 30

            self.Jogo.imprimir_imagem(self.Bat.s_sand, 590, 140)
            self.Jogo.tocar_som(self.Bat.m_tackle)
            pygame.display.update()

        def Chq_Trovao():
            self.Jogo.tocar_som(self.Bat.m_thunder)
            self.Jogo.imprimir_imagem(self.Bat.s_thunder, 600, 80)
            pygame.display.update()
            pygame.time.delay(1000)

        def Onda_Trovao():
            self.Jogo.tocar_som(self.Bat.m_wave)
            self.Jogo.imprimir_imagem(self.Bat.s_wave)
            self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
            pygame.display.update()
            pygame.time.delay(1000)

        def Time_Duplo():
            x1, x2 = self.Pok_atq['x'], self.Pok_atq['x']
            while x1 < self.Pok_atq['x'] + 150:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x1, 290)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x2, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x1 += 25
                x2 -= 25
            
            self.Jogo.tocar_som(self.Bat.m_double_team)

            while x1 > self.Pok_atq['x'] - 25:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x1, 290)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x2, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x1 -= 25
                x2 += 25

        def Batida():
            x = self.Pok_atq['x']
            while x < self.Pok_atq['x'] + 150:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x += 20
            
            self.Jogo.tocar_som(self.Bat.m_tackle)
            self.Jogo.imprimir_imagem(self.Bat.s_slam, 590, 140)
            pygame.display.update()

            while x > self.Pok_atq['x']:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Bat.s_slam, 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()
                pygame.display.update()
                x -= 20

            for x in range(2):
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.fundo_basico()
                pygame.display.update()
                pygame.time.delay(300)

        def Smnt_Prst():
            dx = 591 - self.Pok_atq['x']
            dy = 290 - 224
            Vx = dx/15
            Vy = dy/15
            x, y = self.Pok_atq['x'], 290
            self.Jogo.tocar_som(self.Bat.m_seed)
            while x < 595:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.Jogo.imprimir_imagem(self.Bat.s_seed, x, y)
                self.fundo_basico()
                pygame.display.update()
                y -= Vy
                x += Vx
            pygame.time.delay(1000)            

        def Smnt_Prst2():
            dx = 590 - self.Pok_atq['x']
            dy = 290 - 100
            Vx = dx/15
            Vy = dy/15
            x, y = 590, 140
            self.Jogo.tocar_som(self.Bat.m_heal)
            while x > self.Pok_atq['x']:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_heal, x, y)
                pygame.display.update()
                y += Vy
                x -= Vx
            pygame.time.delay(1000) 
        
        def Cauda_Chcot():
            for z in range(4):
                x = self.Pok_atq['x']
                while x < self.Pok_atq['x'] + 150:
                    self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                    self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                    self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                    self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                    self.fundo_basico()
                    pygame.display.update()
                    x += 60
                
                self.Jogo.tocar_som(self.Bat.m_quick_atack)

                while x > self.Pok_atq['x']:
                    self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                    self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                    self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                    self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None

                    self.fundo_basico()
                    pygame.display.update()
                    x -= 60

        def Raio_Solar():
            y = 140
            self.Jogo.tocar_som(self.Bat.m_solar_beam)
            while y < 290:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_solar, self.Pok_atq['x'], y)
                pygame.display.update()
                y += 10
            pygame.time.delay(1000)

        def Raio_Solar2():
            dx = 610 - self.Pok_atq['x']
            dy = 290 - 140
            Vx = dx/10
            Vy = dy/10
            x, y = self.Pok_atq['x'], 290
            self.Jogo.tocar_som(self.Bat.m_solar_beam)
            while y > 140:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_solar, x, y)
                pygame.display.update()
                y -= Vy
                x += Vx
            pygame.time.delay(1000)

        def Vinha_Chcot():
            x, y = 370, 190
            self.Jogo.tocar_som(self.Bat.m_vine_whip)
            while y < 290:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_vine, x, y)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                pygame.display.update()
                y += 10
                x += 10
            pygame.time.delay(1000)

        def Rugir():
            x, y = self.Pok_atq['x'], 315
            self.Jogo.tocar_som(self.Bat.m_growl)
            while y > 0:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.Jogo.imprimir_imagem(self.Bat.s_growl, x, y)
                self.fundo_basico()
                pygame.display.update()
                y -= 18
                x += 540/11
            pygame.time.delay(1000)
        
        def Barreira():
            y = 510
            self.Jogo.tocar_som(self.Bat.m_barrier)
            while y > 290:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.Jogo.imprimir_imagem(self.Bat.s_barrier, self.Pok_atq['x'], y)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Bat.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.Bat.escrever_caixa_de_texto("Barreira!", self.Baixo, False)
                y -= 4
                pygame.display.update()

        def Confusao():
            x, y = 200, 150
            self.Jogo.tocar_som(self.Bat.m_solar_beam)
            while y < 450:
                self.Jogo.imprimir_imagem(self.Bat.s_confusion, x, y)
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Bat.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.Bat.escrever_caixa_de_texto("Confusão!", self.Baixo, False)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                pygame.display.update()
                y += 7
                x += 28/3
        
        def Meditação():
            x, y = 600, 450
            self.Jogo.tocar_som(self.Bat.m_solar_beam)
            while y > 150:
                self.Jogo.imprimir_imagem(self.Bat.s_confusion, x, y)
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Bat.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.Bat.escrever_caixa_de_texto("Meditação!", self.Baixo, False)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                pygame.display.update()
                y -= 7
                x -= 28/3            

        def Duplo_Tapa():
            x = 550
            self.Jogo.tocar_som(self.Bat.m_slap)
            while x < 650:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_slap, x, 180)
                pygame.display.update()
                x += 10

        def Raio_Psqc():
            xp, yp = self.Pok_atq['x'], 290
            xc, yc = 200, 150
            self.Jogo.tocar_som(self.Bat.m_psybeam)
            while yp > 0:
                self.Jogo.imprimir_imagem(self.Bat.s_confusion, xc, yc)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.Jogo.imprimir_imagem(self.Bat.s_psybeam, xp, yp)
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Bat.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.Bat.escrever_caixa_de_texto("Raio Psíquico!", self.Baixo, False)
                self.fundo_basico()
                pygame.display.update()
                yp -= 7
                xp += 280/11
                yc += 7
                xc += 28/3
            pygame.time.delay(1000)            
        
        def Absorver():
            self.Jogo.tocar_som(self.Bat.m_tackle)
            self.Jogo.imprimir_imagem(self.Bat.s_slam, 590, 140)
            pygame.display.update()
            pygame.time.delay(1000)

            dx = 590 - self.Pok_atq['x']
            dy = 290 - 100
            Vx = dx/15
            Vy = dy/15
            x, y = 590, 140
            self.Jogo.tocar_som(self.Bat.m_heal)
            while x > self.Pok_atq['x']:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_heal, x, y)
                pygame.display.update()
                y += Vy
                x -= Vx
            pygame.time.delay(1000) 

        def Po_Venenoso():
            dx = 631 - self.Pok_atq['x']
            dy = 290 - 165
            Vx = dx/20
            Vy = dy/20
            x, y = self.Pok_atq['x'], 290
            self.Jogo.tocar_som(self.Bat.m_po)
            while y > 160:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_poison, x, y)
                pygame.display.update()
                y -= Vy
                x += Vx
            pygame.time.delay(1000)

        def Po_Venenoso2():
            self.Jogo.tocar_som(self.Bat.m_po)
            self.Jogo.imprimir_imagem(self.Bat.s_poison, 631, 165)
            pygame.display.update()
            pygame.time.delay(1000)

        def Po_de_Sono():
            dx = 631 - self.Pok_atq['x']
            dy = 290 - 165
            Vx = dx/20
            Vy = dy/20
            x, y = self.Pok_atq['x'], 290
            self.Jogo.tocar_som(self.Bat.m_po)
            while y > 160:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_sleep, x, y)
                pygame.display.update()
                y -= Vy
                x += Vx
            pygame.time.delay(1000)

        def Po_de_Sono2():
            x, y = 590, 140
            self.Jogo.tocar_som(self.Bat.m_sleeping)
            while y > 30:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok1['sprite_costas'], self.Pok1['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok2['sprite_costas'], self.Pok2['x'], 290)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Jogo.imprimir_imagem(self.Bat.s_sleeping, x, y)
                pygame.display.update()
                x += 2.5
                y -= 2.5
            pygame.time.delay(1000)

        def Aroma_Doce():
            dx = 610 - self.Pok_atq['x']
            dy = 290 - 160
            Vx = dx/30
            Vy = dy/30
            x, y = self.Pok_atq['x'], 290
            self.Jogo.tocar_som(self.Bat.m_sweet)
            while y > 160:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_sweet, x, y)
                pygame.display.update()
                y -= Vy
                x += Vx
            pygame.time.delay(1000)            
        
        def Petalas():
            y = 140
            self.Jogo.tocar_som(self.Bat.m_petal)
            while y < 300:
                self.Jogo.imprimir_imagem(self.Bat.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
                self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.Bat.s_petal, self.Pok_atq['x'], y)
                pygame.display.update()
                y += 8
            pygame.time.delay(1000)

            Derrubada()
        
        #ANIMACOES DO MISSINGNO

        def Error():
            self.m_musica.set_volume(0)
            self.Jogo.tocar_som(self.m_error)
            self.Jogo.imprimir_imagem(self.s_error)
            pygame.display.update()
            self.Jogo.imprimir_imagem(self.Pok_atq['sprite'], 590, 140)
            self.Jogo.imprimir_imagem(self.inimigo['sprite_costas'], self.inimigo['x'], 290)
            self.Jogo.imprimir_imagem(self.outro['sprite_costas'], self.outro['x'], 290) if self.outro['vivo'] == True else None
            for x in range(10):
                self.Jogo.imprimir_imagem(self.s_error2, self.inimigo['x'], 290)
                self.Jogo.imprimir_imagem(self.s_error2, self.outro['x'], 290)
                pygame.display.update()
                pygame.time.delay(200)
            self.m_musica.set_volume(0.1)
            self.Jogo.imprimir_imagem(self.Bat.s_texto)
    
        def Alarm():
            self.Jogo.tocar_som(self.m_alarm)
            self.Jogo.imprimir_imagem(self.s_alarm)
            pygame.display.update()
            pygame.event.get(); pygame.time.delay(3700); pygame.event.get()
            self.Jogo.janela.fill((0,0,0))
            self.Jogo.imprimir_imagem(self.Pok_atq['sprite'],  400, 290)
            pygame.display.update()
            pygame.event.get(); pygame.time.delay(2000); pygame.event.get()
            self.Jogo.imprimir_imagem(self.Bat.s_texto)

        def Chaos():
            self.Jogo.tocar_som(self.m_chaos)
            for x in range(20):
                self.Jogo.imprimir_imagem(self.Bat.s_fundo, random.randrange(0, 800), random.randrange(0, 600))
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite'], random.randrange(0, 800), random.randrange(0, 600))
                self.Jogo.imprimir_imagem(self.inimigo['sprite_costas'], random.randrange(0, 800), random.randrange(0, 600))
                self.Jogo.imprimir_imagem(self.outro['sprite_costas'], random.randrange(0, 800), random.randrange(0, 600)) if self.outro['vivo'] == True else None
                pygame.display.update()
                pygame.time.delay(100)
            self.Jogo.imprimir_imagem(self.Bat.s_texto)

        def Unfinished():
            self.Jogo.tocar_som(self.m_unfinished)
            pygame.time.delay(3933); pygame.event.get()
            self.Jogo.imprimir_imagem(self.s_unfinished, self.inimigo['x'], 290)
            pygame.display.update()
            pygame.time.delay(2000); pygame.event.get()

        def Denial():
            self.Jogo.tocar_som(self.m_denial)
            self.m_musica.set_volume(0)
            self.Jogo.janela.fill((0,0,0))
            self.Jogo.imprimir_imagem(self.Pok_atq['sprite'], 590, 140)
            self.Jogo.imprimir_imagem(self.outro['sprite_costas'], self.outro['x'], 290) if self.outro['vivo'] == True else None
            pygame.display.update()
            pygame.time.delay(367)
            self.m_musica.set_volume(0.1)
            self.Jogo.imprimir_imagem(self.Bat.s_texto)

        #Selecao da animacao
        if qual == "Investida": Investida()
        if qual == "Atq. Rapido": Atq_Rapido()
        if qual == "Derrubada": Derrubada()
        if qual == "Mordida": Mordida()
        if qual == "Atq. Areia": Atq_Areia()
        if qual == "Chq. Trovão": Chq_Trovao()
        if qual == "Onda Trovão": Onda_Trovao()
        if qual == "Time Duplo": Time_Duplo()
        if qual == "Batida": Batida()
        if qual == "Smnt. Prst.": Smnt_Prst()
        if qual == "Smnt. Prst.2": Smnt_Prst2()
        if qual == "Cauda Chcot.": Cauda_Chcot()
        if qual == "Raio Solar": Raio_Solar()
        if qual == "Raio Solar2": Raio_Solar2()
        if qual == "Vinha Chcot.": Vinha_Chcot()
        if qual == "Rugir": Rugir()
        if qual == "Barreira": Barreira()
        if qual == "Confusão": Confusao()
        if qual == "Meditação": Meditação()
        if qual == "Duplo Tapa": Duplo_Tapa()
        if qual == "Raio Psqc.": Raio_Psqc()
        if qual == "Absorver": Absorver()
        if qual == "Pó Venenoso": Po_Venenoso()
        if qual == "Pó Venenoso2": Po_Venenoso2()
        if qual == "Pó de Sono": Po_de_Sono()
        if qual == "Pó de Sono2": Po_de_Sono2()
        if qual == "Aroma Doce": Aroma_Doce()
        if qual == "Pétalas": Petalas()
        if qual == "Error": Error()
        if qual == "Alarm": Alarm()
        if qual == "Chaos": Chaos()
        if qual == "Unfinished": Unfinished()
        if qual == "Denial": Denial()


    def F_Pok(self, Pok, outro_pok):
        #Derrota de um Pok Bom
        pygame.event.get()

        #Animacao do Pokemon descendo
        y = 290
        self.Jogo.tocar_som(self.Bat.m_faint)
        while y < 510:
            self.Jogo.imprimir_imagem(self.Bat.s_fundo)
            self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 590, 140)
            self.Jogo.imprimir_imagem(Pok['sprite_costas'], Pok['x'], y)
            self.Jogo.imprimir_imagem(outro_pok['sprite_costas'], outro_pok['x'], 290) if outro_pok['vivo'] == True else None
            self.Jogo.imprimir_imagem(self.Bat.s_texto)
            y += 3.8
            pygame.display.update()
        pygame.time.delay(1000)

        #Mensagem
        self.Jogo.imprimir_imagem(self.Bat.s_texto)
        self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} derrotou", self.Cima)
        self.Bat.escrever_caixa_de_texto(f"{Pok['nome']}!", self.Baixo)
        pygame.time.delay(1500)        

    def perderam(self):
        #Derrota dos Pokemons Bons
        pygame.event.get()

        self.m_musica.stop()
        self.Jogo.tocar_som(self.m_nothing, -1, 1)
        pygame.time.delay(1000)

        #Mensagem final de Vitória
        self.Jogo.imprimir_imagem(self.Bat.s_texto)
        self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} te derrotou.", self.Cima)
        pygame.time.delay(2000)
        self.Jogo.imprimir_imagem(self.Bat.s_texto)
        self.Bat.escrever_caixa_de_texto('.', self.Cima); pygame.time.delay(500); pygame.event.get()
        self.Bat.escrever_caixa_de_texto(' .', self.Cima); pygame.time.delay(500); pygame.event.get()
        self.Bat.escrever_caixa_de_texto('  .', self.Cima); pygame.time.delay(500); pygame.event.get()
        pygame.display.update()

        while True:
            self.Jogo.checar_eventos()

            if self.Jogo.ENTER:
                self.Jogo.tocar_som(self.Bat.m_selecionar)
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Bat.escrever_caixa_de_texto(f"Parabéns {self.Pok_alvo['nome']}!", self.Cima)
                pygame.time.delay(5000)
                #Fecha o Jogo
                pygame.quit()
                sys.exit()

    def ganharam(self):
        #Vitoria dos Pokemons Bons
        pygame.event.get()

        #Animacao do Pokemon subindo
        y = 140
        while y > -240:
            self.Jogo.imprimir_imagem(self.Bat.s_fundo)
            self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], self.Pok_atq['x'], 290)
            self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 600, y)
            self.Jogo.imprimir_imagem(self.Pok_out['sprite_costas'], self.Pok_out['x'], 290) if self.Pok_out['vivo'] == True else None
            y -= 3
            pygame.display.update()

        self.m_musica.stop()
        pygame.time.delay(1000)

        #Mensagem Final do Jogo
        self.Jogo.imprimir_imagem(self.Bat.s_texto)
        self.Bat.escrever_caixa_de_texto(f"Parabéns!", self.Cima)
        self.Bat.escrever_caixa_de_texto(f"Você derrotou Missingno.!", self.Baixo)

        while True:
            self.Jogo.checar_eventos()

            if self.Jogo.ENTER:
                self.Jogo.tocar_som(self.Bat.m_selecionar)
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Jogo.tocar_som(self.m_an_ending, -1, 0.5)
                self.Bat.escrever_caixa_de_texto(f"Obrigado por jogar :)", self.Cima)
                self.Jogo.resetar_teclas()

                while True:
                    self.Jogo.checar_eventos()

                    if self.Jogo.ENTER:
                        self.Jogo.tocar_som(self.Bat.m_selecionar)
                        pygame.quit()
                        sys.exit()



    def entrada_da_batalha(self):
        #Definindo os Pokemons
        self.Pok1['vida'] = 50
        self.Pok2['vida'] = 50
        self.Pok1['vida_atual'] = 50
        self.Pok2['vida_atual'] = 50
        self.Pok1['falha_na_precisao'] = 0
        self.Pok2['falha_na_precisao'] = 0
        self.Pok1['falha_na_defesa'] = 1
        self.Pok2['falha_na_defesa'] = 1
        self.Pok_alvo['vida'] = 100
        self.Pok_alvo['vida_atual'] = 100
        self.Pok_alvo['falha_na_precisao'] = 0
        self.Pok_alvo['falha_na_defesa'] = 1

        self.Pok1['x'] = 330
        self.Pok2['x'] = 130

        self.Pok_atq = self.Pok1
        self.Pok_out = self.Pok2

        #Coordenadas y para escrever o texto na caixa de texto
        self.Cima, self.Baixo = 460, 510

        #Animação de Entrada
        self.Jogo.janela = pygame.display.set_mode((self.Jogo.largura, self.Jogo.altura), pygame.FULLSCREEN)
        self.Jogo.janela.fill((0,0,0))
        pygame.display.update()
        self.Jogo.tocar_som(self.m_musica, -1)
        pygame.event.get(); pygame.time.delay(6300); pygame.event.get()
        self.Jogo.imprimir_imagem(self.Pok_alvo['sprite'], 400, 300)
        pygame.display.update()
        pygame.event.get(); pygame.time.delay(6100); pygame.event.get()
        self.Jogo.janela.fill((255,255,255))
        pygame.display.update()
        
        #Iniciando a Batalha
        self.vida()
        self.fundo_da_batalha()
        self.Jogo.resetar_teclas()

    def batalha(self, Pok1, Pok2):
        self.Pok1 = Pok1
        self.Pok2 = Pok2

        #Introduz a Batalha
        self.entrada_da_batalha()

        #Variaveis importantes
        anima = False
        opcao = [1, 1]
        batalhando = True
        trocar_pokemons = False
        ultimo_atq = -1
        penultimo_atq = -1
        self.Pok1['solar_beam'] = False, 0
        self.Pok2['solar_beam'] = False, 0
        self.Pok_alvo['solar_beam'] = False, 0
        self.Pok1['Smnt. Prst.'], self.Pok1['Pó Venenoso'], self.Pok1['Pó de Sono'] = False, False, False
        self.Pok2['Smnt. Prst.'], self.Pok2['Pó Venenoso'], self.Pok2['Pó de Sono'] = False, False, False
        self.Pok_alvo['Smnt. Prst.'], self.Pok_alvo['Pó Venenoso'], self.Pok_alvo['Pó de Sono'] = False, False, False
        self.Pok1_desmaiado, self.Pok2_desmaiado = False, False

        #Loop
        while batalhando:
            if anima: self.Jogo.conserta_enter_adiantado() #A função só é usada uma fez, atraves da variavel anima que se torna False depois da primeira passagem pelo loop
            self.Jogo.checar_eventos()                

            #Troca os Turnos dos Pokemons
            if trocar_pokemons == True:
                if self.Pok_atq == self.Pok1:
                    self.Pok_atq = self.Pok2
                    self.Pok_out = self.Pok1

                elif self.Pok_atq == self.Pok2:
                    self.Pok_atq = self.Pok_alvo

                elif self.Pok_atq == self.Pok_alvo:
                    self.Pok_atq = self.Pok1
                    self.Pok_out = self.Pok2

                #Caso o Pokemon da vez esteja desmaiado
                if self.Pok_atq['vivo'] == False:
                    if self.Pok_atq == self.Pok1:
                        self.Pok_atq = self.Pok2
                        self.Pok_out = self.Pok1
                    elif self.Pok_atq == self.Pok2:
                        self.Pok_atq = self.Pok_alvo
                trocar_pokemons = False

            #Reseta ao estado fundamental da tela para se alguma alteracao for feita (desativa a animacao caso Missingno esteja atacando)
            vai_ter_animacao_de_desmaio = (self.Pok1['vida_atual'] <= 0 and self.Pok1_desmaiado == False) or (self.Pok2['vida_atual'] <= 0 and self.Pok2_desmaiado == False)
            if self.Pok_atq != self.Pok_alvo and not vai_ter_animacao_de_desmaio:
                self.fundo_da_batalha(anima)
            else: self.fundo_da_batalha(False)

            #Verifica se o Pokemon acordou
            if self.Pok_atq['Pó de Sono'] == 'acordou':
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']}", self.Cima)
                self.Bat.escrever_caixa_de_texto("acordou!", self.Baixo)
                self.Pok_atq['Pó de Sono'] = 0
                pygame.time.delay(2000)

            #Verifica se o Pokemon está dormindo
            if self.Pok_atq['Pó de Sono'] > 0:
                self.animacoes("Pó de Sono2")
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']}", self.Cima)
                self.Bat.escrever_caixa_de_texto("está dormindo!", self.Baixo)
                self.Pok_atq['Pó de Sono'] -= 1
                if self.Pok_atq['Pó de Sono'] == 0:
                    self.Pok_atq['Pó de Sono'] = 'acordou'
                pygame.time.delay(2000)
                trocar_pokemons = True
                continue
            
            #Verifica se o Pokemon carregou Raio Solar
            if self.Pok_atq['solar_beam'][0] == True:
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} usou", self.Cima)
                self.Bat.escrever_caixa_de_texto("Raio Solar!", self.Baixo)
                self.animacoes("Raio Solar2")
                self.Pok_alvo['vida'] -= self.Pok_atq['solar_beam'][1]
                self.Pok_atq['solar_beam'] = False, 0
                self.atualizar_vida()
                pygame.time.delay(500)
                trocar_pokemons = True

                #Verifica se o Pokemon usou Semente Paratisa (tem que repetir aqui porque o codigo nao chega no final do loop)
                if self.Pok_atq['Smnt. Prst.'] == True:
                    self.Jogo.imprimir_imagem(self.Bat.s_texto)
                    self.animacoes("Smnt. Prst.2")
                    self.Bat.escrever_caixa_de_texto(f"A vida de {self.Pok_alvo['nome']}", self.Cima)
                    self.Bat.escrever_caixa_de_texto("foi sugada!", self.Baixo)
                    self.Pok_alvo['vida'] -= 3
                    self.Pok_atq['vida'] += 3
                    pygame.time.delay(500)

                if self.Pok_alvo['vida'] > 0:
                    continue
            
            #ATAQUE DO MISSINGNO
            if self.Pok_atq == self.Pok_alvo:
                #Seleciona o Alvo
                Poks_bons = [self.Pok1, self.Pok2]
                self.inimigo = random.choice(Poks_bons)
                Poks_bons.remove(self.inimigo)
                self.outro = Poks_bons[0]

                if self.Pok1['vivo'] == False: self.inimigo = self.Pok2; self.outro = self.Pok1
                if self.Pok2['vivo'] == False: self.inimigo = self.Pok1; self.outro = self.Pok2

                #Escolhe o Ataque (que deve ser diferente do ultimo e do penultimo)
                while True:
                    atq_selecionado = random.randrange(0, 5)
                    if atq_selecionado != ultimo_atq and atq_selecionado != penultimo_atq: break
                penultimo_atq = ultimo_atq
                ultimo_atq = atq_selecionado

                ataque = self.Pok_alvo['ataques'][atq_selecionado]

                #Informa qual ataque foi usado
                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} usou", self.Cima, 'aleatorio')
                self.Bat.escrever_caixa_de_texto(f"{ataque.Nome}!", self.Baixo, True, 'aleatorio')
                pygame.time.delay(1000)

                #Usa o ataque
                acertou, dano = ataque.usar(self.Pok_alvo['falha_na_precisao'], self.inimigo['falha_na_defesa'])
                self.animacoes(ataque.Nome) if acertou != False else None
                pygame.event.get()

                #Ataques com efeitos especiais
                if acertou == 'Error':
                    self.inimigo['vida'] -= dano[0]
                    self.outro['vida'] -= dano[1]

                if acertou == 'Chaos':
                    self.inimigo['vida'] -= dano/2
                    self.outro['vida'] -= dano/2

                if acertou == 'Denial':
                    self.Pok_alvo['falha_na_defesa'] += 0.3
                    self.Jogo.imprimir_imagem(self.Bat.s_texto)
                    self.Bat.escrever_caixa_de_texto("A defesa de", self.Cima)
                    self.Bat.escrever_caixa_de_texto(f"{self.inimigo['nome']} caiu!", self.Baixo)
                    pygame.time.delay(1500)
                
                #Ataques com dano commum
                if acertou == True:
                    self.inimigo['vida'] -= dano

                #Errou o Ataque
                elif acertou == False:
                    pygame.time.delay(1000)
                    self.Jogo.imprimir_imagem(self.Bat.s_texto)
                    self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} errou", self.Cima)
                    self.Bat.escrever_caixa_de_texto("o ataque!", self.Baixo)
                    pygame.display.update()
                    pygame.time.delay(1500)
                pygame.event.get()

                #Mudança de Variaveis Importantes
                Voltou_A_Opcoes = True
                trocar_pokemons = True
                self.atualizar_vida()
                continue

            #Selecao da Acao (Pokemons Bons)

            #Checa se outra opção foi selecionada para tocar o efeito sonoro
            opcao_atual = opcao.copy()
            #Variavel que faz a animação do texto acontecer quando volta-se ao menu das opcoes
            Voltou_A_Opcoes = False

            #Navega-se pelas opcoes de acao por uma lista com coordenadas x e y, que podem ser 1 ou 2
            if opcao == [1, 1]: self.Jogo.escrever_texto("LUTAR", 30, self.Pok_atq['cor'], 495, 481, 'centro')
            if opcao == [1, 2]: self.Jogo.escrever_texto("POKÉMON", 30, self.Pok_atq['cor'], 520, 543, 'centro')
            if opcao == [2, 1]: self.Jogo.escrever_texto("BOLSA", 30, self.Pok_atq['cor'], 684, 481, 'centro')
            if opcao == [2, 2]: self.Jogo.escrever_texto("CORRER", 30, self.Pok_atq['cor'], 696, 542, 'centro')
            pygame.display.update()
            
            #Muda a opcao selecionada
            if self.Jogo.cima: opcao[1] -= 1
            if self.Jogo.baixo: opcao[1] += 1
            if self.Jogo.direita: opcao[0] += 1
            if self.Jogo.esquerda: opcao[0] -= 1

            for x in range(2):
                if opcao[x] <= 0: opcao[x] = 1
                if opcao[x] >= 3: opcao[x] = 2

            #Efeito Sonoro
            if opcao != opcao_atual:
                self.Jogo.tocar_som(self.Bat.m_selecionar)

            #Seleciona opcao atual
            if self.Jogo.ENTER and self.vidas_certas == True:
                self.Jogo.tocar_som(self.Bat.m_selecionar)
                self.Jogo.resetar_teclas()

                if opcao == [1, 1]: #LUTAR
                    menu_ataques = True

                    atq = [1, 1]
                    while menu_ataques:
                        self.Jogo.resetar_teclas()
                        self.Jogo.checar_eventos()

                        self.Jogo.imprimir_imagem(self.Bat.s_ataques)
                        self.Bat.escrever_ataques(self.Pok_atq)

                        atq_atual = atq.copy()
                        #Navega-se pelos ataques por uma lista com coordenadas x e y, que podem ser 1 ou 2 (Indica-se o PP do ataque e seu Tipo)
                        if atq == [1, 1]: atq_selecionado = 0
                        if atq == [1, 2]: atq_selecionado = 1
                        if atq == [2, 1]: atq_selecionado = 2
                        if atq == [2, 2]: atq_selecionado = 3

                        self.Bat.escrever_ataques(self.Pok_atq, atq_selecionado, self.Pok_atq['cor'])
                        self.Jogo.escrever_texto(f"{self.Pok_atq['ataques'][atq_selecionado].PPatual}/{self.Pok_atq['ataques'][atq_selecionado].PP}", 25, (0,0,0), 720, 482, 'centro')
                        self.Jogo.escrever_texto(f"{self.Pok_atq['ataques'][atq_selecionado].Tipo}", 25, (0,0,0), 558, 535, 'sup_esq')

                        #Muda o ataque selecionado
                        if self.Jogo.cima: atq[1] -= 1
                        if self.Jogo.baixo: atq[1] += 1
                        if self.Jogo.direita: atq[0] += 1
                        if self.Jogo.esquerda: atq[0] -= 1

                        for x in range(2):
                            if atq[x] <= 0: atq[x] = 1
                            if atq[x] >= 3: atq[x] = 2

                        #Efeito Sonoro
                        if atq != atq_atual:
                            self.Jogo.tocar_som(self.Bat.m_selecionar)

                        #Seleciona opcao atual

                        #Caso o PP seja 0
                        if self.Jogo.ENTER and self.Pok_atq['ataques'][atq_selecionado].PPatual <= 0:
                            self.Jogo.imprimir_imagem(self.Bat.s_texto)
                            self.Bat.escrever_caixa_de_texto('Não pode usar o ataque!', self.Cima)
                            pygame.time.delay(2000)
                            continue
                        
                        #Usa o Ataque
                        if self.Jogo.ENTER:
                            self.Jogo.tocar_som(self.Bat.m_selecionar)
                            self.Jogo.imprimir_imagem(self.Bat.s_texto)
                            pygame.display.update()
                            
                            #Informa qual ataque foi usado
                            if self.Pok_atq['ataques'][atq_selecionado].Nome == "Smnt. Prst.":
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} usou", self.Cima)
                                self.Bat.escrever_caixa_de_texto("Semente Parasita!", self.Baixo)
                            elif self.Pok_atq['ataques'][atq_selecionado].Nome == "Pétalas":
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} usou", self.Cima)
                                self.Bat.escrever_caixa_de_texto("Dança de Pétalas!", self.Baixo)                                                              
                            elif self.Pok_atq['ataques'][atq_selecionado].Nome != "Raio Solar":
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} usou", self.Cima)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['ataques'][atq_selecionado].Nome}!", self.Baixo)

                            #Diminui o PP do ataque
                            self.Pok_atq['ataques'][atq_selecionado].PPatual -= 1

                            #Usa o Ataque Selecionado
                            acertou, dano = self.Pok_atq['ataques'][atq_selecionado].usar(self.Pok_atq['falha_na_precisao'], self.Pok_alvo['falha_na_defesa'])
                            self.animacoes(self.Pok_atq['ataques'][atq_selecionado].Nome) if acertou != False and self.Pok_atq['ataques'][atq_selecionado].Nome != "Duplo Tapa" else None
                            pygame.event.get()

                            #Ataques que alteram os status
                            if acertou == 'Precisao_adv':
                                self.Pok_alvo['falha_na_precisao'] += 5
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto("A precisão de", self.Cima)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} caiu!", self.Baixo)
                                pygame.time.delay(1500)
                            
                            if acertou == 'Evasao_adv':
                                self.Pok_atq['falha_na_precisao'] -= 5
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto("A evasão de", self.Cima)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} caiu!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Defesa_adv':
                                self.Pok_alvo['falha_na_defesa'] += 0.1
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto("A defesa de", self.Cima)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} caiu!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Defesa_sua':
                                self.Pok_atq['falha_na_defesa'] -= 0.1
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto("A defesa de", self.Cima)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} subiu!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Ataque_seu':
                                self.Pok_alvo['falha_na_defesa'] += 0.1
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto("O ataque de", self.Cima)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} subiu!", self.Baixo)
                                pygame.time.delay(1500)

                            #Ataques Especiais com Efeito Extra
                            if acertou == 'Derrubada':
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Pok_alvo['vida'] -= dano[0]
                                self.Pok_atq['vida'] -= dano[1]
                                self.Bat.escrever_caixa_de_texto("Parte do dano", self.Cima)
                                self.Bat.escrever_caixa_de_texto("rebateu!", self.Baixo)
                                pygame.time.delay(1000)

                            if acertou == 'Absorver':
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Pok_alvo['vida'] -= dano[0]
                                self.Pok_atq['vida'] += dano[1]
                                self.Bat.escrever_caixa_de_texto(f"A vida de {self.Pok_alvo['nome']}", self.Cima)
                                self.Bat.escrever_caixa_de_texto("foi sugada!", self.Baixo)
                                pygame.time.delay(3000)

                            if acertou == 'Raio Solar':
                                self.Pok_atq['solar_beam'] = True, dano
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} carregou", self.Cima)
                                self.Bat.escrever_caixa_de_texto("o ataque!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Pó Venenoso':
                                self.Pok_atq['Pó Venenoso'] = True
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} foi", self.Cima)
                                self.Bat.escrever_caixa_de_texto("envenenado!", self.Baixo)
                                pygame.time.delay(1500)                             
                            
                            if acertou == "Pó de Sono":
                                self.Pok_alvo['Pó de Sono'] = dano
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} caiu", self.Cima)
                                self.Bat.escrever_caixa_de_texto("no sono!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Smnt. Prst.':
                                self.Pok_atq['Smnt. Prst.'] = True
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} foi", self.Cima)
                                self.Bat.escrever_caixa_de_texto("semeado!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Duplo Tapa':
                                for hit in range(len(dano)):
                                    self.animacoes("Duplo Tapa")
                                    self.Pok_alvo['vida'] -= dano[hit]
                                    self.atualizar_vida()
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto(f"Acertou {len(dano)} vezes!", self.Cima)
                                pygame.time.delay(1500)  

                            pygame.event.get()

                            #Ataques Comuns que apenas Causam Dano
                            if acertou == True:
                                self.Pok_alvo['vida'] -= dano

                            #Errou o Ataque
                            elif acertou == False:
                                pygame.time.delay(1000)
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} errou", self.Cima)
                                self.Bat.escrever_caixa_de_texto("o ataque!", self.Baixo)
                                pygame.display.update()
                                pygame.time.delay(1500)
                            
                            #Mudança de Variaveis Importantes
                            Voltou_A_Opcoes = True
                            menu_ataques = False
                            trocar_pokemons = True
                            self.atualizar_vida()

                            #Checa ataques que agem em turnos
                            if self.Pok_atq['Pó Venenoso'] == True:
                                self.Jogo.checar_eventos()
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.Bat.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} é ferido", self.Cima)
                                self.Bat.escrever_caixa_de_texto("pelo veneno!", self.Baixo)
                                self.Pok_alvo['vida'] -= 6.25
                                self.animacoes("Pó Venenoso2")
                                pygame.time.delay(500)

                            if self.Pok_atq['Smnt. Prst.'] == True:
                                self.Jogo.imprimir_imagem(self.Bat.s_texto)
                                self.animacoes("Smnt. Prst.2")
                                self.Bat.escrever_caixa_de_texto(f"A vida de {self.Pok_alvo['nome']}", self.Cima)
                                self.Bat.escrever_caixa_de_texto("foi sugada!", self.Baixo)
                                self.Pok_alvo['vida'] -= 3
                                self.Pok_atq['vida'] += 3
                                pygame.time.delay(500)

                            #Limites das Falhas na Defesa e na Precisao
                            if self.Pok_atq['falha_na_defesa'] < 0.4: self.Pok_atq['falha_na_defesa'] = 0.4
                            if self.Pok_atq['falha_na_precisao'] > 50: self.Pok_atq['falha_na_precisao'] = 50
                            self.atualizar_vida()
                            pygame.time.delay(1000)

                        #Volta ao menu das opcoes de acao
                        if self.Jogo.ESC:
                            Voltou_A_Opcoes = True
                            self.Jogo.tocar_som(self.Bat.m_selecionar)
                            menu_ataques = False

                        pygame.display.update()
                        self.Jogo.resetar_teclas()

                if opcao == [1, 2]: #POKÉMON
                    self.Jogo.imprimir_imagem(self.Bat.s_texto)
                    self.Bat.escrever_caixa_de_texto('Acho que 2x1 seria', self.Cima)
                    self.Bat.escrever_caixa_de_texto('um pouco injus-',self.Baixo)
                    pygame.time.delay(1000)
                    self.Jogo.imprimir_imagem(self.Bat.s_texto)
                    self.Bat.escrever_caixa_de_texto('Ok, talvez seja justo', self.Cima)
                    self.Bat.escrever_caixa_de_texto('nessa situação', self.Baixo)
                    pygame.time.delay(1000)
                    Voltou_A_Opcoes = True

                if opcao == [2, 1]: #BOLSA
                    self.Jogo.imprimir_imagem(self.Bat.s_texto)
                    self.Bat.escrever_caixa_de_texto('Você abre a bolsa!', self.Cima)
                    pygame.time.delay(1000)
                    pygame.event.get()
                    self.Jogo.imprimir_imagem(self.Bat.s_texto)
                    self.Bat.escrever_caixa_de_texto('.', self.Cima); pygame.time.delay(500)
                    self.Bat.escrever_caixa_de_texto(' .', self.Cima); pygame.time.delay(500)
                    self.Bat.escrever_caixa_de_texto('  .', self.Cima); pygame.time.delay(500)
                    self.Jogo.imprimir_imagem(self.Bat.s_texto)
                    self.Bat.escrever_caixa_de_texto('Não há nada dentro!', self.Cima)
                    pygame.time.delay(2000)
                    Voltou_A_Opcoes = True

                if opcao == [2, 2]: #CORRER
                    #Não corra por favor :(
                    self.Jogo.imprimir_imagem(self.Bat.s_texto)
                    self.Bat.escrever_caixa_de_texto("Sério, você vai", self.Cima)
                    self.Bat.escrever_caixa_de_texto("simplesmente fugir?", self.Baixo)
                    correndo = True

                    while correndo:
                        self.Jogo.checar_eventos()

                        #Corre
                        if self.Jogo.ENTER:
                            self.Jogo.tocar_som(self.Bat.m_selecionar)
                            self.Jogo.imprimir_imagem(self.Bat.s_texto)
                            self.Jogo.tocar_som(self.m_bug1)
                            self.Bat.escrever_caixa_de_texto("Tá bom então", self.Cima, True, (212, 0, 0))
                            self.Bat.escrever_caixa_de_texto(">:((((((((((((((((((((((((((", self.Baixo, True, (212, 0, 0))
                            pygame.quit()
                            sys.exit()

                        #Volta ao menu das opcoes de acao
                        if self.Jogo.ESC:
                            self.Jogo.tocar_som(self.Bat.m_selecionar)
                            correndo = False
                            Voltou_A_Opcoes = True

            #Checa o Desmaio do Pok1
            if self.Pok1['vida_atual'] <= 0 and self.Pok1_desmaiado == False:
                self.F_Pok(self.Pok1, self.Pok2)
                self.Pok1_desmaiado = True
                Voltou_A_Opcoes = True
            #Checa o Desmaio do Pok2
            if self.Pok2['vida_atual'] <= 0 and self.Pok2_desmaiado == False:
                self.F_Pok(self.Pok2, self.Pok1)
                self.Pok2_desmaiado = True
                Voltou_A_Opcoes = True

            #Checa Vitória dos Pokemons Bons
            if self.Pok_alvo['vida_atual'] <= 0:
                self.ganharam()
                batalhando = False          
            
            #Checa Vitória de Missingno
            if self.Pok1['vida_atual'] <= 0 and self.Pok2['vida_atual'] <= 0:
                self.perderam()
                pygame.quit()
                sys.exit()

            self.Jogo.resetar_teclas()

            #Realiza a animacao de escrever caso o jogador volte ao menu de opcoes de acao
            anima = True
            if Voltou_A_Opcoes: continue
            anima = False