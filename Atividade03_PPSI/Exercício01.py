"""Faça um programa que dado o valor da temperatura em graus FARENHEIT, calcular e escrever o valor da temperatura em
graus CELSIUS. Fórmula: C = 5/9 * (F - 32) """

print('Conversor de temperatura de ºF para ºC.')
F = float(input('Insira o valor da temperatura em graus Fahrenheit: '))
C = (F - 32) * (5 / 9)
print('A temperatura em graus Celsius é de: {0:.1f}ºC' .format(C))