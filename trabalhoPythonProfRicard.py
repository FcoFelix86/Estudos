# Função para criar uma nova lista vazia
def criar_lista():
    return []

# Função para adicionar um elemento à lista
def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    print(f"'{elemento}' foi adicionado à lista.")

# Função para remover elementos "Encerrado" da lista
def remover_encerrados(lista):
    lista = [item for item in lista if item != "Encerrado"]
    print("Elementos 'Encerrado' foram removidos da lista.")

# Função para exibir a lista atual
def exibir_lista(lista):
    print("Lista atual:")
    for item in lista:
        print(item)

# Função principal
def main():
    lista = criar_lista()
    
    while True:
        print("\nOpções:")
        print("1. Adicionar elemento")
        print("2. Remover elementos 'Encerrado'")
        print("3. Exibir lista")
        print("4. Sair")
        
        escolha = input("Escolha uma opção (1/2/3/4): ")
        
        if escolha == "1":
            elemento = input("Digite o elemento a ser adicionado (Abertura/Atendido/Preferencial/Normal): ")
            if elemento in ["Abertura", "Atendido", "Preferencial", "Normal"]:
                adicionar_elemento(lista, elemento)
            else:
                print("Opção inválida. Use uma das opções válidas.")
        elif escolha == "2":
            remover_encerrados(lista)
        elif escolha == "3":
            exibir_lista(lista)
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()