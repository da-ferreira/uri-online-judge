
n = 1
while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    i = quantidade // 50
    temp = quantidade % 50

    j = temp // 10
    temp %= 10

    k = temp // 5
    temp %= 5

    l = temp // 1

    print(f'Teste {n}')
    print(f'{i} {j} {k} {l}')
    print()
    
    n += 1
