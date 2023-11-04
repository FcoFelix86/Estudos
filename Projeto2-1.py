# Inicialize as variáveis para a maior altura, menor altura e soma das alturas
maior_altura = 0
menor_altura = float('inf')  # inicializa com um valor infinitamente grande
soma_alturas = 0

# Número de pessoas na pesquisa
numero_pessoas = 10

# Coleta das alturas e cálculo da soma das alturas
for i in range(numero_pessoas):
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    soma_alturas += altura
    
    # Atualiza a maior altura, se necessário
    if altura > maior_altura:
        maior_altura = altura
    
    # Atualiza a menor altura, se necessário
    if altura < menor_altura:
        menor_altura = altura

# Calcula a média das alturas
media_alturas = soma_alturas / numero_pessoas

# Conta quantas pessoas têm altura inferior à média das alturas
pessoas_inferiores_media = 0
for i in range(numero_pessoas):
    altura = float(input(f"Digite a altura da pessoa {i+1} (em metros): "))
    if altura < media_alturas:
        pessoas_inferiores_media += 1

# Exibe os resultados
print(f"A maior altura é: {maior_altura} metros")
print(f"A menor altura é: {menor_altura} metros")
print(f"A média das alturas é: {media_alturas:.2f} metros")
print(f"{pessoas_inferiores_media} pessoas têm altura inferior à média das alturas.")