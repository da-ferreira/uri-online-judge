
casos = int(input())

pular_linhas = 1

for i in range(casos):
    tamanho = int(input())
    matriz = []

    tab_colunas = [0 for x in range(tamanho)]  # tabulação de cada coluna
        
    for j in range(tamanho):
        entrada = list(map(int, input().split()))

        matriz.append([str(valor ** 2) for valor in entrada])

        for x in range(tamanho):
            if len(matriz[-1][x]) > tab_colunas[x]:
                tab_colunas[x] = len(matriz[-1][x])

    if pular_linhas != 1:
        print()
    
    print(f'Quadrado da matriz #{i + 4}:')

    for j in range(tamanho):
        for k in range(tamanho):
            if k != (tamanho - 1):
                print(f'{matriz[j][k].rjust(tab_colunas[k])}', end=' ')
            else:
                print(f'{matriz[j][k].rjust(tab_colunas[k])}')

    pular_linhas += 1
