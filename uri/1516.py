
while True:
    linhas, colunas = map(int, input().split())
    if linhas == 0 and colunas == 0:
        break

    figura = []

    for i in range(linhas):
        figura.append(input())
    
    redimensionar_linhas, redimensionar_colunas = map(int, input().split())

    redimensionar_linhas //= linhas
    redimensionar_colunas //= colunas

    nova_figura = [[''] for x in range(linhas)]
    
    for i in range(colunas):
        for j in range(colunas):
            nova_figura[i][0] += figura[i][j] * redimensionar_colunas
    
    figura.clear()

    for i in range(linhas):
        for j in range(redimensionar_linhas):
            figura.append(nova_figura[i])
    
    for i in range(len(figura)):
        print(figura[i][0])
    
    print()
