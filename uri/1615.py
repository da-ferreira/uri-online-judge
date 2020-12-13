
casos = int(input())

for i in range(casos):
    n, m = map(int, input().split())

    votacao = [0] * n
    votos = input().split()

    for j in range(1, n+1):
        votacao[j - 1] = votos.count(str(j))

    maior = votacao.index(max(votacao)) + 1
    quantidade = max(votacao)

    if quantidade * 100 / m > 50:
        print(maior)
    else:
        print(-1)
