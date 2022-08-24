"""
Exercício Python 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

"""

#Minha solução
"""
from datetime import date
atual = date.today().year
nascimento = int(input('Informe seu ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))
if idade <= 9:
    print('Você faz parte da categoria MIRIM!')
elif idade <= 14:
    print('Você faz parte da categoria INFANTIL!')
elif idade <= 19:
    print('Você faz parte da categoria JÚNIOR!')
elif idade <= 25:
    print('Você faz parte da categoria SÊNIOR!')
elif idade > 25:
    print('Você faz parte da categoria MASTER!')
"""
#Solução Guanabara
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <=9:
    print('Classificação: MIRIM!')
elif idade <= 14:
    print('Classificação: INFANTIL!')
elif idade <= 19:
    print('Classificação: JÚNIOR!')
elif idade <= 25:
    print('Classificação: SÊNIOR!')
else:
    print('Classificação: MASTER!')


