"""
Exercício Python 012:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
Para lembrar: 10*5/100 = 0.5 - regra de porcentagem

"""
preco = float(input('Qual é o preço do produto? R$'))
novo_preco = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5%, custará R${:.2f}.'.format(preco, novo_preco))