
entrada, jogadas = map(int, input().split())

players = {
    'D': entrada,
    'E': entrada,
    'F': entrada
}

for i in range(jogadas):
    entrada = input().split()

    if len(entrada) == 3:
        if entrada[0] == 'C':
            players[entrada[1]] -= int(entrada[2])
        else:
            players[entrada[1]] += int(entrada[2])
    else:
        players[entrada[1]] += int(entrada[3])
        players[entrada[2]] -= int(entrada[3])
    
print(players['D'], players['E'], players['F'])
