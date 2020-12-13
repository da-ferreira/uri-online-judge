
i = 1

while True:
    n = int(input())
    if n < 0:
        break

    print(f'Teste {i}')
    print(4 ** n + (2 * (2 ** n) + 1))
    print()

    i += 1
