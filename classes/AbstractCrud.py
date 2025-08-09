import json
from abc import ABC

class AbstractCrud(ABC):
    
    def detalhar(self):
        return self.__dict__    
        
    def inserir(self):
        lista = self.consultar()        
        
        lista.append(self.detalhar())   
        
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)  #pega os dados da variável lista e os converte para a sintaxe JSON. 
        
        print('Registro cadastrado com sucesso')    


    @classmethod
    def listarTodos(cls):
        lista = cls.consultar()

        for i, p in enumerate(lista):
            print(f"{i} - {p}")


    @classmethod
    def consultar(cls):
        try:
            with open(cls.arquivo) as file:
                return json.load(file) #lê o conteudo do arquivo que foi pasasdo "file" e converte o JSON em uma estrutura de dados Python.
        except Exception:
            return []           
  

