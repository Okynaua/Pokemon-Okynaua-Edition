import pygame, sys, random
from data.ataques import ataque
from data.missingno import Missingno


class Batalha():
    def __init__(self, Jogo):
        #Importa as Funções do Jogo
        self.Jogo = Jogo

        #Importa a Batalha Secreta
        self.Missingno = Missingno(Jogo, self)

        #Controla FPS
        self.clock = pygame.time.Clock()

        #Sprites da Interface
        self.s_fundo = pygame.image.load('data/Sprites/FundoPokemon.png')
        self.s_texto = pygame.image.load('data/Sprites/text_bar.png')
        self.s_ataques = pygame.image.load('data/Sprites/pp_bar.png')
        self.s_opcoes = pygame.image.load('data/Sprites/fgt_options.png')
        self.s_vidaadv = pygame.image.load('data/Sprites/barra_1.png')
        self.s_vidasua = pygame.image.load('data/Sprites/barra_2.png')
        self.s_bolsa = pygame.image.load('data/Sprites/Bolsa.png')

        #Sprites da Batalha
        self.s_slam = pygame.image.load('data/Sprites/Slam.png')
        self.s_bite = pygame.image.load('data/Sprites/Bite.png')
        self.s_sand = pygame.image.load('data/Sprites/Sand.png')
        self.s_thunder = pygame.image.load('data/Sprites/Thunder.png')
        self.s_wave = pygame.image.load('data/Sprites/Wave.png')
        self.s_solar = pygame.image.load('data/Sprites/Solar_Beam.png')
        self.s_vine = pygame.image.load('data/Sprites/Vine_Whip.png')
        self.s_growl = pygame.image.load('data/Sprites/Growl.png')
        self.s_seed = pygame.image.load('data/Sprites/Seed.png')
        self.s_barrier = pygame.image.load('data/Sprites/Barrier.png')
        self.s_confusion = pygame.image.load('data/Sprites/Confusion.png')
        self.s_slap = pygame.image.load('data/Sprites/Slap.png')
        self.s_psybeam = pygame.image.load('data/Sprites/Psybeam.png')
        self.s_poison = pygame.image.load('data/Sprites/Poison.png')
        self.s_sleep = pygame.image.load('data/Sprites/Sleep.png')
        self.s_sleeping = pygame.image.load('data/Sprites/Zzz.png')
        self.s_sweet = pygame.image.load('data/Sprites/Sweet.png')
        self.s_petal = pygame.image.load('data/Sprites/Petalas.png')
        self.s_heal = pygame.image.load('data/Sprites/Heart.png')

        #Músicas
        self.m_batalha = pygame.mixer.Sound('data/Sons/batalha.wav')
        self.m_vitoria = pygame.mixer.Sound('data/Sons/vitoria.wav')

        #Efeitos Sonoros
        self.m_selecionar = pygame.mixer.Sound('data/Sons/Selecionar.wav')
        self.m_tackle = pygame.mixer.Sound('data/Sons/Tackle.wav')
        self.m_quick_atack = pygame.mixer.Sound('data/Sons/Quick_Attack.wav')
        self.m_bite = pygame.mixer.Sound('data/Sons/Bite.wav')
        self.m_thunder = pygame.mixer.Sound('data/Sons/Thunder.wav')
        self.m_wave = pygame.mixer.Sound('data/Sons/Wave.wav')
        self.m_double_team = pygame.mixer.Sound('data/Sons/Double_Team.wav')
        self.m_solar_beam = pygame.mixer.Sound('data/Sons/Solar_Beam.wav')
        self.m_vine_whip = pygame.mixer.Sound('data/Sons/Vine_Whip.wav')
        self.m_growl = pygame.mixer.Sound('data/Sons/Growl.wav')
        self.m_seed = pygame.mixer.Sound('data/Sons/Seed.wav')
        self.m_barrier = pygame.mixer.Sound('data/Sons/Barrier.wav')
        self.m_slap = pygame.mixer.Sound('data/Sons/Slap.wav')
        self.m_psybeam = pygame.mixer.Sound('data/Sons/Psybeam.wav')
        self.m_po = pygame.mixer.Sound('data/Sons/Po.wav')
        self.m_sleeping = pygame.mixer.Sound('data/Sons/Sleep.wav')
        self.m_sweet = pygame.mixer.Sound('data/Sons/Sweet.wav')
        self.m_petal = pygame.mixer.Sound('data/Sons/Petal.wav')
        self.m_heal = pygame.mixer.Sound('data/Sons/Heal.wav')
        self.m_faint = pygame.mixer.Sound('data/Sons/Faint.wav')

    def que_pokemon(self, Pok):
        #Converte o numero que representa o Pokemon para suas caracteristicas atraves de um dicionario
        if Pok == 1:
            return {
                'nome': "Eevee",
                'sprite_frente': pygame.image.load('data/Sprites/FEevee.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CEevee.png'),
                'cor': (197,152,96),
                'ataques': [
                ataque('Investida', 'Normal', 40, 95, 35, 35),
                ataque('Atq. Rapido', 'Normal', 35, 100, 30, 30),
                ataque('Derrubada', 'Normal', 90, 85, 20, 20),
                ataque('Mordida', 'Sombrio', 60, 100, 10, 10),
                ataque('Atq. Areia', 'Terra', None, 100, 15, 15)]
            }
        if Pok == 2:
            return {
                'nome': "Pikachu",
                'sprite_frente': pygame.image.load('data/Sprites/FPikachu.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CPikachu.png'),
                'cor': (238,215,77),
                'ataques': [
                ataque('Chq. Trovão', 'Elétrico', 40, 100, 30, 30),
                ataque('Onda Trovão', 'Elétrico', None, 90, 20, 20),
                ataque('Time Duplo', 'Normal', None, 100, 15, 15),
                ataque('Batida', 'Normal', 80, 80, 20, 20),
                ataque('Cauda Chcot.', 'Normal', None, 100, 30, 30)]
            }
        if Pok == 3:
            return {
                'nome': "Bulbassauro",
                'sprite_frente': pygame.image.load('data/Sprites/FBulbassauro.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CBulbassauro.png'),
                'cor': (139,203,182),
                'ataques': [
                ataque('Smnt. Prst.', 'Planta', None, 90, 10, 10),
                ataque('Raio Solar', 'Planta', 120, 100, 10, 10),
                ataque('Vinha Chcot.', 'Planta', 45, 100, 25, 25),
                ataque('Rugir', 'Normal', None, 100, 40, 40),
                ataque('Cauda Chcot.', 'Normal', None, 100, 30, 30)]
            }
        if Pok == 4:
            return {
                'nome': "Mr. Mime",
                'sprite_frente': pygame.image.load('data/Sprites/FMr.Mime.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CMr.Mime.png'),
                'cor': (226,96,116),
                'ataques': [
                ataque('Barreira', 'Psíquico', None, 100, 20, 20),
                ataque('Confusão', 'Psíquico', 50, 100, 25, 25),
                ataque('Meditação', 'Psíquico', None, 100, 40, 40),
                ataque('Duplo Tapa', 'Normal', 15, 85, 10, 10),
                ataque('Raio Psqc.', 'Psíquico', 65, 100, 20, 20)]
            }
        if Pok == 5:
            return {
                'nome': "Vileplume",
                'sprite_frente': pygame.image.load('data/Sprites/FVileplume.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CVileplume.png'),
                'cor': (133,146,185),
                'ataques': [
                ataque('Absorver', 'Planta', 20, 100, 25, 25),
                ataque('Pó Venenoso', 'Venenoso', None, 85, 35, 35),
                ataque('Pó de Sono', 'Planta', None, 85, 15, 15),
                ataque('Aroma Doce', 'Normal', None, 100, 20, 20),
                ataque('Pétalas', 'Planta', 90, 100, 10, 10)]
            }

    def escrever_caixa_de_texto(self, texto, y, anima=True, cor=(255,255,255)):
        #Escreve uma mensagem na caixa de texto da batalha
        #A variavel anima diz se o texto tera animacao ou nao

        if cor == 'aleatorio': #Gera uma cor aleatoria para o texto
            r, g, b = random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)
            cor = (r,g,b)
    
        if anima == False: #Texto sem animacao
            self.Jogo.escrever_texto(texto, 35, cor, 35, y, 'sup_esq')

        else: #Texto com animacao
            txt = ''
            for letra in texto:
                txt += letra
                self.Jogo.escrever_texto(txt, 35, cor, 35, y, 'sup_esq')
                pygame.display.update()
                pygame.time.delay(25)

    def escrever_ataques(self, Pok, qual='todos', cor=(0,0,0)):
        #Escreve os nomes do ataques do Pokemon do Jogador
        fonte = pygame.font.Font(self.Jogo.fonte, 25)

        coords = [(25, 465), (25, 515), (275, 465), (275, 515)]

        if qual == 'todos':
            for ataque in Pok['ataques'][0:4]:
                ataque_superf = fonte.render(ataque.Nome, True, cor)
                ataque_rect = ataque_superf.get_rect()
                ataque_rect.topleft = coords[0]
                self.Jogo.janela.blit(ataque_superf, ataque_rect)
                coords.pop(0)
        else:
            for ataque in Pok['ataques'][qual:qual+1]:
                ataque_superf = fonte.render(ataque.Nome, True, cor)
                ataque_rect = ataque_superf.get_rect()
                ataque_rect.topleft = coords[qual]
                self.Jogo.janela.blit(ataque_superf, ataque_rect)
    
    def vida(self):
        #Calcula as vidas e como estao as barras de vida

        #Valores das Vidas
        if self.Pok1['vida'] > 50: self.Pok1['vida'] = 50
        if self.Pok2['vida'] > 50: self.Pok2['vida'] = 50

        if self.Pok1['vida_atual'] > self.Pok1['vida']:
            self.Pok1['vida_atual'] -= 1
        if self.Pok1['vida_atual'] < self.Pok1['vida']:
            self.Pok1['vida_atual'] += 1

        if self.Pok2['vida_atual'] > self.Pok2['vida']:
            self.Pok2['vida_atual'] -= 1
        if self.Pok2['vida_atual'] < self.Pok2['vida']:
            self.Pok2['vida_atual'] += 1

        if self.Pok1['vida'] < 0: self.Pok1['vida'] = 0
        if self.Pok2['vida'] < 0: self.Pok2['vida'] = 0

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
        
        #Larguras das Barras de Vida
        self.Pok1['largura'] = self.Pok1['vida_atual']/50 * 160
        self.Pok2['largura'] = self.Pok2['vida_atual']/50 * 160
   
    def checar_vida(self):
        #Checa se a animação de vida acabou, para prosseguir com a batalha
        d1 = abs(self.Pok1['vida'] - self.Pok1['vida_atual'])
        d2 = abs(self.Pok2['vida'] - self.Pok2['vida_atual'])
        if d1 < 1 and d2 < 1: self.vidas_certas = True
        else: self.vidas_certas = False

    def atualizar_vida(self):
        #Realiza a animacao da vida até os valores estarem corretos
        self.checar_vida()
        while self.vidas_certas == False:
            self.Jogo.imprimir_imagem(self.s_fundo)
            self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
            self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
            self.fundo_basico()
            pygame.display.update()
            pygame.time.delay(10)        

    def fundo_da_batalha(self, anima=True):
        #Dispõe todos os elementos do fundo da batalha durante a escolha das opcoes
        self.Jogo.imprimir_imagem(self.s_fundo)
        self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
        self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
        self.Jogo.imprimir_imagem(self.s_texto)
        self.Jogo.imprimir_imagem(self.s_opcoes)

        self.fundo_basico()

        self.escrever_caixa_de_texto("O quê fará", self.Cima, anima)
        self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']}?", self.Baixo, anima)

    def fundo_basico(self):
        #Fundo basico que pode ser usado em diversos momentos
        self.vida()
        self.checar_vida()
        pygame.draw.rect(self.Jogo.janela, self.Pok_atq['vida_cor'], (578, 338, self.Pok_atq['largura'], 13))
        pygame.draw.rect(self.Jogo.janela, self.Pok_alvo['vida_cor'], (172, 119, self.Pok_alvo['largura'], 13))
        self.Jogo.imprimir_imagem(self.s_vidasua)
        self.Jogo.imprimir_imagem(self.s_vidaadv)
        self.Jogo.escrever_texto(f"{self.Pok_atq['vida_atual']}/50", 25, (0,0,0), 635, 357, 'sup_esq')
        self.Jogo.escrever_texto(f"{self.Pok_alvo['vida_atual']}/50", 25, (0,0,0), 225, 137, 'sup_esq')
        self.Jogo.escrever_texto(self.Pok_atq['nome'], 25, (0,0,0), 470, 292, 'sup_esq')
        self.Jogo.escrever_texto(self.Pok_alvo['nome'], 25, (0,0,0), 60, 72, 'sup_esq')

    def animacoes(self, qual):
        #Animacoes de todos os ataques (sao muitas, eu sei :P)
        def Investida():
            x = 200
            while x < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 20
            
            self.Jogo.tocar_som(self.m_tackle)

            while x > 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 20

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)

        def Atq_Rapido():
            self.Jogo.tocar_som(self.m_quick_atack)
            x = 200
            while x < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 30

            while x > 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 30

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)

        def Derrubada():
            x = 200
            while x > 50:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 5

            while x < 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_slam, 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 25

            self.Jogo.tocar_som(self.m_tackle)
            self.Jogo.imprimir_imagem(self.s_slam, 600, 180)
            pygame.display.update()

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)
        
        def Mordida():
            x = 200
            while x < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 20
            
            self.Jogo.tocar_som(self.m_bite)
            self.Jogo.imprimir_imagem(self.s_bite, 600, 180)
            pygame.display.update()

            while x > 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_bite, 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 20

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)

        def Atq_Areia():
            x = 200
            while x > 100:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 10

            while x < 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_sand, 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 30

            self.Jogo.imprimir_imagem(self.s_sand, 600, 180)
            self.Jogo.tocar_som(self.m_tackle)
            pygame.display.update()

        def Chq_Trovao():
            self.Jogo.tocar_som(self.m_thunder)
            self.Jogo.imprimir_imagem(self.s_thunder, 600, 80)
            pygame.display.update()
            pygame.time.delay(1000)

        def Onda_Trovao():
            self.Jogo.tocar_som(self.m_wave)
            self.Jogo.imprimir_imagem(self.s_wave)
            self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
            pygame.display.update()
            pygame.time.delay(1000)

        def Time_Duplo():
            x1, x2 = 200, 200
            while x1 < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x1, 290)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x2, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x1 += 25
                x2 -= 25
            
            self.Jogo.tocar_som(self.m_double_team)

            while x1 > 175:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x1, 290)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x2, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x1 -= 25
                x2 += 25

        def Batida():
            x = 200
            while x < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 20
            
            self.Jogo.tocar_som(self.m_tackle)
            self.Jogo.imprimir_imagem(self.s_slam, 600, 180)
            pygame.display.update()

            while x > 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_slam, 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 20

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)

        def Smnt_Prst():
            x, y = 200, 290
            self.Jogo.tocar_som(self.m_seed)
            while y > 220:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_seed, x, y)
                pygame.display.update()
                y -= 7
                x += 480/11
            pygame.time.delay(1000)            

        def Smnt_Prst2():
            x, y = 600, 180
            self.Jogo.tocar_som(self.m_heal)
            while y < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_heal, x, y)
                pygame.display.update()
                y += 14
                x -= 360/11
            pygame.time.delay(1000) 
        
        def Cauda_Chcot():
            for z in range(4):
                x = 200
                while x < 350:
                    self.Jogo.imprimir_imagem(self.s_fundo)
                    self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                    self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                    self.fundo_basico()
                    pygame.display.update()
                    x += 60
                
                self.Jogo.tocar_som(self.m_quick_atack)

                while x > 200:
                    self.Jogo.imprimir_imagem(self.s_fundo)
                    self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], x, 290)
                    self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)

                    self.fundo_basico()
                    pygame.display.update()
                    x -= 60

        def Raio_Solar():
            y = 140
            self.Jogo.tocar_som(self.m_solar_beam)
            while y < 290:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_solar, 200, y)
                pygame.display.update()
                y += 10
            pygame.time.delay(1000)

        def Raio_Solar2():
            x, y = 200, 290
            self.Jogo.tocar_som(self.m_solar_beam)
            while y > 160:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_solar, x, y)
                pygame.display.update()
                y -= 10
                x += 400/11
            pygame.time.delay(1000)

        def Vinha_Chcot():
            x, y = 370, 190
            self.Jogo.tocar_som(self.m_vine_whip)
            while y < 290:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_vine, x, y)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                pygame.display.update()
                y += 10
                x += 10
            pygame.time.delay(1000)

        def Rugir():
            x, y = 250, 315
            self.Jogo.tocar_som(self.m_growl)
            while y > 0:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_growl, x, y)
                self.fundo_basico()
                pygame.display.update()
                y -= 18
                x += 540/11
            pygame.time.delay(1000)
        
        def Barreira():
            y = 510
            self.Jogo.tocar_som(self.m_barrier)
            while y > 290:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_barrier, 200, y)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.escrever_caixa_de_texto("Barreira!", self.Baixo, False)
                y -= 4
                pygame.display.update()

        def Confusao():
            x, y = 200, 150
            self.Jogo.tocar_som(self.m_solar_beam)
            while y < 450:
                self.Jogo.imprimir_imagem(self.s_confusion, x, y)
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.escrever_caixa_de_texto("Confusão!", self.Baixo, False)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                pygame.display.update()
                y += 7
                x += 28/3
        
        def Meditação():
            x, y = 600, 450
            self.Jogo.tocar_som(self.m_solar_beam)
            while y > 150:
                self.Jogo.imprimir_imagem(self.s_confusion, x, y)
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.escrever_caixa_de_texto("Meditação!", self.Baixo, False)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                pygame.display.update()
                y -= 7
                x -= 28/3            

        def Duplo_Tapa():
            x = 550
            self.Jogo.tocar_som(self.m_slap)
            while x < 650:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_slap, x, 180)
                pygame.display.update()
                x += 10

        def Raio_Psqc():
            xp, yp = 200, 290
            xc, yc = 200, 150
            self.Jogo.tocar_som(self.m_psybeam)
            while yp > 0:
                self.Jogo.imprimir_imagem(self.s_confusion, xc, yc)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_psybeam, xp, yp)
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.escrever_caixa_de_texto("Raio Psíquico!", self.Baixo, False)
                self.fundo_basico()
                pygame.display.update()
                yp -= 7
                xp += 280/11
                yc += 7
                xc += 28/3
            pygame.time.delay(1000)            
        
        def Absorver():
            self.Jogo.tocar_som(self.m_tackle)
            self.Jogo.imprimir_imagem(self.s_slam, 600, 180)
            pygame.display.update()
            pygame.time.delay(1000)

            x, y = 600, 180
            self.Jogo.tocar_som(self.m_heal)
            while y < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_heal, x, y)
                pygame.display.update()
                y += 10
                x -= 300/11
            pygame.time.delay(1000) 

        def Po_Venenoso():
            x, y = 200, 290
            self.Jogo.tocar_som(self.m_po)
            while y > 160:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_poison, x, y)
                pygame.display.update()
                y -= 5
                x += 190/11
            pygame.time.delay(1000)

        def Po_Venenoso2():
            self.Jogo.tocar_som(self.m_po)
            self.Jogo.imprimir_imagem(self.s_poison, 631, 165)
            pygame.display.update()
            pygame.time.delay(1000)

        def Po_de_Sono():
            x, y = 200, 290
            self.Jogo.tocar_som(self.m_po)
            while y > 160:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_sleep, x, y)
                pygame.display.update()
                y -= 5
                x += 190/11
            pygame.time.delay(1000)

        def Po_de_Sono2():
            x, y = 200, 290
            self.Jogo.tocar_som(self.m_sleeping)
            while y > 180:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_sleeping, x, y)
                pygame.display.update()
                x += 2.5
                y -= 2.5
            pygame.time.delay(1000)

        def Aroma_Doce():
            x, y = 200, 290
            self.Jogo.tocar_som(self.m_sweet)
            while y > 160:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_sweet, x, y)
                pygame.display.update()
                y -= 5
                x += 190/11
            pygame.time.delay(1000)            
        
        def Petalas():
            y = 140
            self.Jogo.tocar_som(self.m_petal)
            while y < 300:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_petal, 200, y)
                pygame.display.update()
                y += 8
            pygame.time.delay(1000)

            Derrubada()

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

    def ganhou(self):
        #Quando a vida do Pokemon Adversario chega a 0
        pygame.event.get()

        #Animacao do Pokemon subindo
        y = 180
        self.Jogo.tocar_som(self.m_faint)
        while y > -200:
            self.Jogo.imprimir_imagem(self.s_fundo)
            self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, 290)
            self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, y)
            y -= 3
            pygame.display.update()

        self.m_batalha.stop()
        self.Jogo.tocar_som(self.m_vitoria, -1)
        pygame.time.delay(1000)

        #Mensagem Final de Vitória
        self.Jogo.imprimir_imagem(self.s_texto)
        self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} derrotou", self.Cima)
        self.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']}!", self.Baixo)

        while True:
            self.Jogo.checar_eventos()

            if self.Jogo.ENTER:
                self.Jogo.tocar_som(self.m_selecionar)
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto(f"Parabéns {self.Pok_atq['nome']}!", self.Cima)
                self.Jogo.resetar_teclas()

                while True:
                    self.Jogo.checar_eventos()
                    if self.Jogo.ENTER:
                        self.Jogo.tocar_som(self.m_selecionar)
                        self.m_vitoria.stop()
                        self.Jogo.resetar_teclas()
                        break
                break

    def perdeu(self):
        #Para caso o Pokemon atacando perca (o que é meio dificil)
        pygame.event.get()

        #Animacao do Pokemon descendo
        y = 290
        self.Jogo.tocar_som(self.m_faint)
        while y < 510:
            self.Jogo.imprimir_imagem(self.s_fundo)
            self.Jogo.imprimir_imagem(self.Pok_alvo['sprite_frente'], 600, 180)
            self.Jogo.imprimir_imagem(self.Pok_atq['sprite_costas'], 200, y)
            self.Jogo.imprimir_imagem(self.s_texto)
            y += 3.8
            pygame.display.update()

        self.m_batalha.stop()
        self.Jogo.tocar_som(self.m_vitoria, -1)
        pygame.time.delay(1000)

        #Mensagem final de Vitória
        self.Jogo.imprimir_imagem(self.s_texto)
        self.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} derrotou", self.Cima)
        self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']}!", self.Baixo)

        while True:
            self.Jogo.resetar_teclas()
            self.Jogo.checar_eventos()

            if self.Jogo.ENTER:
                self.Jogo.tocar_som(self.m_selecionar)
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto(f"Parabéns {self.Pok_alvo['nome']}!", self.Cima)
                self.Jogo.resetar_teclas()

                while True:
                    self.Jogo.checar_eventos()
                    if self.Jogo.ENTER:
                        self.Jogo.tocar_som(self.m_selecionar)
                        self.m_vitoria.stop()
                        self.Jogo.resetar_teclas()
                        break
                break

    def entrada_da_batalha(self, Pok1, Pok2):
        #Definindo os Pokemons
        self.Pok1 = self.que_pokemon(Pok1)
        self.Pok2 = self.que_pokemon(Pok2)

        self.Pok1['vida'] = 50
        self.Pok2['vida'] = 50
        self.Pok1['vida_atual'] = 50
        self.Pok2['vida_atual'] = 50
        self.Pok1['falha_na_precisao'] = 0
        self.Pok2['falha_na_precisao'] = 0
        self.Pok1['falha_na_defesa'] = 1
        self.Pok2['falha_na_defesa'] = 1

        #1 dos 5 ataques é removido, para ter apenas 4
        self.Pok1['ataques'].remove(random.choice(self.Pok1['ataques']))
        self.Pok2['ataques'].remove(random.choice(self.Pok2['ataques']))

        self.Pok_atq = self.Pok1
        self.Pok_alvo = self.Pok2

        #Coordenadas y para escrever o texto na caixa de texto
        self.Cima, self.Baixo = 460, 510

        #Animação de Entrada
        pygame.time.delay(100)
        self.Jogo.tocar_som(self.m_batalha, -1)

        #Fundo Basico da Batalha
        self.Jogo.imprimir_imagem(self.s_fundo)
        self.Jogo.imprimir_imagem(self.s_texto)

        #Pokemon Adversario
        self.escrever_caixa_de_texto(f"{self.Pok2['nome']}", self.Cima)
        self.escrever_caixa_de_texto(f"entra em cena!", self.Baixo)
        y = -40
        while y < 180:

            self.Jogo.imprimir_imagem(self.s_fundo)
            self.Jogo.imprimir_imagem(self.Pok2['sprite_frente'], 600, y)
            y += 3
            pygame.display.update()

        pygame.time.delay(1000)

        #Pokemon Atacando
        self.Jogo.imprimir_imagem(self.s_texto)
        self.escrever_caixa_de_texto(f"Vai {self.Pok1['nome']}!", self.Cima)
        y = 510
        while y > 290:
            self.Jogo.imprimir_imagem(self.s_fundo)
            self.Jogo.imprimir_imagem(self.Pok2['sprite_frente'], 600, 180)

            self.Jogo.imprimir_imagem(self.Pok1['sprite_costas'], 200, y)
            self.Jogo.imprimir_imagem(self.s_texto)
            self.escrever_caixa_de_texto(f"Vai {self.Pok1['nome']}!", self.Cima, False)
            y -= 3.8
            pygame.display.update()

        pygame.time.delay(100)
        
        #Iniciando a Batalha
        self.fundo_da_batalha()



    def loop(self, Pok1, Pok2):
        #Introduz a Batalha
        self.entrada_da_batalha(Pok1, Pok2)

        #Variaveis importantes
        anima = False
        opcao = [1, 1]
        batalhando = True
        trocar_pokemons = False
        self.Pok1['solar_beam'] = False, 0
        self.Pok2['solar_beam'] = False, 0
        self.Pok1['Smnt. Prst.'], self.Pok1['Pó Venenoso'], self.Pok1['Pó de Sono'] = False, False, False
        self.Pok2['Smnt. Prst.'], self.Pok2['Pó Venenoso'], self.Pok2['Pó de Sono'] = False, False, False

        #Loop
        while batalhando:
            if anima: self.Jogo.conserta_enter_adiantado() #A função só é usada uma fez, atraves da variavel anima que se torna False depois da primeira passagem pelo loop
            self.Jogo.checar_eventos()

            #Controla o FPS
            self.clock.tick(60)

            #Troca os Turnos dos Pokemons
            if trocar_pokemons == True:
                if self.Pok_atq == self.Pok1:
                    self.Pok_atq = self.Pok2
                    self.Pok_alvo = self.Pok1
                else:
                    self.Pok_atq = self.Pok1
                    self.Pok_alvo = self.Pok2
                trocar_pokemons = False

            #Reseta ao estado fundamental da tela para se alguma alteracao for feita
            self.fundo_da_batalha(anima)

            #Verifica se o Pokemon acordou
            if self.Pok_atq['Pó de Sono'] == 'acordou':
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']}", self.Cima)
                self.escrever_caixa_de_texto("acordou!", self.Baixo)
                self.Pok_atq['Pó de Sono'] = 0
                pygame.time.delay(2000)

            #Verifica se o Pokemon está dormindo
            if self.Pok_atq['Pó de Sono'] > 0:
                self.animacoes("Pó de Sono2")
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']}", self.Cima)
                self.escrever_caixa_de_texto("está dormindo!", self.Baixo)
                self.Pok_atq['Pó de Sono'] -= 1
                if self.Pok_atq['Pó de Sono'] == 0:
                    self.Pok_atq['Pó de Sono'] = 'acordou'
                pygame.time.delay(2000)
                trocar_pokemons = True
                continue
            
            #Verifica se o Pokemon carregou Raio Solar
            if self.Pok_atq['solar_beam'][0] == True:
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} usou", self.Cima)
                self.escrever_caixa_de_texto("Raio Solar!", self.Baixo)
                self.animacoes("Raio Solar2")
                self.Pok_alvo['vida'] -= self.Pok_atq['solar_beam'][1]
                self.Pok_atq['solar_beam'] = False, 0
                self.atualizar_vida()
                pygame.time.delay(500)
                trocar_pokemons = True

                #Verifica se o Pokemon usou Semente Paratisa (tem que repetir aqui porque o codigo nao chega no final do loop)
                if self.Pok_atq['Smnt. Prst.'] == True:
                    self.Jogo.imprimir_imagem(self.s_texto)
                    self.animacoes("Smnt. Prst.2")
                    self.escrever_caixa_de_texto(f"A vida de {self.Pok_alvo['nome']}", self.Cima)
                    self.escrever_caixa_de_texto("foi sugada!", self.Baixo)
                    self.Pok_alvo['vida'] -= 3
                    self.Pok_atq['vida'] += 3
                    pygame.time.delay(500)

                if self.Pok_alvo['vida'] > 0:
                    continue

            #Selecao da Acao

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
                self.Jogo.tocar_som(self.m_selecionar)

            #Seleciona opcao atual
            if self.Jogo.ENTER and self.vidas_certas == True:
                self.Jogo.tocar_som(self.m_selecionar)
                self.Jogo.resetar_teclas()

                if opcao == [1, 1]: #LUTAR
                    menu_ataques = True

                    atq = [1, 1]
                    while menu_ataques:
                        self.Jogo.checar_eventos()

                        self.Jogo.imprimir_imagem(self.s_ataques)
                        self.escrever_ataques(self.Pok_atq)

                        atq_atual = atq.copy()
                        #Navega-se pelos ataques por uma lista com coordenadas x e y, que podem ser 1 ou 2 (Indica-se o PP o Tipo do ataque)
                        if atq == [1, 1]: atq_selecionado = 0
                        if atq == [1, 2]: atq_selecionado = 1
                        if atq == [2, 1]: atq_selecionado = 2
                        if atq == [2, 2]: atq_selecionado = 3

                        self.escrever_ataques(self.Pok_atq, atq_selecionado, self.Pok_atq['cor'])
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
                            self.Jogo.tocar_som(self.m_selecionar)


                        #Seleciona opcao atual
                        #Caso o PP seja 0
                        if self.Jogo.ENTER and self.Pok_atq['ataques'][atq_selecionado].PPatual <= 0:
                            self.Jogo.imprimir_imagem(self.s_texto)
                            self.escrever_caixa_de_texto('Não pode usar o ataque!', self.Cima)
                            pygame.time.delay(2000)
                            self.Jogo.conserta_enter_adiantado()
                            continue
                        
                        #Usa o Ataque
                        if self.Jogo.ENTER:
                            self.Jogo.tocar_som(self.m_selecionar)
                            self.Jogo.imprimir_imagem(self.s_texto)
                            
                            #Informa qual ataque foi usado
                            if self.Pok_atq['ataques'][atq_selecionado].Nome == "Smnt. Prst.": #"Smnt. Prst."" é escrito como "Semente Parasita"
                                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} usou", self.Cima)
                                self.escrever_caixa_de_texto("Semente Parasita!", self.Baixo)
                            elif self.Pok_atq['ataques'][atq_selecionado].Nome == "Pétalas": #"Pétalas"" é escrito como "Dança de Pétalas"
                                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} usou", self.Cima)
                                self.escrever_caixa_de_texto("Dança de Pétalas!", self.Baixo)                                                              
                            elif self.Pok_atq['ataques'][atq_selecionado].Nome != "Raio Solar":
                                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} usou", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Pok_atq['ataques'][atq_selecionado].Nome}!", self.Baixo)

                            #Diminui o PP do ataque em 1
                            self.Pok_atq['ataques'][atq_selecionado].PPatual -= 1

                            #Usa o Ataque Selecionado, com a precisão do pokemon atacando e a defesa do pokemon alvo
                            acertou, dano = self.Pok_atq['ataques'][atq_selecionado].usar(self.Pok_atq['falha_na_precisao'], self.Pok_alvo['falha_na_defesa'])
                            self.animacoes(self.Pok_atq['ataques'][atq_selecionado].Nome) if acertou != False and self.Pok_atq['ataques'][atq_selecionado].Nome != "Duplo Tapa" else None #A animacao de Duplo Tapa nao pode ser usada aqui, pois ela eh repetida varias vezes durante o ataque
                            pygame.event.get()

                            #Ataques que alteram os status
                            if acertou == 'Precisao_adv':
                                self.Pok_alvo['falha_na_precisao'] += 5
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto("A precisão de", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} caiu!", self.Baixo)
                                pygame.time.delay(1500)
                            
                            if acertou == 'Evasao_adv':
                                self.Pok_atq['falha_na_precisao'] -= 5
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto("A evasão de", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} caiu!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Defesa_adv':
                                self.Pok_alvo['falha_na_defesa'] += 0.1
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto("A defesa de", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} caiu!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Defesa_sua':
                                self.Pok_atq['falha_na_defesa'] -= 0.1
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto("A defesa de", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} subiu!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Ataque_seu':
                                self.Pok_alvo['falha_na_defesa'] += 0.1
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto("O ataque de", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} subiu!", self.Baixo)
                                pygame.time.delay(1500)

                            #Ataques Especiais com Efeito Extra
                            if acertou == 'Derrubada':
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.Pok_alvo['vida'] -= dano[0]
                                self.Pok_atq['vida'] -= dano[1]
                                self.escrever_caixa_de_texto("Parte do dano", self.Cima)
                                self.escrever_caixa_de_texto("rebateu!", self.Baixo)
                                pygame.time.delay(1000)

                            if acertou == 'Absorver':
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.Pok_alvo['vida'] -= dano[0]
                                self.Pok_atq['vida'] += dano[1]
                                self.escrever_caixa_de_texto(f"A vida de {self.Pok_alvo['nome']}", self.Cima)
                                self.escrever_caixa_de_texto("foi sugada!", self.Baixo)
                                pygame.time.delay(3000)

                            if acertou == 'Raio Solar':
                                self.Pok_atq['solar_beam'] = True, dano
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} carregou", self.Cima)
                                self.escrever_caixa_de_texto("o ataque!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Pó Venenoso':
                                self.Pok_atq['Pó Venenoso'] = True
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} foi", self.Cima)
                                self.escrever_caixa_de_texto("envenenado!", self.Baixo)
                                pygame.time.delay(1500)                             
                            
                            if acertou == "Pó de Sono":
                                self.Pok_alvo['Pó de Sono'] = dano
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} caiu", self.Cima)
                                self.escrever_caixa_de_texto("no sono!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Smnt. Prst.':
                                self.Pok_atq['Smnt. Prst.'] = True
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} foi", self.Cima)
                                self.escrever_caixa_de_texto("semeado!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Duplo Tapa':
                                for hit in range(len(dano)):
                                    self.animacoes("Duplo Tapa")
                                    self.Pok_alvo['vida'] -= dano[hit]
                                    self.atualizar_vida()
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"Acertou {len(dano)} vezes!", self.Cima)
                                pygame.time.delay(1500)  

                            pygame.event.get()

                            #Ataques Comuns que apenas Causam Dano
                            if acertou == True:
                                self.Pok_alvo['vida'] -= dano

                            #Errou o Ataque
                            elif acertou == False:
                                pygame.time.delay(1000)
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"{self.Pok_atq['nome']} errou", self.Cima)
                                self.escrever_caixa_de_texto("o ataque!", self.Baixo)
                                pygame.display.update()
                                pygame.time.delay(1500)
                            
                            #Mudança de Variaveis Importantes
                            pygame.time.delay(10)
                            Voltou_A_Opcoes = True
                            menu_ataques = False
                            trocar_pokemons = True
                            self.atualizar_vida()

                            #Checa ataques que agem em turnos infinitamente
                            if self.Pok_atq['Pó Venenoso'] == True:
                                self.Jogo.checar_eventos()
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"{self.Pok_alvo['nome']} é ferido", self.Cima)
                                self.escrever_caixa_de_texto("pelo veneno!", self.Baixo)
                                self.Pok_alvo['vida'] -= 6.25
                                self.animacoes("Pó Venenoso2")
                                pygame.time.delay(500)

                            if self.Pok_atq['Smnt. Prst.'] == True:
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.animacoes("Smnt. Prst.2")
                                self.escrever_caixa_de_texto(f"A vida de {self.Pok_alvo['nome']}", self.Cima)
                                self.escrever_caixa_de_texto("foi sugada!", self.Baixo)
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
                            self.Jogo.tocar_som(self.m_selecionar)
                            menu_ataques = False

                        self.Jogo.resetar_teclas()
                        pygame.display.update()

                if opcao == [1, 2]: #POKÉMON
                    #O jogo te da uma licao de fair play
                    self.Jogo.imprimir_imagem(self.s_texto)
                    self.escrever_caixa_de_texto('Acho que 2x1 seria', self.Cima)
                    self.escrever_caixa_de_texto('um pouco injusto, não?',self.Baixo)
                    pygame.time.delay(2000)
                    Voltou_A_Opcoes = True

                if opcao == [2, 1]: #BOLSA
                    #Abre a Bolsa
                    self.Jogo.imprimir_imagem(self.s_bolsa)
                    pygame.display.update()

                    menu_bolsa = True
                    while menu_bolsa:
                        self.Jogo.resetar_teclas()
                        self.Jogo.checar_eventos()

                        #Usa o Item Misterioso
                        if self.Jogo.ENTER:
                            self.Jogo.tocar_som(self.m_selecionar)

                            #Nada acontece caso ambos os pokemons nao estejam com vida "carmesim"
                            if self.Pok_atq['vida_atual'] > 10 or self.Pok_alvo['vida_atual'] > 10:
                                self.fundo_da_batalha(False); self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto('Você usa o', self.Cima)
                                self.escrever_caixa_de_texto('Item misterioso!', self.Baixo)
                                pygame.time.delay(2000)
                                pygame.event.get()

                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto('.', self.Cima); pygame.time.delay(500)
                                self.escrever_caixa_de_texto(' .', self.Cima); pygame.time.delay(500)
                                self.escrever_caixa_de_texto('  .', self.Cima); pygame.time.delay(500)
                                pygame.event.get()

                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto('Nada acontece!', self.Cima)
                                pygame.time.delay(1000)
                                menu_bolsa = False
                                Voltou_A_Opcoes = True

                            #Caso ambos os pokemons estejam com a vida "carmesim", inicia-se a batalha secreta contra o Missingno
                            elif self.Pok_atq['vida_atual'] <= 10 and self.Pok_alvo['vida_atual'] <= 10:
                                self.fundo_da_batalha(False); self.Jogo.imprimir_imagem(self.s_texto)
                        
                                self.escrever_caixa_de_texto('Você usa o ite-^าง6รบ}j', self.Cima)
                                self.Jogo.tocar_som(self.Missingno.m_bug1)
                                self.escrever_caixa_de_texto('สw+ส~L*เป6Pอย`าง7รบ}า!', self.Baixo)

                                self.m_batalha.stop()
                                self.Jogo.janela.fill((0,0,0))
                                pygame.display.update()
                                pygame.time.delay(2000)
    
                                self.Missingno.batalha(self.Pok_atq, self.Pok_alvo)

                        #So ha um item na bolsa, mas o efeito sonoro da a impressao de que poderia haver mais
                        if self.Jogo.cima or self.Jogo.baixo:
                            self.Jogo.tocar_som(self.m_selecionar)

                        #Fecha da Bolsa
                        if self.Jogo.ESC:
                            self.Jogo.tocar_som(self.m_selecionar)
                            menu_bolsa = False
                            Voltou_A_Opcoes = True

                if opcao == [2, 2]: #CORRER
                    #Não corra por favor :(
                    self.Jogo.imprimir_imagem(self.s_texto)
                    self.escrever_caixa_de_texto("Sério, você vai", self.Cima)
                    self.escrever_caixa_de_texto("simplesmente fugir?", self.Baixo)
                    correndo = True

                    while correndo:
                        self.Jogo.checar_eventos()

                        #Corre
                        if self.Jogo.ENTER:
                            self.Jogo.tocar_som(self.m_selecionar)
                            self.Jogo.imprimir_imagem(self.s_texto)
                            self.escrever_caixa_de_texto("Tá bom então", self.Cima, True, (212, 0, 0)) #O texto eh imprimido com cor vermelha
                            self.escrever_caixa_de_texto(">:((((((((((((((((((((((((((", self.Baixo, True, (212, 0, 0))
                            pygame.quit()
                            sys.exit()

                        #Volta ao menu das opcoes de acao
                        if self.Jogo.ESC:
                            self.Jogo.tocar_som(self.m_selecionar)
                            correndo = False
                            Voltou_A_Opcoes = True

            #Checa Vitória do Pokemon Atacando
            if self.Pok_alvo['vida_atual'] <= 0:
                self.ganhou()
                batalhando = False          
            
            #Checa Vitória do Pokemon Alvo
            if self.Pok_atq['vida_atual'] <= 0:
                self.perdeu()
                batalhando = False

            self.Jogo.resetar_teclas()

            #Realiza a animacao de escrever caso o jogador volte ao menu de opcoes de acao
            anima = True
            if Voltou_A_Opcoes: continue
            anima = False