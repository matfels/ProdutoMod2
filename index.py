from classes.Produto import Produto
from classes.Categoria import Categoria


def menu():
    print()
    print("Digite uma alternativa: ")
    print("1 - Listra Produtos")
    print("2 - Inserir Produtos")
    print("3 - Alterar Produtos")
    print("4 - Excluir Produtos")
    print("0 - Sair")

opcao = 1    
    
while opcao != 0:
    menu()
    opcao = int(input("Digite um valor: "))
    match opcao:
        case 1:
            print("=====================================================================================")
            Produto.listarTodos()
            print("=====================================================================================")

        case 2: 
            codigo     = int(input("Digite o numero do codigo: "))
            nome       = str(input("Digite o nome do produto: "))
            quantidade = int(input("Digite a quantidade de produto: "))
            valor      = float(input("Digite o valor do produto: "))
            
            produto = Produto(codigo, nome, quantidade, valor)
            
            confirmacao = input("Tem certeza que deseja adicionar esse produto? (y) para sim (n) para não. Digite (y/n): ")
            if confirmacao == "y":
                produto.detalhar()
                print()
                
                print("=====================================================================================")
                produto.inserir()
                print("=====================================================================================")

            else:
                print()
                print("=====================================================================================")
                print("Produto Cancelado")
                print("=====================================================================================")

        case 3:
            ...
        case 4:
            ...
    
    


