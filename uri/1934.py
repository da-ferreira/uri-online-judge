
linhas, colunas = map(int, input().split())

quebra_cabeca = []
variaveis = {}  # guarda os valores das variaveis.

for i in range(linhas + 1):
    quebra_cabeca.append(input().split())

    if i != linhas:
        for j in range(colunas):
            if quebra_cabeca[-1][j] not in variaveis:
                variaveis[quebra_cabeca[-1][j]] = None
            
parada = 0

while parada < len(variaveis):
    for i in range(linhas):
        variaveis_nao_calculadas = {}
        soma = 0  # soma das variaveis que ja foram achadas.

        for j in range(colunas):
            if variaveis[quebra_cabeca[i][j]] is None:
                if quebra_cabeca[i][j] not in variaveis_nao_calculadas:
                    variaveis_nao_calculadas[quebra_cabeca[i][j]] = 1
                else:
                    variaveis_nao_calculadas[quebra_cabeca[i][j]] += 1
            else:
                soma += variaveis[quebra_cabeca[i][j]]

        if len(variaveis_nao_calculadas) == 1:
            temp = list(variaveis_nao_calculadas.keys())  # pegando a chave da unica variavel que nao foi calculada.

            variaveis[temp[0]] = (int(quebra_cabeca[i][colunas]) - soma) // variaveis_nao_calculadas[temp[0]]
            parada += 1  # mais um valor de variavel achada


    for j in range(colunas):
        variaveis_nao_calculadas = {}
        soma = 0

        for i in range(linhas):
            if variaveis[quebra_cabeca[i][j]] is None:
                if quebra_cabeca[i][j] not in variaveis_nao_calculadas:
                    variaveis_nao_calculadas[quebra_cabeca[i][j]] = 1
                else:
                    variaveis_nao_calculadas[quebra_cabeca[i][j]] += 1
            else:
                soma += variaveis[quebra_cabeca[i][j]]

        if len(variaveis_nao_calculadas) == 1:
            temp = list(variaveis_nao_calculadas.keys())  # pegando a chave da unica variavel que nao foi calculada.
            
            variaveis[temp[0]] = (int(quebra_cabeca[linhas][j]) - soma) // variaveis_nao_calculadas[temp[0]]
            parada += 1  # mais um valor de variavel achada


for i in sorted(variaveis.keys()):
    print(i, variaveis[i])
