
testes = 1

while True:
    participantes, qtd_rodadas = map(int, input().split())
    if participantes == 0:
        break

    fila = list(map(int, input().split()))
    
    for i in range(qtd_rodadas):
        rodada = list(map(int, input().split()))
        
        n_round = rodada.pop(0)
        ordem = rodada.pop(0)
        apagar = set()

        for j in range(n_round):
            if rodada[j] != ordem:
                apagar.add(j)
        
        fila = [fila[x] for x in range(len(fila)) if x not in apagar]
            
    print(f'Teste {testes}')
    print(fila[0])
    print()

    testes += 1
