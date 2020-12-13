
qtd_letras, qtd_frases = map(int, input().split())

letras_front, letras_back = {}, {}

for i in range(qtd_letras):
    letras = input().split()

    letras_front[letras[0]] = letras[1]
    letras_back[letras[1]] = letras[0]

for i in range(qtd_frases):
    frase = list(input())

    for j in range(len(frase)):
        if frase[j] in letras_front:
            frase[j] = letras_front[frase[j]]
        elif frase[j] in letras_back:
            frase[j] = letras_back[frase[j]]

    print(''.join(frase))
