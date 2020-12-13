
j = 1
while True:
    n = int(input())
    if n == 0:
        break

    participantes = list(map(int, input().split()))

    print(f'Teste {j}')

    for i in range(n):
        if participantes[i] == (i + 1):
            print(participantes[i])
    
    print()

    j += 1

