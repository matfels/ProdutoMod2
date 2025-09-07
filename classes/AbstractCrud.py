import json
from abc import ABC

#Classe pai, urilizada pelas classes filhas.
class AbstractCrud(ABC):
    
#imprime tudo o que esta dentro do self utilizando o "__dict__".
    def detalhar(self):
        return self.__dict__    
        
#Chama o metodo "Consultar()" e recebe os dados do JSON em formato de lista, logo apos realiza um append(self.detalhar()) para dentro da lista com os dados do jason, e por ultimo chama o metodo (__gravarArquivo)
# para gravar dentro do arquivo JSON.
    def inserir(self):
        texto = "inserido"
        lista = self.consultar()        
        
        lista.append(self.detalhar())   
        
        self.__gravarArquivo(lista, texto)


#Chama o metodo "Consultar()" e recebe os dados do JSON em formato de lista, utiliza a variavel "item" para localizar o item expecifico na lista e exclui o mesmo.
    @classmethod
    def excluir(self, item = None):
        lista = self.consultar()   
        lista.remove(lista[item])

        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)  #pega os dados da variável lista e os converte para a sintaxe JSON. 
        print(f'Registro excluído com sucesso')


#Chama o metodo "Consultar()" e recebe os dados do JSON em formato de lista, utiliza a variavel "item" para localizar o item expecifico na lista que recebera o "self.detalhar()",
# então chama a o metodo (__.gravarArquivo) para gravar dentro do arquivo JSON.
    def alterar(self, item): 
        
        texto = "alterado"
        
        lista = self.consultar()        
        lista[item] = self.detalhar()
        self.__gravarArquivo(lista, texto)
        
        
#Recebe uma lista com os dados que devem ser inserido no arquivo JSON, apos isso abre o arquivo, escreve no arquivo e logo apos imprime se foi registrado com sucesso.
    def __gravarArquivo(self, lista, texto):        
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)  #pega os dados da variável lista e os converte para a sintaxe JSON. 
        print(f'Registro {texto} com sucesso')


#Usa o metodo consultar para trazer os dados do arquivo json, logo apos é utilizado um for e um enumerate para imprimir listando cada atributo do arquivo.
    @classmethod
    def listarTodos(cls): 
        lista = cls.consultar()

        for i, p in enumerate(lista):
            print(f"{i} - {p}")


#Abre um arquivo json e retorna ele em formato de lista, se for adicionado um indice ele retorna um indice específico de dentro do json.
    @classmethod
    def consultar(cls, item = None):  
        try:
            with open(cls.arquivo) as file:
                lista = json.load(file) #lê o conteudo do arquivo que foi pasasdo "file" e converte o JSON em uma estrutura de dados Python.
                return lista[item] if isinstance(item, int) else lista #If ternario
        
        except Exception: #Caso não encontre o arquivo ele retorna uma lista vazia!
            return []           
  

