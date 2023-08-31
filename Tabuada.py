print()
print('Gerador de tabuada')
print()
option = input('+ - * /: ')
print()
tabuada = int(input('Tabuada de '))
print()
valor = int(input('Até que número quer gerar a tabuada? '))
print()

if option == '+':
    for n in range(1, valor + 1):
        resultado = tabuada + n
print(f'{tabuada} + {n} = {resultado}')

if option == '-':
    resultado = 0
inicio = int(input(f'Repita o número {tabuada} para iniciar a tabuada: '))
print()
for n in range(inicio, valor-1):
    resultado = n - tabuada
print(f'{n} - {tabuada} = {resultado}')

if option == '*':
    for n in range(1, valor * 1):
        resultado = tabuada * n
print(f'{tabuada} x {n} = {resultado}')

if option == '/':
    resultado = 0
passo = int(input(f'Digite o número {tabuada}: '))
print()
inicio = int(input(f'Digite novamente o número {tabuada}: '))
print()
for n in range(inicio, valor / 1, passo):
    resultado = n / tabuada
print(f'{n} / {tabuada} = {resultado:.0f}')