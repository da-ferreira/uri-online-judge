
jogadores = list(map(int, input().split()))
oitavas = []
posicao = ''

for i in range(0, 16, 2):
    if 1 in [jogadores[i], jogadores[i + 1]] and 9 in [jogadores[i], jogadores[i + 1]]:
        posicao = 'oitavas'
    
    elif 1 in [jogadores[i], jogadores[i + 1]]:
        oitavas.append(1)
    
    elif 9 in [jogadores[i], jogadores[i + 1]]:
        oitavas.append(9)
    
    else:
        oitavas.append(jogadores[i])

if posicao == '':
    quartas = []

    for i in range(0, 8, 2):
        if 1 in [oitavas[i], oitavas[i + 1]] and 9 in [oitavas[i], oitavas[i + 1]]:
            posicao = 'quartas'
        
        elif 1 in [oitavas[i], oitavas[i + 1]]:
            quartas.append(1)
        
        elif 9 in [oitavas[i], oitavas[i + 1]]:
            quartas.append(9)
        
        else:
            quartas.append(oitavas[i])

if posicao == '':
    semi = []

    for i in range(0, 4, 2):
        if 1 in [quartas[i], quartas[i + 1]] and 9 in [quartas[i], quartas[i + 1]]:
            posicao = 'semifinal'
        
        elif 1 in [quartas[i], quartas[i + 1]]:
            semi.append(1)
        
        elif 9 in [quartas[i], quartas[i + 1]]:
            semi.append(9)
        
        else:
            semi.append(quartas[i])

if posicao == '':
    posicao = 'final'

print(posicao)
