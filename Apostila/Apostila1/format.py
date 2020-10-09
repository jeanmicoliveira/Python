"""Método Format"""

"""
Exemplo 01
frase = 'O filme {0} merece {1} estrelas'
print(frase.format('Pantera Negra', 5))
"""
"""
Exemplo 2 


texto = '{0} percorreu {quilometragem} quilômetros.'
print('Programa para calcular quanto um motorista percorreu em uma viagem')
nome = input('Entre com o nome do motorista: ')
kmi = int(input('Digite a quilometragem inicial do veículo: '))
kmf = int(input('Digite a quilometragem final do veículo: '))
print(texto.format(nome, quilometragem = kmf - kmi))
"""

"""
Format com string - estrutura


texto = 'Programando em Python'

print("{0:>20}" .format(texto)) #alinha 20 a direita
print("{0:<20}" .format(texto)) #alinha 20 a esquerda
print("{0:.5}" .format(texto))  #imprime as 5 primeiras strings ( do 0 ao 4)
"""

"""
Format com núnemos - estrutura
"""

print('Programa para calcular o salário de um funcionário')
nome = input('Entre com o nome do funcionario: ')
base = float(input('Digite o salário base: '))
desconto = float(input('Digite o desconto: '))
salário = base - desconto
print('{0} teve média igual a: {1:4.2f}' .format(nome, salário),' reais.')