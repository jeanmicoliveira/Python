"""
Crie um programa que leia a altura de 10 pessoas. Ao final o programa deve informar o total de pessoas cadastradas, a quantidade de pessoas com altura inferior a 1,60 metros; a quantidade de pessoas com altura entre 1,60 metros e 1,80 metros e a quantidade de pessoas com altura superior a 1,80 metros.
"""


cadastros = inferior = entre = superior = 0

for cadastros in range(10):
    altura = float(input('Informe a altura: '))

    if altura < 1.6:
        inferior += 1
    elif 1.8 >= altura >= 1.6:
        entre += 1
    else:
        superior += 1

print(f'''
Foram cadastradas {cadastros + 1} pessoas
Pessoas com altura menor de 1,6m: {inferior}
Pessoas com altura entre 1,60m e 1,8m: {entre}
Pessoas com altura superior a 1,8m: {superior}''')