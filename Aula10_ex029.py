"""
Exercício Python 029:
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
Divide et impera!
"""
#Minha resolução
"""
velocidade = int(input('Qual a velocidade do seu carro? '))
if velocidade >= 80:
    print('Você não tem multa.')
else:
    velocidade <= 80
    print("Você foi tem uma multa, gafanhoto!")
"""
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado. Você excedeu o limite permitido de 80 km/h!')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha uma boa viagem. Dirija com segurança!')


