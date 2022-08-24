"""
Exercício Python 044:
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros

"""
#Minha solução
"""
from time import sleep
preço = float(input('Qual o preço do produto? R$'))
pagamento = int(input('Escolha as opções abaixo para selecionar a condição de'
                      ' pagamento:\n'
                      '[ 1 ] Dinheiro ou cheque: 10% de desconto.\n'
                      '[ 2 ] À vista no cartão: 5% de desconto. \n'
                      '[ 3 ] Em até duas vezes no cartão. Preço normal.\n'
                      '[ 4 ] Em três vezes no cartão: 20% de juros.\n' ))
print('Calculando...')
sleep(3)
if pagamento == 1:
    pagar = preço - (preço * 10 / 100)
    print('O valor a pagar é de R${:.2f}.'.format(pagar))
elif pagamento == 2:
    pagar = preço - (preço * 5 / 100)
    print ('O valor a pagar é de R${:.2f}.'.format(pagar))
elif pagamento == 3:
    pagar = preço
    print('O valor a pagar é de R${:.2f}.'.format(pagar))
elif pagamento == 4:
    pagar = preço +  (preço * 20 / 100)
    print('O valor a pagar é de R${:.2f}.'.format(pagar))
"""

#Solução Guanabara
print('{:=^40} ' .format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque. 
[ 2 ] À vista no cartão.
[ 3 ] 2x no cartão. 
[ 4 ] 3x ou mais no cartão. ''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 /100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcela em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    total_de_parcela = int(input('Quantas parcelas? '))
    parcela = total / total_de_parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(total_de_parcela, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente.')

print('Sua compra de R${:.2f} custará R${:.2f} no final.'.format(preço, total))


