
while True:
    n = int(input())
    if n == 0:
        break

    problemas = {}

    tempo = resolvidos = 0


    for i in range(n):
        identificador, t, modo = input().split()
        t = int(t)

        if modo == 'correct':
            if identificador in problemas:
                tempo += t + (problemas[identificador][2] * 20)
            else:
                tempo += t 

            resolvidos += 1
        else:
            if identificador not in problemas:
                problemas[identificador] = [t, modo, 1]
            else:
                problemas[identificador][2] += 1

    print(resolvidos, tempo)
