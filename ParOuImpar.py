def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

entrada = input("Digite um número inteiro: ")

if entrada.isdigit():
    numero = int(entrada)
    resultado = verificar_par_impar(numero)
    print(resultado)
else:
    print("Por favor, insira um número inteiro válido.")