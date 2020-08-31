""" FAÇA UM PROGRAM QUE OBTENHA A PARTIR DA DIGITAÇÃO DO USUÁRIO OS SEGUINTES DADOS:
A QUANTIDADE DE ALUNOS QUE FAZEM O CURSO DE SISTEMAS DE INFORMAÇÃO E A QUANTIDADE
DE ALUNOS QUE FAZEM O CURSO DE ANÁLISE DE SISTEMAS. AO FINAL O PROGRAMA DEVE INFORMAR O TOTAL DE ALUNOS, A PORCETAGEM DE ALUNOS
QUE FAZEM SISTEMAS E A PORCETAGEM DE ALUNOS QUE CURSAM ANÁLISES."""

qtd_sistemas = int(input('Quantidade de alunos que cursam Sistemas: '))
qtd_análises = int(input('Quantidade de alunos que cursam Análises:'))
total_alunos = qtd_sistemas+qtd_análises
print('Total de alunos:', total_alunos)
perc_sistemas = qtd_sistemas/total_alunos*100
print('A porcentagem de alunos de Sistemas é:', perc_sistemas,'%')
perc_análises = qtd_análises/total_alunos*100
print('A porcentagem de alunos de Análises é:', perc_análises,'%')