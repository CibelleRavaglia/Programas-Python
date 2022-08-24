"""
Exercício Python 046:
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
#Minha solução
"""
from time import sleep
i = print('Todos prontos para começar:?')
for c in range(0, 11,):
    print(c, '...')
    sleep(1)
print('BUM!!!')
"""
#Solução Guanabara
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('BUM! POOW!!!')


