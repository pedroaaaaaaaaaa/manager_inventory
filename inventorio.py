

class Inventorio():
    def __init__(self, tamanho_maximo):
        self.__lista = [ ]
        self.__tamanho_maximo = tamanho_maximo
    def addItem(self, item):
        self.__lista.append(item)
    def removeItem(self, item):
        self.__lista.remove(item)
    def getItens(self)->list:
        return self.__lista
    def get_size(self) -> int:
        return self.__tamanho_maximo
    def get_item_by_index(self, index):
        return self.__lista[index]