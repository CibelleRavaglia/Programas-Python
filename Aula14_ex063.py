"""
Exercício Python 063:
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci. Exemplo:
0 - 1 - 1 - 2
0 mais 1 = 1
o próximo termo: 1 mais 1 = 2
o próximo termo termo: 2 + 1 = 3
Sempre começa com 0 ou 1
---> 0 – 1 – 1 – 2 – 3 – 5 – 8
"""
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~' *30)
print('{} --> {}'.format(t1, t2), end='')
cont = 3 #Começa em 3, pois já mostrei o 1 termo e o 2 termo
while cont <= n:
    t3 = t1 + t2
    print(' --> {}'.format(t3), end= '')
    t1 = t2
    t2 = t3
    cont += 1
print(' --> FIM!')
