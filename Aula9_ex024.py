"""
Exercício Python 024:
Crie um programa que leia o nome de uma cidade diga se ela começa ou não
com o nome “SANTO”.

"""
#O strip elimina os espaços
#O upper converte o que o usuário escreveu para maiúsculo
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')