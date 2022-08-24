"""
Exercício Python 064:
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).

"""
#Minha solução/Tentiva
"""
n = int(input('Informe o número desejado ou digite 999 para sair:  '))
soma = 0
cont = 0
total = 0
while n != 999:
    n = int(input('Informe o número desejado ou digite 999 para sair: '))
    
    
    else:
print('Programa finalizado.')
"""
#Solução Guanabara
#núm = cont = soma = 0 #Mais limpo
núm = 0
cont = 0
soma = 0
núm = int(input('Digite um número ou 999 para parar: '))
while núm != 999:
    soma += núm #soma = soma + número
    cont += 1
    núm = int(input('Digite um número ou 999 para parar: '))
print('Você digitou {} números e as soma entre eles foi {}.'.format(cont, soma)) #-999gambiarra







