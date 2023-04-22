

class Inventorio():
    def __init__(self, tamanho_maximo):
        self.__lista = [ ]
        self.__tamanho_maximo = tamanho_maximo
    def addItem(self, item):
        self.__lista.append(item)
    def removeItem(self, item):
        self.__lista.remove(item)
    def getItem(self)->list:
        return self.__lista
