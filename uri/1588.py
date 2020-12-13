
casos = int(input())

for i in range(casos):
    n, m = map(int, input().split())

    posicao_time = {}
    times = []
    #[nome, pontos, vitorias, mais_gols, numero_entrada]

    for j in range(n):
        nome = input()
        posicao_time[nome] = j

        times.append([nome, 0, 0, 0, j])

    for j in range(m):
        x, timeA, y, timeB = input().split()

        x = int(x)
        y = int(y)

        if x > y:
            times[posicao_time[timeA]][1] += 3
            times[posicao_time[timeA]][2] += 1
        elif y > x:
            times[posicao_time[timeB]][1] += 3
            times[posicao_time[timeB]][2] += 1
        else:
            times[posicao_time[timeA]][1] += 1
            times[posicao_time[timeB]][1] += 1

        times[posicao_time[timeA]][3] += x
        times[posicao_time[timeB]][3] += y

    times = sorted(times, key=lambda k: k[4])
    times = sorted(times, key=lambda k: k[3], reverse=True)
    times = sorted(times, key=lambda k: k[2], reverse=True)
    times = sorted(times, key=lambda k: k[1], reverse=True)

    for j in range(len(times)):
        print(times[j][0])
