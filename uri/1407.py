
while True:
    sorteios, qtd_aposta, valor_maximo = map(int, input().split())
    if sorteios == 0:
        break

    numeros = {x: 0 for x in range(1, valor_maximo + 1)}
        
    for i in range(sorteios):
        entrada = list(map(int, input().split()))

        for j in range(qtd_aposta):
            numeros[entrada[j]] += 1
    
    menor = min(numeros.values())
    resultados = []

    for i in numeros:
        if numeros[i] == menor:
            resultados.append(str(i))

    print(' '.join(resultados))
