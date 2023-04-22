from inventorio import *

class Usuario():
    def __init__(self, nome, nivel = 0):
        self.__codigo = "77777"
        self.__dinheiro = 0
        self.__inventorio = Inventorio(50)
        self.__nivel = nivel
        self.__nome = nome

    def verInventario(self):

        itens = self.__inventorio.getItem()
        for x in range(len(itens)):
            print(itens[x])
    def comprarItens(self, preço, item):
        if self.__dinheiro < preço:
            return
        self.__dinheiro  = self.__dinheiro - preço
        self.__inventorio.addItem(item)
    def venderItens(self, preço, item):
        self.__dinheiro = self.__dinheiro + preço
        self.__inventorio.removeItem(item)




