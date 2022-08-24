"""
Exercício Python 030:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

"""
#Matematicamente:
#O resto da divisão de qualquer número par por 2 é zero.
#O resto da divisão de qualquer número ímpar por 2 é 1.
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR.'.format(numero))
else:
    print('O número {} é ÍMPAR.'.format(numero))


