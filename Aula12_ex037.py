"""
Exercício Python 037:
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

"""
#Solução Guanabara
"""
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:])) #fatiando
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
"""
#Complementos de pesquisa
#Fonte usada: https://acervolima.com/python-converter-string-em-binario/
#Método 1
"""
teste_str = 'GeekforGeeks'
print("The original string is : " + str(teste_str))
res = ''.join(format(ord(i), 'b') for i in teste_str)
print("The string after binary conversion : " + str(res))

teste_str = 'ODiógeneséruim!!!'
print('A string original é: ' + str(teste_str))
resultado = ''.join(format(ord(i), 'b') for i in teste_str)
print('String em binário: ' + str(resultado))
"""
#Método 2
"""
test_str = "GeeksforGeeks"
print("The original string is : " + str(test_str))
res = ''.join(format(i, 'b') for i in bytearray(test_str, encoding ='utf-8'))
print("The string after binary conversion : " + str(res))
"""
D = 'Non videmus manticae quod in tergo est!'
print('A string original é: ' + str(D))
resultado = ''.join(format(i, 'b') for i in bytearray(D, encoding = 'utf-8' ))
print('String em binário: ' + str(resultado))
