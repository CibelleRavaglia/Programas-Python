"""
Exercício Python 054:
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores.

"""
#Tentativa de solução
"""
from datetime import date
atual = date.today().year
for c in range(1, 8):
    pessoas = float(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - pessoas
if pessoas == 18:
        print('Tantas {} são maiores de idade!'.format(idade))
if pessoas > 18:
        print('Tantas {} são menores de idade!'.format(idade))
else:
        print('Tantas {} maiores de idade!'.format(idade))
"""
#Solução Guanabara
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1 #totmaior +=1
    else:
        totmenor = totmenor + 1 #totmenor +=1
print('Ao todo temos {} pessoas maiores de idade.'.format(totmaior))
print('E também temos {} pessoas menores de idade.'.format(totmenor))




