"""
Exercício Python 019:
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do
escolhido.

"""
#Também pode ser: from random import choice
import random
n1 = str(input('Informe o primeiro aluno: '))
n2 = str(input('Informe o segundo aluno: '))
n3 = str(input('Informe o terceiro aluno: '))
n4 = str(input('Informe o quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))

