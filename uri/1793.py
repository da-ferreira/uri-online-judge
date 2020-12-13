
while True:
    n = int(input())
    if n == 0:
        break

    pessoas = list(map(int, input().split()))

    tempo = 10

    for i in range(n - 1):
        if pessoas[i + 1] - pessoas[i] <= 10:
            tempo += pessoas[i + 1] - pessoas[i]
        else:
            tempo += 10
    
    print(tempo)
