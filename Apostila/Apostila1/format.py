"""Método Format"""

"""
Exemplo 01
frase = 'O filme {0} merece {1} estrelas'
print(frase.format('Pantera Negra', 5))
"""
"""
Exemplo 2 
"""

texto = '{0} percorreu {quilometragem} quilômetros.'
print('Programa para calcular quanto um motorista percorreu em uma viagem')
nome = input('Entre com o nome do motorista: ')
kmi = int(input('Digite a quilometragem inicial do veículo: '))
kmf = int(input('Digite a quilometragem final do veículo: '))
print(texto.format(nome, quilometragem = kmf - kmi))
