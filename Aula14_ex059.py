"""
Exercício Python 059:
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
#Tentativa de solução
"""

print('Seja bem-vindX!')
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
opções = int(input('''Escolha uma das seguintes opções:\n
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
Informe a opção escolhida: '''))
while opções:
    if opções == '1':
        soma = valor1 + valor2
        print('A soma de {} + {} é {}'.format(valor1, valor2, soma))
"""
#Solução Guanabara com melhorias minhas
from time import sleep
print('Seja bem-vindX!')
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa ''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}.'.format(n1, n2, produto))
    elif opção == 3:
        if n > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente.')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre, gafanhotX!')
