
casos = int(input())

for i in range(casos):
    maletas = []
    diferenca = {}

    for j in range(3):
        maletas.append(list(map(int, input().split())))

        if abs(maletas[-1][0] - maletas[-1][1]) not in diferenca:
            diferenca[abs(maletas[-1][0] - maletas[-1][1])] = 2
        else:
            diferenca[abs(maletas[-1][0] - maletas[-1][1])] += 2
        
        if abs(maletas[-1][2] - maletas[-1][1]) not in diferenca:
            diferenca[abs(maletas[-1][2] - maletas[-1][1])] = 1
        else:
            diferenca[abs(maletas[-1][2] - maletas[-1][1])] += 1
    
    
    for j in diferenca:
        if diferenca[j] == max(diferenca.values()):
            maior = j
    
    possiveis_maletas = []

    for j in maletas:
        temp = [abs(j[0] - j[1]), abs(j[0] - j[2])]

        if maior not in temp:
            possiveis_maletas.append(j[0])
        
        temp = [abs(j[1] - j[0]), abs(j[1] - j[2])]

        if maior not in temp:
            possiveis_maletas.append(j[1])
        
        temp = [abs(j[2] - j[1]), abs(j[2] - j[0])]

        if maior not in temp:
            possiveis_maletas.append(j[2])
    
    print('Possiveis maletas: ', end='')

    for j in range(len(possiveis_maletas)):
        if j != len(possiveis_maletas) - 1:
            print(possiveis_maletas[j], end=', ')
        else:
            print(f'{possiveis_maletas[j]};')
    
