"""
Exercício Python 050:
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

"""
#Tentativa de solução
"""
soma = 0
cont = 0
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))
num4 = int(input('Informe o quarto o número: '))
num5 = int(input('Informe o quinto número: '))
num6 = int(input('Informe o sexto número: '))
for c in range(num1, num6):
    if c % 2 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores pares solicitados é {}.'.format(soma))
"""
#Solução Guanabara
soma = 0
cont = 0
for c in range(1, 7): #Isso é muito interessantíssimo
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num #soma += num
        cont = cont + 1 #cont += 1
print('Você informou {} números PARES e a soma foi {}.'.format(cont, soma))
