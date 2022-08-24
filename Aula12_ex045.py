"""
Exercício Python 045:
Crie um programa que faça o computador jogar Jokenpô com você.

"""
#Solução Guanabara/Melhorada por mim
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[1;36;100mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[1;36;100m''')
jogador = int(input('Qual é a sua jogada? '))
print('\033[1;97;100mJO\033[m')
sleep(1)
print('\033[1;97;100mKEN\033[m')
sleep(1)
print('\033[1;97;100mPO!!!\033[m')
print('\033[1;31;100m-=' * 15)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('\033[1;31;100m-=' * 15)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('\033[1;94;100mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;94;100mJOGADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;94;100mCOMPUTADOR VENCE!\033[m')
    else:
        print('\033[1;94;100mJOGADA INVÁLIDA!!!\033[m')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('\033[1;94;100mCOMPUTADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1;94;100mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;94;100mJOGADOR VENCE!\033[m')
    else:
        print('\033[1;94;100mJOGADA INVÁLIDA!!!\033[m')
elif computador == 2:#Computador jogou TESOURA
    if jogador == 0:
        print('\033[1;94;100mJOGADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1;94;100mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;94;100mEMPATE!\033[m')
    else:
        print('\033[1;91;100mJOGADA INVÁLIDA!!!\033[m')





