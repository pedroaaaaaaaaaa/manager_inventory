from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, nomeItem, preco, raridade):
        self.__nome = nomeItem
        self.__preco = preco
        self.__raridade = raridade



    def getATB(self):
        return (self.__nome, self.__preco, self.__raridade)





