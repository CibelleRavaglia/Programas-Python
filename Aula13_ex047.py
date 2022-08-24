"""
Exercício Python 047:
Crie um programa que mostre na tela todos os números pares que estão no intervalo
entre 1 e 50.

"""
#Minha solução
"""
for c in range(0, 51):
    if (c % 2) == 0:
        print('Os números pares são {}.'.format(c))
"""
#Soluções Guanabara
"""
for n in range(1, 51):
    print('.', end= '') #Mostra as iterações
    if n % 2 == 0:
        print(n, end= ' ')
print('ACABOU!!!')
    #print('{} '.format(n))
"""
for n in range(2, 51, 2):
    print(n, end= ' ')
print('ACABOU!')




