
j = 1
while True:
    n = int(input())
    if n == 0:
        break

    movimentos = 1

    for i in range(n - 1):
        movimentos += (movimentos + 1)

    print(f'Teste {j}')
    print(movimentos)
    print()

    j += 1
