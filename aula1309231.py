class Atendimento:
    def __init__(self, tipo, nome):
        self.tipo = tipo
        self.nome = nome

fila_normal = []
fila_preferencial = []

def adicionar_atendimento():
    tipo = input("Digite o tipo de atendimento (N para normal, P para preferencial): ").upper()
    nome = input("Digite o nome do cliente: ")
    
    if tipo == "N":
        atendimento = Atendimento("Normal", nome)
        fila_normal.append(atendimento)
    elif tipo == "P":
        atendimento = Atendimento("Preferencial", nome)
        fila_preferencial.append(atendimento)
    else:
        print("Tipo de atendimento inválido!")

def encerrar_atendimento():
    if fila_preferencial:
        atendimento = fila_preferencial.pop(0)
        print(f"Atendimento Preferencial encerrado para {atendimento.nome}")
    elif fila_normal:
        atendimento = fila_normal.pop(0)
        print(f"Atendimento Normal encerrado para {atendimento.nome}")
    else:
        print("Não há mais atendimentos para encerrar!")

def mostrar_filas():
    print("\nFila Preferencial:")
    for atendimento in fila_preferencial:
        print(f"{atendimento.tipo}: {atendimento.nome}")
    
    print("\nFila Normal:")
    for atendimento in fila_normal:
        print(f"{atendimento.tipo}: {atendimento.nome}")

while True:
    print("\nOpções:")
    print("1. Adicionar atendimento")
    print("2. Encerrar atendimento")
    print("3. Mostrar filas")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        adicionar_atendimento()
    elif opcao == "2":
        encerrar_atendimento()
    elif opcao == "3":
        mostrar_filas()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")