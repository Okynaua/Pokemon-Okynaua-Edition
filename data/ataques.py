import random

class ataque():
    def __init__(self, Nome, Tipo, Poder, Precisao, PPatual, PP):
        #Propriedades do ataque
        self.Nome = Nome
        self.Tipo = Tipo
        self.Poder = Poder
        self.Precisao = Precisao
        self.PP = PP
        self.PPatual = PPatual

    def usar(self, falha_na_precisao, falha_na_defesa):
        #Checa se o Pokémon acerta o ataque
        acertou = random.choices([True, False], weights = [self.Precisao - falha_na_precisao, 100 - (self.Precisao - falha_na_precisao)])[0]
        if acertou == False: return False, 0

        #Calculo do dano basico (apenas se o Poder tiver valor numerico)
        if self.Poder != None:
            dano = (0.208 * self.Poder + 2) * random.uniform(0.85, 1) * falha_na_defesa


        #Ataques que alteram os status dos Pokémons, ou agem por mais de um turno
        if self.Poder == None:
            if self.Nome == 'Atq. Areia' or self.Nome == 'Onda Trovão' or self.Nome == 'Time Duplo':
                return 'Precisao_adv', 0
            if self.Nome == 'Aroma Doce':
                return 'Evasao_adv', 0
            if self.Nome == 'Cauda Chcot.':
                return 'Defesa_adv', 0
            if self.Nome == 'Barreira':
                return 'Defesa_sua', 0
            if self.Nome == 'Rugir' or self.Nome == 'Meditação':
                return 'Ataque_seu', 0
            if self.Nome == 'Smnt. Prst.':
                return 'Smnt. Prst.', 0
            if self.Nome == 'Pó Venenoso':
                return 'Pó Venenoso', 0
            if self.Nome == "Pó de Sono":
                turnos = random.randrange(1, 3)
                return "Pó de Sono", turnos

        #Ataques (que causam dano) com Efeito Extra
        if self.Nome == 'Derrubada':
            dano = dano, 1/4 * dano
            return 'Derrubada', dano

        if self.Nome == 'Raio Solar':
            return 'Raio Solar', dano

        if self.Nome == 'Duplo Tapa':
            danos = []
            hits = random.randrange(2, 6)
            for hit in range(hits):
                dano = (0.208 * self.Poder + 2) * random.uniform(0.85, 1) * falha_na_defesa
                danos.append(dano)
            return 'Duplo Tapa', danos

        if self.Nome == 'Absorver':
            dano = dano, 1/2 * dano
            return 'Absorver', dano

        #MISSINGNO
        if self.Nome == 'Error':
            dano = 4/3*dano, 2/3*dano
            return 'Error', dano
        if self.Nome == 'Chaos':
            return 'Chaos', dano
        if self.Nome == 'Denial':
            return 'Denial', 0

        #Ataques sem Efeito Extra
        return True, dano