"""
Exercício Python 003:
Crie um programa que leia dois números e mostre a soma entre eles.
"""
#Tem que colocar o tipo primitivo para não concatenar
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
