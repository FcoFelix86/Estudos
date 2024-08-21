import random

# Resultados da Mega Sena nos últimos 5 anos (exemplo fictício)
resultados_5_anos = [
    [1, 5, 10, 20, 30, 40],
    [2, 15, 25, 30, 35, 45],
    # Adicione mais resultados aqui
]

def gerar_numero_sorteio(resultados_anteriores):
    numeros = list(range(1, 61))

    # Remover números já sorteados nos últimos resultados
    for resultado in resultados_anteriores:
        for numero in resultado:
            if numero in numeros:
                numeros.remove(numero)

    # Embaralhar e escolher 6 números
    numeros_sorteio = random.sample(numeros, 6)

    return sorted(numeros_sorteio)

# Gerar um novo número de sorteio
novo_sorteio = gerar_numero_sorteio(resultados_5_anos)

print("Possível resultado da Mega Sena baseado nos últimos 5 anos:")
print(novo_sorteio)