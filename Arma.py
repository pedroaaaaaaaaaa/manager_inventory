from Item import Item



class Arma(Item):
    def __init__(self, nomeItem, preco, raridade,dano):
        self.__nome = nomeItem
        self.__preco = preco
        self.__raridade = raridade
        self.__dano = dano

    def getATB(self):
        return (self.__nome,self.__preco,self.__raridade, self.__dano)

