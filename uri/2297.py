
i = 1
while True:
    rodadas = int(input())
    if rodadas == 0:
        break
    
    pontos = [0, 0]
    
    for j in range(rodadas):
        aldo, beto = map(int, input().split())
        pontos[0] += aldo
        pontos[1] += beto

    print(f'Teste {i}')
    if pontos[0] > pontos[1]:
        print('Aldo')
    else:
        print('Beto')
    print()

    i += 1
