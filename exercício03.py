"""FAÇA UM PROGRAMA QUE LEIA A PARTIR DA DIGITAÇÃO DE UN USUÁRIO A DESCRIÇÃO DE UM PRODUTO, O SEU VALOR UNITÁRIO E A SUA QUANTIDADE. o PROGRAMA DEVE CALCULAR E INFORMAR O VALOR A PAGAR PELO PRDUTO."""

descrição = input('Descrição do produto: ')
valor = float(input('Digite o valor unitário: '))
quantidade = int(input('Digite a quantidade: '))
total = valor * quantidade
print('Valor a pagar: ', total)