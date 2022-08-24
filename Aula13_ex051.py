"""
Exercício Python 051:
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'Conta de 0 até 10 de 2 em 2: 0, 2, 4, 6, 8, 10, onde o primeiro termo é 0 e a razão
é 2.'

"""
#Solução Guanabara
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão #Fórmula do enézimo termo de uma PA
for c in range(primeiro, décimo + razão, razão):
    print('{} '.format(c), end= '-> ')
print('Acabou!')
