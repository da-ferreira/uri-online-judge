
tabuleiro = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

colunas = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7
}

posicao_inicial, posicao_final = input().split()

values_linha = [int(posicao_final[1]) - 1, int(posicao_inicial[1]) - 1]
values_coluna = [colunas[posicao_inicial[0]], colunas[posicao_final[0]]]

if (max(values_linha) - min(values_linha)) + (max(values_coluna) - min(values_coluna)) == 3:
    print('VALIDO')
else:
    print('INVALIDO')
