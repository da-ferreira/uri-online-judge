
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(0)
else:
    vetor = [0, 1, 0, 0]
    mod = 10 ** 9 + 7

    vetor[1] = 1

    for i in range(3, n + 1):
        vetor[3] = vetor[3 - 2] + vetor[3 - 3]
        vetor.pop(0)
        vetor.append(0)

    print(vetor[-2] % mod)

