"""
Exercício Python 036:
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

"""
#Minha solução
"""
valor_casa = float(input('Informe o valor da casa que deseja comprar: R$'))
salário = float(input('Agora, informe o seu salário: R$ '))
prestações = float(input('Informe em quantos anos deseja pagar o imóvel: '))
meses = prestações * 12
prestações = valor_casa / meses
if prestações > salário * 0.3:
    print('Infelizmente, você não é elegível para o financiamento.')
else:
    print('Parabéns, arrombado(a)(x)! CASA PRÓPRIA!!!')
"""

#Solução Guanabara
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de '
      'R${:.3f}'.format(casa, anos, prestação))
if prestação <= mínimo:
      print('Empréstimo pode ser CONCEDIDO!')
else:
      print('Empréstimo NEGADO!!!')




