def contar_letras(palavra):
    # Cria um dicionário para armazenar as contagens de cada letra
    contagem_letras = {}

    # Percorre cada letra na palavra
    for letra in palavra:
        # Verifica se a letra já está no dicionário
        if letra in contagem_letras:
            # Se sim, incrementa a contagem
            contagem_letras[letra] += 1
        else:
            # Se não, adiciona a letra ao dicionário com contagem 1
            contagem_letras[letra] = 1

    # Imprime o resultado
    for letra, contagem in contagem_letras.items():
        print(f"A letra '{letra}' aparece {contagem} vez(es) na palavra.")

    # Calcula o total de letras na palavra
    total_letras = len(palavra)
    print(f"Total de letras na palavra: {total_letras}")

if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    contar_letras(palavra)