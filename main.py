
print("=====PERFIL======")

nome = input("Nome: ")
idade = input("Idade: ")
cidade = input("Cidade: ")
profisao = input("Profissao: ")
print("Olá, bem vindo ao sistema de gestao")

print("1 - Cadastrar Clientes")
print("2 - Listar Clientes")
print("3 - Buscar Clientes")
print("4 - Excluir Clientes")
print("5 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("Cadastrar Clientes")

elif opcao == "2":
    print("cliente 1,", "cliente 2,", "cliente 3,", "cliente 4")

elif opcao == "3":
    print("Pesquisar cliente:")

elif opcao == "4":
    print("Excluir cliente:")

elif opcao == "5":
    print("Saindo...")

else:
    print("Opcao invalida!")


