
notas = {
    'W': 1,
    'H': 1 / 2,
    'Q': 1 / 4,
    'E': 1 / 8,
    'S': 1 / 16,
    'T': 1 / 32,
    'X': 1 / 64
}

while True:
    composicao = input()
    if composicao == '*':
        break

    composicao = composicao.split('/')
    
    composicao.pop(0)
    composicao.pop(-1)

    acertos = 0

    for i in range(len(composicao)):
        soma = 0
        
        for letra in composicao[i]:
            soma += notas[letra]

        if soma == 1:
            acertos += 1

    print(acertos)    
