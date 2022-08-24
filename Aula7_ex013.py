"""
Exercício Python 013:
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
com 15% de aumento.

"""
#Minha solução
"""
salario_atual = float(input('Informe o seu salário atual: R$'))
aumento = salario_atual + (salario_atual * 15 / 100)
print("Seu novo salário com 15% de aumento é de {}.".format(aumento))

"""
#Solução Guanabara
salario = float(input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 /100)
print('Um funcionário que ganhava R${:.2f}, com 15%, passa a receber R${:.2f}'.format(salario, novo))