"""
Exercício Python 004:
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possíveis sobre ele.

"""
#A função input retorna uma string independentemente do tipo
#O a é objeto, métodos
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('As letras estão em maiúsculas? ', a.isupper())
print('As letras estão em minúsculas? ', a.islower())
print('As letras estão capitalizadas? ', a.istitle())
