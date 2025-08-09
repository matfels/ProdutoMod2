from classes.Produto import Produto
from classes.Categoria import Categoria



#Categoria.listarTodos()



produto1 = Produto('001','Carro', 50, 1300)
produto1.inserir()

categoria = Categoria("Veiculo")
categoria.inserir()
print(categoria.detalhar())

produto1.listarTodos()
categoria.listarTodos()

