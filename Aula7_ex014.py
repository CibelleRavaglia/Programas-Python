"""
Exercício Python 014:
4: Escreva um programa que converta uma temperatura digitando em graus Celsius e
converta para graus Fahrenheit.

"""
c = float(input('Informe a temperatura em °C: '))
f = ((9 *c ) /5 + 32) #Fórmula graus para fahrenheit
print('A temperatura de {0}°C corresponde a {1}°F!'.format(c, f))