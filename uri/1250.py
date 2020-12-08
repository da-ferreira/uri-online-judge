
casos = int(input())

for i in range(casos):
    qtd_tiros = int(input())
    altura = list(map(int, input().split()))
    pulos = input()

    atingido = 0

    for j in range(qtd_tiros):
        if pulos[j] == 'S' and altura[j] in range(1, 3):
            atingido += 1
        
        elif pulos[j] == 'J' and altura[j] > 2:
            atingido += 1
    print(atingido)
