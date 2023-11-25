# Inicializando variáveis
numero_pessoas = 10
alturas = []
soma_alturas = 0

# Coleta das alturas
for i in range(numero_pessoas):
    altura = float(input(f"Informe a altura da pessoa {i + 1} (em metros): "))
    alturas.append(altura)
    soma_alturas += altura

# Calculando a maior altura, menor altura e média das alturas
maior_altura = max(alturas)
menor_altura = min(alturas)
media_alturas = soma_alturas / numero_pessoas

# Contando quantas pessoas têm altura inferior à média das alturas
abaixo_media = sum(altura < media_alturas for altura in alturas)

# Exibindo os resultados
print(f"Maior altura: {maior_altura} metros")
print(f"Menor altura: {menor_altura} metros")
print(f"Média das alturas: {media_alturas} metros")
print(f"Pessoas com altura abaixo da média: {abaixo_media}")