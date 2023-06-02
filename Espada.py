from Arma import *

class Espada(Arma):
    def __init__(self,nome,preco,raridade,dano,duplo_fio: bool):
        super().__init__(nome,preco,raridade,dano)
        self.duplo_fio = duplo_fio

    def getATB(self):
        '''
        Retorna todos atributos desta arma. Duplo fio indica se possui ou não
        :return:
        self.__nome,self.__preco,self.__raridade, self.__dano e duplo_fio
        '''
        return (self.__nome,self.__preco,self.__raridade, self.__dano, self.duplo_fio)