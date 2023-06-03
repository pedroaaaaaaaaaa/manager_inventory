from Arma import *

class Alabarda(Arma):
    def __init__(self,nome,preco,raridade,dano,material_cabo):
        super().__init__(nome,preco,raridade,dano)
        self.material_cabo = material_cabo

    def getATB(self):
        '''
        Retorna todos atributos desta arma
        :return:
        self.__nome,self.__preco,self.__raridade, self.__dano e material do cabo
        '''
        return (self.__nome,self.__preco,self.__raridade, self.__dano, self.material_cabo)
