from Item import Item


class Armadura(Item):
    def __init__(self, nomeItem, preco, raridade, defesa):
        self.__defesa = defesa
        self.__nome = nomeItem
        self.__preco = preco
        self.__raridade = raridade
        self.__item = Item()

    def getATB(self):
        return self.__nome, self.__preco, self.__raridade, self.__defesa

