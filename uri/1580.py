
from math import factorial as fac
from string import ascii_uppercase

while True:
    try:
        palavra = input()
        letras = {}

        for i in range(26):
            letras[ascii_uppercase[i]] = palavra.count(ascii_uppercase[i])

        soma_k = 1

        for i in letras:
            if letras[i] > 1:
                soma_k *= fac(letras[i])
        
        result = fac(len(palavra)) // soma_k
        print(result % 1000000007)
    except EOFError:
        break

