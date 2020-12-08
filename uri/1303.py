
pular_linha = 1

while True:
    n = int(input())
    if n == 0:
        break

    posicao_times = {}
    times = []
    # [inscricao 0, pontos 1, marcados 2, sofridos 3, cesta_average 4]

    for i in range(n * (n - 1) // 2):
        x, y, z, w = map(int, input().split())

        if x not in posicao_times:
            posicao_times[x] = len(times)
            
            if y > w:
                times.append([x, 2, y, w, None])
            else:
                times.append([x, 1, y, w, None])
        else:
            times[posicao_times[x]][2] += y         
            times[posicao_times[x]][3] += w

            if y > w:
                times[posicao_times[x]][1] += 2
            else:
                times[posicao_times[x]][1] += 1
        
        if z not in posicao_times:
            posicao_times[z] = len(times)
            
            if w > y:
                times.append([z, 2, w, y, None])
            else:
                times.append([z, 1, w, y, None])
        else:
            times[posicao_times[z]][2] += w         
            times[posicao_times[z]][3] += y
            
            if w > y:
                times[posicao_times[z]][1] += 2
            else:
                times[posicao_times[z]][1] += 1

    for i in range(len(posicao_times)):
        if times[i][3] != 0:
            times[i][4] = times[i][2] / times[i][3]
        else:
            times[i][4] = times[i][2]

    times = sorted(times, key=lambda k: k[0])
    times = sorted(times, key=lambda k: k[2], reverse=True)
    times = sorted(times, key=lambda k: k[4], reverse=True)
    times = sorted(times, key=lambda k: k[1], reverse=True)

    if pular_linha != 1:
        print()
    
    print(f'Instancia {pular_linha}')
    for i in range(len(posicao_times)):
        if i != (len(posicao_times) - 1):
            print(times[i][0], end=' ')
        else:
            print(times[i][0])
            
    pular_linha += 1
    