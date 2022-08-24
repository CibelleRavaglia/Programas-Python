"""
Exercício Python 007:
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

"""
#Erro clássico por causa da ordem de precedência.
"""
n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))
m = n1 + n2 / 2 # Aqui está o erro, sem ordem de precedência
print('A média entre {} e {} é igual a {}.'.format(n1, n2, m))

"""
#Código com a ordem de precedência certa, com ()
n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))
m = (n1 + n2) / 2 #Colocando parênteses
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, m))
# o :.1f utiliza as regras de arredondamento, 1 float após o ponto
