import json
from abc import ABC

class AbstractCrud(ABC):
    
    def detalhar(self):
        return self.__dict__    
        
    def inserir(self):
        texto = "inserido"
        lista = self.consultar()        
        
        lista.append(self.detalhar())   
        
        self.__gravarArquivo(lista, texto)

    @classmethod
    def excluir(self, item = None):
        lista = self.consultar()   
        lista.remove(lista[item])

        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)  #pega os dados da variável lista e os converte para a sintaxe JSON. 
        print(f'Registro excluído com sucesso')



    def alterar(self, item):
        
        texto = "alterado"
        
        lista = self.consultar()        
        lista[item] = self.detalhar()
        self.__gravarArquivo(lista, texto)
        

    def __gravarArquivo(self, lista, texto):      
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)  #pega os dados da variável lista e os converte para a sintaxe JSON. 
        print(f'Registro {texto} com sucesso')

    @classmethod
    def listarTodos(cls):
        lista = cls.consultar()

        for i, p in enumerate(lista):
            print(f"{i} - {p}")


    @classmethod
    def consultar(cls, item = None):
        try:
            with open(cls.arquivo) as file:
                lista = json.load(file) #lê o conteudo do arquivo que foi pasasdo "file" e converte o JSON em uma estrutura de dados Python.
                return lista[item] if isinstance(item, int) else lista #If ternario

#                if isinstance(item, int):
#                    return lista[item]
#                else:
#                    return lista


        except Exception:
            return []           
  

