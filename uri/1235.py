
quantidade = int(input())

for i in range(quantidade):
    frase = input()
    
    metade = round((len(frase) / 2) - 1)
    new_frase = frase[metade::-1]
    new_frase += frase[-1:metade:-1]

    print(new_frase)
