
testes = 1

while True:
    qtd_aeroporto, qtd_voos = map(int, input().split())
    if qtd_aeroporto == 0 and qtd_voos == 0:
        break

    aeroportos = [0] * qtd_aeroporto

    maior = 0

    for i in range(qtd_voos):
        x, y = map(int, input().split())

        aeroportos[x - 1] += 1
        aeroportos[y - 1] += 1

        if aeroportos[x - 1] > maior:
            maior = aeroportos[x - 1]
        
        if aeroportos[y - 1] > maior:
            maior = aeroportos[y - 1]

    print(f'Teste {testes}')

    for i in range(qtd_aeroporto):
        if aeroportos[i] == maior:
            print(i + 1, end=' ')

    print('\n')

    testes += 1
