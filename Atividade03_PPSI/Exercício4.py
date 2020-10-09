"""
Faça um programa que leia dois números e mostre qual o maior dos dois. O programa deve informar caso sejam iguais.
"""
print('Escolha somente números inteiros.')
n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

if n1 == n2:
    print('Os números selecionados são iguais.')

if n1 > n2:
    print('O primeiro número digitado é maior que o segundo número.')

if n1 < n2:
    print('O Segundo número é maior que o primeiro número digitado.')
