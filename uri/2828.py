
from math import factorial
from string import ascii_letters

caracteres = input()

letras = {}

for i in range(26):
    letras[ascii_letters[i]] = caracteres.count(ascii_letters[i])

soma = 1

for i in letras:
    if letras[i] > 1:
        soma *= factorial(letras[i])

resultado = factorial(len(caracteres)) // soma
print(resultado % 1000000007)
