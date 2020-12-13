
while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    numeros = list(map(int, input().split()))
    
    permutacao = [0] * quantidade
    semelhancas = 0

    for i in range(0, quantidade):
        permutacao[numeros[i] - 1] = i + 1

        if permutacao[numeros[i] - 1] == numeros[numeros[i] - 1]:
            semelhancas += 1
    
    if semelhancas == quantidade:
        print('ambiguous')
    else:
        print('not ambiguous')
