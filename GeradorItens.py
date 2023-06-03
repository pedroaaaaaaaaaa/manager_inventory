import random

from Alabarda import *
from Armadura import *
from Espada import *

class GeradorItens():
    def __init__(self):
        self.pool_espadas = ["espada longa", "claymore", "zheiwander"]
        self.pool_armaduras = ["cota de malha", "armadura de couro", "armadura de aço"]
        self.raridades = ["comum", "raro", "epico", "lendário"]


        #todo
        self.pool_alabardas = []


    def gerarEspada(self) -> Espada:
        preco = random.randint(50, 200)
        dano = random.randint(5,50)
        espada_escolhida = self.pool_espadas[random.randint(0, len(self.pool_espadas) -1)]
        raridade_escolhida = self.raridades[random.randint(0, len(self.raridades) -1)]
        duplo_fio = True
        if dano%5 == 0:
            duplo_fio = False

        new_sword = Espada(espada_escolhida, preco, raridade_escolhida, dano, duplo_fio)
        return new_sword

    #todo
    def gerarAlabarda(self) -> Alabarda:
        pass

    def gerarArmadura(self) -> Armadura:
        armadura_escolhida = self.pool_armaduras[random.randint(0, len(self.pool_armaduras) -1)]
        preco = random.randint(50, 1000)
        raridade_escolhida = self.raridades[random.randint(0, len(self.raridades) -1)]
        defesa = random.randint(5,40)

        new_armor = Armadura(armadura_escolhida, preco, raridade_escolhida, defesa)
        return new_armor


