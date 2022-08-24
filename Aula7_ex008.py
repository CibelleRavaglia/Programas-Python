"""
Exercício Python 008:
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e
milímetros
km hm dam m dm cm mm
0  0   0  1 0  0  0

"""
#Uma possibilidade
medida = float(input("Informe uma distância em metros: "))
cm = medida *100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm.'.format(medida, cm, mm))