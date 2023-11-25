#Necessário importar a biblioteca random
import random

# Gerando 1000 alturas aleatórias entre 145 e 200 centímetros
alturas = [random.randint(145, 200) for _ in range(1000)]

# Valor da maior altura
maior_altura = max(alturas)

# Valor da menor altura
menor_altura = min(alturas)

# Média das alturas
media_alturas = sum(alturas) / len(alturas)

# Quantas pessoas têm altura inferior à média das alturas
abaixo_da_media = sum(altura < media_alturas for altura in alturas)

# Exibindo os resultados
print(f"Valor da maior altura: {maior_altura} cm")
print(f"Valor da menor altura: {menor_altura} cm")
print(f"Média das alturas: {media_alturas:.2f} cm")
print(f"Pessoas com altura abaixo da média: {abaixo_da_media}")
