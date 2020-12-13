
while True:
    qtd_times = int(input())
    if qtd_times == 0:
        break

    times = []
    posicao_times = {}

    for i in range(qtd_times):
        nome, pontos = input().split()
        
        times.append([nome, int(pontos)])
        posicao_times[nome] = i

    for i in range(qtd_times // 2):
        timeA, placar, timeB = input().split()

        placar = placar.split('-')
        placar = [int(x) for x in placar]

        times[posicao_times[timeA]][1] += (3 * placar[0])
        times[posicao_times[timeB]][1] += (3 * placar[1])

        if placar[0] > placar[1]:
            times[posicao_times[timeA]][1] += 5
        elif placar[1] > placar[0]:
            times[posicao_times[timeB]][1] += 5
        else:
            times[posicao_times[timeA]][1] += 1
            times[posicao_times[timeB]][1] += 1
        
    
    times.sort(key=lambda k: k[1], reverse=True)

    if times[0][0] == 'Sport':
        print(f'O Sport foi o campeao com {times[0][1]} pontos :D')
    else:
        print(f'O Sport nao foi o campeao. O time campeao foi o {times[0][0]} com {times[0][1]} pontos :(')

    print()
