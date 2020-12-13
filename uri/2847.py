
frase = input()

letras = {
    'y': 0,
    'I': 0,
    'v': 0, 
    'o': 0, 
    '!': 0, 
    'e': 0, 
    'u': 0, 
    'l': 0
}

for caracter in frase:
    if caracter in letras:
        letras[caracter] += 1

letras['o'] //= 2

if min(letras.values()) > 0:
    print(min(letras.values()))
else:
    print(0)

