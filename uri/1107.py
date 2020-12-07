
while True:
    a, c = map(int, input().split())
    if a == 0 and c == 0:
        break

    alturas_finais = list(map(int, input().split()))
    lazer = 0

    if alturas_finais[0] < a:
        lazer += a - alturas_finais[0]


    if len(alturas_finais):
        for i in range(1, c):
            if alturas_finais[i] < alturas_finais[i - 1]:
                lazer += (alturas_finais[i - 1] - alturas_finais[i])

    print(lazer)
