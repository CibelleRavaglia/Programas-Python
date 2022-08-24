"""
Exercício Python 017:
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#Sem importação
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa será de {:.2f}.\nEnfim, a hipotenusa.'.format(hi))

"""
#Importando a coisa mais linda que eu já vi
import math
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa será de {:.2f}. \nJá diria Pitágoras, enfim, a hipotenusa.'
      ''.format(hi))

