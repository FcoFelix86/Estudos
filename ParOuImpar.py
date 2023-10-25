def par_impar(numero):
    
    if numero % 2 == 0:
        return True
    else:
        return False

numero = int(input("Digite um número: "))
resultado = par_impar(numero)

if resultado:
    print(f"{numero} é um numero par.")
else:
    print(f"{numero} é um numero impar.")