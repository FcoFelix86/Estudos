# Função para adicionar um item à lista de compras
def adicionar_item(lista_compras):
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade a ser comprada: "))
    lista_compras[produto] = quantidade
    print(f"{quantidade} {produto}(s) foram adicionados à lista de compras.")

# Função para remover um item da lista de compras
def remover_item(lista_compras):
    produto = input("Digite o nome do produto que deseja remover: ")
    if produto in lista_compras:
        del lista_compras[produto]
        print(f"{produto} foi removido da lista de compras.")
    else:
        print(f"{produto} não foi encontrado na lista de compras.")

# Função para exibir a lista de compras completa
def exibir_lista(lista_compras):
    print("\nLista de Compras:")
    for produto, quantidade in lista_compras.items():
        print(f"{produto}: {quantidade}")

# Função principal
def main():
    lista_compras = {}

    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Item")
        print("2. Remover Item")
        print("3. Exibir Lista de Compras")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            adicionar_item(lista_compras)
        elif escolha == '2':
            remover_item(lista_compras)
        elif escolha == '3':
            exibir_lista(lista_compras)
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()