"""
Exercício Python 067:
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.

"""
#Minha solução
"""
from time import sleep
print('Bem-vindo todas, todes e todos!')
print('----'* 8)
print('Tabuada!!!')
print('----'* 8)
num = 0
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('Calculando a tabuada...')
    sleep(3)
    if num < 0:
        print('Vejamos...')
        sleep(3)
        break
        print('Programa finalizado, vá estudar!!!')
    for c in range(1, 11):
            print(f'{num} x {c} = {num * c}')
"""
#Solução Guanabara
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {n} = {n * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')