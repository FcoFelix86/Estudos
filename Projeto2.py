# Inicialize listas vazias para armazenar as alturas
alturas = []

''' Coleta de alturas de 1.000 pessoas - Alterar para uma quantidade menor no Range, para validação
de testes'''

for i in range(1000):
    altura = float(input(f"Informe a altura da pessoa {i+1} (em centímetros): "))
    alturas.append(altura)

# Calcula a maior altura, a menor altura e a média das alturas
maior_altura = max(alturas)
menor_altura = min(alturas)
media_alturas = sum(alturas) / len(alturas)

# Conta quantas pessoas têm altura inferior à média das alturas
pessoas_inferior_media = sum(altura < media_alturas for altura in alturas)

# Exibe os resultados
print(f"Maior altura: {maior_altura} centímetros")
print(f"Menor altura: {menor_altura} centímetros")
print(f"Média das alturas: {media_alturas:.2f} centímetros")
print(f"Pessoas com altura inferior à média: {pessoas_inferior_media}")