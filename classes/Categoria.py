class Categoria:
    def __init__(self, nome):
        self.nome = nome 
        
    def detalhar(self):
        return self.__dict__     