"""
Exercício Python 006:
Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

"""
#Uma possibilidade
"""
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raizq = num ** (1/2) #Parêntes para forçar a execução, ordem de precedência.
print('O dobro de {} vale {}.'.format(num, dobro))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.3f}.'.format(num,triplo, num, raizq))

"""
#Outras possibilidades
num = int(input('Informe um número: '))
print('O dobro de {} vale {}.'.format(num, (num*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(num, (num*3), num, (num**(1/2))))

#Dá para usar a função pow(num, (1/2))

