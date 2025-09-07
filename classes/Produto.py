from classes.AbstractCrud import AbstractCrud

class Produto(AbstractCrud):

    arquivo = 'db/produtos.json'

    def __init__(self, codigo, nome, quantidade = 0, valor = 0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        
        
    def inserir(self):
        lista = self.consultar()
        print(lista)
        produtorDuplicado = filter(lambda p: p['codigo'] == self.codigo, lista)
        
        if len(list(produtorDuplicado)):
            print()
            print("Já existe um produto com esse código")
        else:
            super().inserir()
