def multiplo_de_2(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Exemplos de uso:
numero = int(input("Digite um número: "))
resultado = multiplo_de_2(numero)

if resultado:
    print(f"{numero} é um múltiplo de 2.")
else:
    print(f"{numero} não é um múltiplo de 2.")
