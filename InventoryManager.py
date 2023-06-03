from Armadura import *
from inventorio import *
from GeradorItens import *
from usuario import *
from Loja import *

class InventoryManager:
    def __init__(self):
        self.usuario = Usuario("Player1", 0)
        self.gerador = GeradorItens()
        self.rodando = True
        self.loja = Loja()


        for i in range(100):
            espada = self.gerador.gerarEspada()
            self.loja.receberDoacao(espada)

        for i in range(100):
            armadura = self.gerador.gerarArmadura()
            self.loja.receberDoacao(armadura)

        #To do: Gerar alabardas e colocar na loja



    def run(self):
        while self.rodando:
            myinput = int(input('''Bem vindo ao seu manager de inventório
            1: Ver meus itens
            2: Ver itens loja
            3: Comprar itens
            4: Vender itens
            '''))



            #Questão: Os itens são printados a partir de seus atributos fornecidos
            #Porém, como poderiamos criar uma forma sistemática de imprimirmos atributos não genéricos,
            #como dano de armas ou defesa de armaduras?

            #Questão 2: Faz sentido exibirmos ao jogador o index de seus itens? Ou isso deveria
            #ser uma questão interna do sistema
            if myinput == 1:
                user_inv = self.usuario.getInventario()
                itens = user_inv.getItens()
                index = 0
                if len(itens) == 0:
                    print("Você ainda não possui itens")
                else:
                    for item in itens:
                        atributos = item.getATB()
                        print("""
                        Index - {}
                        Nome - {}
                        Preço - {}
                        Raridade {}   
                        """.format(index, atributos[0], atributos[1], atributos[2]))
                        index += 1

            if myinput == 2:
                itens = self.loja.exibirItens()
                index = 0
                for item in itens:
                    atributos = item.getATB()
                    print("""
                    Index - {}
                    Nome - {}
                    Preço - {}
                    Raridade - {}   
                    """.format(index, atributos[0], atributos[1], atributos[2]))
                    index += 1



            #Aqui pedimos o index ao usuário. Será que não há uma forma mais legal de comprar um item?
            if myinput == 3:
                index_item = int(input("Insira o index do item que você deseja comprar"))
                preco_item = self.loja.getPrecoItem(index_item)
                dinheiro_usuario = self.usuario.checkCash()
                if preco_item > dinheiro_usuario:
                    print("Você não possui dinheiro para efetuar a transação")

                else:
                    item = self.loja.VenderItem(index_item)
                    self.usuario.comprarItens(item)


            #To do
            if myinput == 4:
                pass






inv = InventoryManager()
inv.run()



