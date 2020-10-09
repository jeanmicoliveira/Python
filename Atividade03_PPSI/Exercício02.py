"""
Elabore um programa para solicitar o nome de uma equipe de futebol, a quantidade de derrotas, empates e vitórias obtidas por ela no campeonato. No futebol, cada vitória vale três pontos e cada empate vale um ponto. Calcular e informar: a quantidade de pontos ganhos, a quantidade de pontos perdidos e o percentual de aproveitamento da equipe.
"""

print()
print('Caculadora de pontos ganhos, quantidade de pontos perdidos e o percentual de aproveitamento da equipe selecionada.')
print()
time = input('Digite o nome do time selecionado: ')
vit = int(input('Digite o número de vitórias deste time: '))
der = int(input('Digite o número de derrotas deste time: '))
emp = int(input('Digite o número de empates deste time: '))

pg = vit * 3 + emp
pp = der * 3
pe = emp * 1
jogos = vit + der + emp

aprov = (pg / (jogos * 3)) * 100

print('O', time, 'obteve', pg, 'pontos ganhos', 'tendo', pp, 'pontos perdidos num total de', jogos,' jogos e o seu percentual de aproveitamento foi de: {:.1f}'.format(aprov), '%.')