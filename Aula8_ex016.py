"""
Exercício Python 016:
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua
porção Inteira.
Exemplo: digite um número: 6.217
O número 6.217 tem a parte inteira 6.

"""
#Importando a biblioteca math
"""
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, trunc(num)))

"""
#Sem importar a biblioteca
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}.'.format(num, int(num)))
