# Solicitar ao usuário o número para o qual deseja gerar a tabuada
numero = int(input("Digite um número para gerar a tabuada: "))

# Loop de 1 a 10 para gerar a tabuada
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")