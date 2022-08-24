"""
Exercício Python 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida

"""
#Minha solução
"""
from time import sleep
peso = float(input('Informe seu peso atual: '))
altura = float(input('Informe sua altura com ponto: '))
IMC = (peso / (altura * altura))
print('Calculando...')
sleep(3)
print('Seu IMC é de {:.2f}.'.format(IMC))
if IMC < 18.5:
    print('Classificação: ABAIXO DO PESO.')
elif IMC == 18.5:
    print('Classificação: PESO IDEAL.')
elif IMC >= 25:
    print('Classificação: SOBREPESO.')
elif IMC >= 30:
    print('Classificação: OBESIDADE.')
elif IMC > 40:
    print('Classificação: OBESIDADE MÓRBIDA.')
"""
#Solução do Guanabara
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO NORMAL.')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBSESIDADE MÓRBIDA, vá ao médico!')


