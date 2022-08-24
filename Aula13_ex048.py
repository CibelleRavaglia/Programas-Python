"""
Exercício Python 048:
Faça um programa que calcule a soma entre todos os números que são múltiplos de três
e que se encontram no intervalo de 1 até 500.

"""
#Minha solução, uma merda
"""
for c in range(1, 501,):
    if c % 3 == 0:
        print('Os multiplos de 3 são: {}.'.format(c))
"""
#Minha solução sem ímpares
"""
soma = 0
contador = 0
for c in range(1, 501, 3):
    soma = soma + c #soma += c
    contador = contador + c #contador += c
    print(c)
print('ACABOU!')
"""

#Solução Guanabara
soma = 0 #Acumulador
cont = 0 #Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
     #print(c, end= ' ') #end separa por espaço

