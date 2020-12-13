
casos = int(input())

for i in range(casos):
    n, m = map(int, input().split())

    renas = [] 

    for j in range(n):
        nome, peso, idade, altura = input().split()

        renas.append([nome, int(peso), int(idade), float(altura)])

    renas = sorted(renas, key=lambda k: k[0])
    renas = sorted(renas, key=lambda k: k[3])
    renas = sorted(renas, key=lambda k: k[2])
    renas = sorted(renas, key=lambda k: k[1], reverse=True)

    print(f'CENARIO {"{"}{(i + 1)}{"}"}')

    for j in range(m):
        print(f'{j + 1} - {renas[j][0]}')
