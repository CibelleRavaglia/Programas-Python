"""
Exercício Python 066:
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).

"""
#Minha solução
#número = 0 contador = 0 soma = 0 #Mais limpo
"""
from time import sleep
número = 0
contador = 0
soma = 0
print('Bem-vindo todas, todos e todes!!!')
while True:
    número = int(input('Informe um número ou digite 999 para sair: '))
    if número == 999: #Condição de parada/flag
        break
    soma = soma + número # soma += número
    contador = contador + 1 #contador += 1
print('Calculando...')
sleep(3)
print('Você digitou {} números e a soma entre eles é de {}.'.format(contador, soma))
print('Programa finalizado.')
"""

#Solução Guanabara
soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
#soma -= 999 #Gambiarra fudida
print(f'A soma dos {cont} valores foi de {soma}!')#F-strings









