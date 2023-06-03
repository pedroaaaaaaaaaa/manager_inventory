from inventorio import *

class Usuario():
    def __init__(self, nome, nivel = 0):
        self.__codigo = "77777"
        self.__dinheiro = 500
        self.__inventorio = Inventorio(50)
        self.__nivel = nivel
        self.__nome = nome


    def checkCash(self):
        return self.__dinheiro

    def getInventario(self):
        return self.__inventorio

    def comprarItens(self, item):
        self.__dinheiro  = self.__dinheiro - item.getATB()[1]
        self.__inventorio.addItem(item)

    def venderItens(self, preço, item):
        self.__dinheiro = self.__dinheiro + preço
        self.__inventorio.removeItem(item)




