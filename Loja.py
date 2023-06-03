from inventorio import *



class Loja:
    def __init__(self):
        self.__inventario = Inventorio(100000)
        self.__caixa = 0

        #algumas coisas legais poderiam ser feitas aqui. Poderiamos fazer um
        #sistema de buscas de itens, e abordariamos algumas estrategias de buscas bem interessas
        #Mas o escopo disso é provavelmente bem complexo, então podemos
        #manter assim por ora e posteriormente avaliamos se é interessante fazer isso
        self.__slots_armas = []
        self.__slot_armaduras = []

    def getSize(self):
        return self.__inventario.get_size()
    def exibirItens(self) -> []:
        lista_itens = self.__inventario.getItens()
        return lista_itens

    def exibirArmas(self) -> []:
        return self.__slots_armas

    def exibirArmaduras(self) -> []:
        return self.__slot_armaduras

    #Isso aq precisa ser melhorado, getATB()[1] não é uma forma legal de pegar o preço do item
    def VenderItem(self, indexItemComprar):
        item = self.__inventario.get_item_by_index(indexItemComprar)
        self.__caixa += item.getATB()[1]
        self.__inventario.removeItem(item)
        return item

    #loja pode ficar em débito pelas nossas regras, ent tanto faz se n tiver dinheiro
    def comprarItem(self, item):
        self.__caixa -= item.getATB()[1]
        self.__inventario.addItem(item)

    def receberDoacao(self, item):
        self.__inventario.addItem(item)

    def getPrecoItem(self, indexItem) -> int:
        item = self.__inventario.get_item_by_index(indexItem)
        return item.getATB()[1]

