
while True:
    try:
        n = int(input())
        vetor = sorted(list(map(int, input().split())))

        soma = 0
        j = n - 1
        meio = n // 2

        for i in range(meio):
            soma += (vetor[j] - vetor[i])
            j -= 1

        print(soma)
    except EOFError:
        break
