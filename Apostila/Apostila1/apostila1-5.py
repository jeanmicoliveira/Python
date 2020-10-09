"""Metodos para trabalhar com String"""

a = "            Programando em Python"
print(a.strip()) # retira os espaços.

b = "Programando em Python"
print(len(b)) # mostra o tamanho da string

c = "Programando em Python"
print(c.lower()) # tudo minúsculo

d = "Programando em Python"
print(d.upper()) # tudo maiúsculo

e = "Programando em Python"
print(e.replace("P", "C")) # substitui o P por C

f = "Programando,Python"
print(f.split(",")) # vai separar as palavras Programando e Python com uma virgula.