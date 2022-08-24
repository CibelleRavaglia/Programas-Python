"""
Exercício Python 052:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
Obs: número primo só é divisível por duas vezes. Dividido por um e por ele mesmo.

"""
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='') #Amarelo se for divisível.
        tot = tot + 1 #tot +=1
    else:
        print('\033[31m', end='') #Vermelho se não for divisível
    print('{} ->'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('E, por isso, o número é PRIMO!')
else:
    print('E, por isso, o número NÃO É PRIMO!')
