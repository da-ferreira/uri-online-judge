
while True:
    n = int(input())
    if n == 0:
        break

    tentativas = 0
    ordem_certa = [str(x) for x in range(1, n + 1)]

    while True:
        ordenacao = input().split()
        tentativas += 1

        if ordenacao == ordem_certa:
            break

    print(tentativas)
