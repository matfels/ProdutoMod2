import json

class AbstractCrud:
    
    def detalhar(self):
        return self.__dict__    
        
    def inserir(self):
        lista = self.consultar()        
        
        lista.append(self.detalhar())
        
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)  #pega os dados da variável lista e os converte para a sintaxe JSON. 
        
        print('Registro cadastrado com sucesso')    


    def listarTodos(self):
        lista = self.consultar()

        for i, p in enumerate(lista):
            print(f"{i} - {p}")


    def consultar(self):
        try:
            with open(self.arquivo) as file:
                return json.load(file) #lê o conteudo do arquivo que foi pasasdo "file" e converte o JSON em uma estrutura de dados Python.
        except Exception:
            return []           
  

