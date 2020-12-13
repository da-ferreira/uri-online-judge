
kung = int(input())
lu = int(input())

jogadores = [x for x in range(1, 17)]

oitavas = []
posicao = ''

for i in range(0, 16, 2):
    if lu in [jogadores[i], jogadores[i + 1]] and kung in [jogadores[i], jogadores[i + 1]]:
        posicao = 'oitavas'
    
    elif lu in [jogadores[i], jogadores[i + 1]]:
        oitavas.append(lu)
    
    elif kung in [jogadores[i], jogadores[i + 1]]:
        oitavas.append(kung)
    
    else:
        oitavas.append(jogadores[i])

if posicao == '':
    quartas = []

    for i in range(0, 8, 2):
        if lu in [oitavas[i], oitavas[i + 1]] and kung in [oitavas[i], oitavas[i + 1]]:
            posicao = 'quartas'
        
        elif lu in [oitavas[i], oitavas[i + 1]]:
            quartas.append(lu)
        
        elif kung in [oitavas[i], oitavas[i + 1]]:
            quartas.append(kung)
        
        else:
            quartas.append(oitavas[i])

if posicao == '':
    semi = []

    for i in range(0, 4, 2):
        if lu in [quartas[i], quartas[i + 1]] and kung in [quartas[i], quartas[i + 1]]:
            posicao = 'semifinal'
        
        elif lu in [quartas[i], quartas[i + 1]]:
            semi.append(lu)
        
        elif kung in [quartas[i], quartas[i + 1]]:
            semi.append(kung)
        
        else:
            semi.append(quartas[i])

if posicao == '':
    posicao = 'final'

print(posicao)
