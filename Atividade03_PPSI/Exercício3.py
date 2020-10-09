"""
Faça um programa para solicitar o nome e as duas notas de um aluno. Calcular sua média e informá-la. Se ela for inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado".
"""

aluno = input('Insira o nome do aluno: ')
nt1 = float(input('Insira a primeira nota do aluno: '))
nt2 = float(input('Insira a segunda nota do aluno: '))

md = (nt1 + nt2 ) / 2 # calculo da média
print('A média do obtida pelo',aluno, 'foi de: {:.1f}'.format(md))

if md > 7:
    print('Aprovado')

else:
    print('Reprovado')
