
tabela = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 1,
    'k': 2,
    'l': 3,
    'm': 4,
    'n': 5,
    'o': 6,
    'p': 7,
    'q': 8,
    'r': 9,
    's': 1,
    't': 2,
    'u': 3,
    'v': 4,
    'w': 5,
    'x': 6,
    'y': 7,
    'z': 8
}


while True:
    try:
        nome = input()
        soma = 0

        for i in range(len(nome)):
            if nome[i] != ' ':
                soma += tabela[nome[i].casefold()]
        
        soma = str(soma)

        while len(soma) != 1:
            soma = [int(x) for x in soma]
            soma = sum(soma)
            soma = str(soma)
        
        print(soma)
    except EOFError:
        break