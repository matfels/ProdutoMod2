from classes.Produto import Produto
from classes.Categoria import Categoria



produto1 = Produto('00223','celular', 50, 5000)
produto1.inserir()

categoria = Categoria("Eletronico")
categoria.inserir()
print(categoria.detalhar())

produto1.listarTodos()
categoria.listarTodos()