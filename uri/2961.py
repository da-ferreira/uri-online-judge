
anos = int(input())

erros = [[1, 0], [2, 0], [3, 0], [4, 0]]

maior = 0

for i in range(anos):
    palpites = input()

    melhor_filme = input()
    melhor_diretor = input()
    melhor_atriz = input()
    melhor_ator = input()
 
    vencedores = input()

    melhor_filme2 = input()
    melhor_diretor2 = input()
    melhor_atriz2 = input()
    melhor_ator2 = input()

    if melhor_filme != melhor_filme2:
        erros[0][1] += 1
    
    if melhor_diretor != melhor_diretor2:
        erros[1][1] += 1
    
    if melhor_atriz !=  melhor_atriz2:
        erros[2][1] += 1
    
    if melhor_ator != melhor_ator2:
        erros[3][1] += 1

    for j in range(4):
        if erros[j][1] > maior:
            maior = erros[j][1]
    
printar = []

for i in range(4):
    if erros[i][1] == maior:
        printar.append(str(erros[i][0]))

print(' '.join(printar))
