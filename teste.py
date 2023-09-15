# Inicialize a lista com as opções "Abertura", "Atendido" e "Encerrado"
opcoes = ["Abertura", "Atendido", "Encerrado"]

# Crie um loop para interagir com o usuário
while True:
    print("\nOpções disponíveis:")
    for i, opcao in enumerate(opcoes):
        print(f"{i + 1}. {opcao}")

    escolha = input("Escolha uma opção (ou 'q' para sair): ")

    if escolha == 'q':
        break

    # Verifique se a escolha é válida
    try:
        escolha = int(escolha)
        if escolha < 1 or escolha > len(opcoes):
            print("Opção inválida. Tente novamente.")
            continue
    except ValueError:
        print("Entrada inválida. Digite um número válido ou 'q' para sair.")
        continue

    opcao_selecionada = opcoes[escolha - 1]

    # Se a opção selecionada for "Encerrado", remova um item dessa opção
    if opcao_selecionada == "Encerrado":
        if len(opcoes) > 3:
            print("Item removido da opção 'Encerrado'.")
            opcoes.remove(opcao_selecionada)
        else:
            print("Não é possível remover mais itens da opção 'Encerrado'.")
    else:
        # Se a opção não for "Encerrado", peça ao usuário para escolher entre "Preferencial" e "Normal"
        tipo_atendimento = input("Escolha o tipo de atendimento (Preferencial/Normal): ")
        if tipo_atendimento.lower() == "preferencial" or tipo_atendimento.lower() == "normal":
            opcoes.append(f"{tipo_atendimento} - {opcao_selecionada}")
            print(f"Item adicionado à lista: {tipo_atendimento} - {opcao_selecionada}")
        else:
            print("Tipo de atendimento inválido. Tente novamente.")

print("Programa encerrado.")