# Crie uma lista para armazenar os valores
valores = []

# Use um loop para pedir ao usuário que insira os valores
num_valores = int(input("Quantos valores você deseja inserir? "))
for i in range(num_valores):
    valor = float(input(f"Insira o valor {i + 1}: "))
    valores.append(valor)

# Calcule a média dos valores
soma = sum(valores)
media = soma / len(valores)

# Mostre a média
print(f"A média dos valores inseridos é: {media}")