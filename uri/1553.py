
while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break

    perguntas = list(map(int, input().split()))
    perguntas.sort()

    freguentes = 0
    while len(perguntas) != 0:
        if perguntas.count(perguntas[0]) >= k:
            freguentes += 1
            for i in range(perguntas.count(perguntas[0])):
                perguntas.pop(0)
        else:
            for i in range(perguntas.count(perguntas[0])):
                perguntas.pop(0)
    print(freguentes)
