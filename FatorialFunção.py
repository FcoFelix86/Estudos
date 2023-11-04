'''def pesquisa (L,n):
    for i, x in enumerate(L):
        if x == n:
            return i
    return None

lista = [12,12,34,54]
print(pesquisa(lista, 12))
print(pesquisa(lista, 50))'''

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else: 
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial
numero = int(input("Digite um numero para calcular o fatorial: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")

