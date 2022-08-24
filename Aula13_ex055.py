"""
Exercício Python 055:
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.

"""
#Tentativa de solução
"""
peso_maior = 0
peso_menor = 0

for pessoas in range(1, 6):
    peso = int(input('Informe o peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        peso_menor = peso
        peso_menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso

print('O maior peso foi da {}ª pessoa.'.format(peso_maior))
print('O menor peso foi da {}ª pessoa.'.format(peso_menor))
"""
#Solução Guanabara
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O maior peso lido foi de {}Kg'.format(menor))

