
def linha_a(p, q, x, dimensao, linha):
    linha_a = [(p * linha + q * j) % x for j in range(1, dimensao + 1)]

    return linha_a


def coluna_b(r, s, y, dimensao, coluna):
    coluna_b = []

    for i in range(1, dimensao + 1):
        coluna_b.append((r * i + s * coluna) % y)

    return coluna_b


def indice_i_j(linha, coluna, dimensao):
    resultante = 0

    for i in range(dimensao):
        resultante += (linha[i] * coluna[i])
    
    return resultante


tamanho = int(input())

P, Q, R, S, X, Y = map(int, input().split())
linha, coluna = map(int, input().split())

line = linha_a(P, Q, X, tamanho, linha)
column = coluna_b(R, S, Y, tamanho, coluna)

print(indice_i_j(line, column, tamanho))
