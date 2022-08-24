"""
Exercício Python 040:
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO

"""
#Minha solução
"""
nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informa sua segunda nota: "))
média = (nota1 + nota2) / 2
print('Sua média é de {}.'.format(média))
if média < 5.0:
    print('REPROVADO, ARROMBADO. Estude mais!!!')
elif média >= 5.0 and média <= 6.9:
    print('RECUPERAÇÃO!')
elif média >= 7.0 and média > 7.0:
    print('APROVADO, GAFANHOTO!!!')
"""

#Solução Guanabara
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, média))
#if média > 5 and média < 7: #jeito tradicional de fazer
if 7 > média >= 5:
    print('O aluno está e RECUPERAÇÃO.')
elif média <5:
    print('O aluno está REPROVADO!')
elif média >= 7: #Código mais legível
    print('O aluno está APROVADO!')

