
visitantes = int(input())
jogadores = ['F A C E']

premios = 0

for i in range(visitantes):
    jogadores.append(input())

j = 1
painel = 0

while j < len(jogadores) and len(jogadores) > 0:
    if jogadores[j][::-1] == jogadores[painel]:
        premios += 1

        jogadores.pop(j)
        jogadores.pop(painel)
        j -= 2

        if j - 1 > 0:
            painel = j - 1
        else:
            jogadores.insert(0, 'F A C E')
            painel = 0
            j = 1
    else:
        painel = j
        j += 1

print(premios)
