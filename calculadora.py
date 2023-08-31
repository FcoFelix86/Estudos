import os

operacao = input('''
Digite a operação que vai iniciar:
+ Soma
- Subtração
* Multiplicação
/ Divisão
''')

num_1 = int(input('Entre com o Primeiro número: '))
num_2 = int(input('Entre com o Segundo número: '))

if operacao == '+':
   print('{} + {} = '.format(num_1, num_2))
   print(num_1 + num_2)

elif operacao == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)

elif operacao == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)

elif operacao == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)
else:
   os.system('clear')
