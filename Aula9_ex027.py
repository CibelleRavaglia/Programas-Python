"""
Exercício Python 027:
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

"""
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()#Vai fatiar os nomes em pedaços separados por espaços, joga numa lista
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))