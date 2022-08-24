"""
Exercício Python 002:
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input("Qual seu nome? ")
idade = input("Quantos anos você tem? ")
peso = input("Qual é o seu peso? ")
print(f"Seu nome é {nome}, sua idade é {idade} e seu peso é {peso}.")

nome = input("Digite seu nome: ")
print("É um prazer te conhecer, {}!".format(nome))

#Se tirar o int, não tem soma, ele junta, concatena
n1 = int(input('Digite um número: '))
#print(type(n1))
n2 = int(input('Digite mais um número: '))
#print(type(n2))
s = n1 + n2
#print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

"""
#Mais um teste
#Métodos na seguinte ordem
#Se é número
#Se é alpha, alfabético
#Se é alfanumérico
#Se tem letra maíscula
n = (input('Digite um valor: '))
#print(n.isnumeric())
#print(n.isalpha())
#print(n.isalnum())
print(n.isupper())





