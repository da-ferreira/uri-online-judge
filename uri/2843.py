
def tempo_de_escrita(reacao, escrita, frase):
    tempo = reacao + (escrita * frase)

    return tempo


quantidade = int(input())
rank = [0] * quantidade
jogadores = []

for i in range(quantidade):
    reacao, escrita = map(int, input().split())
    jogadores.append([reacao, escrita, i])

frase = input()
frase = len(frase)

fase = 1
i = 0

while quantidade != 1:
    tempo1 = tempo_de_escrita(jogadores[i][0], jogadores[i][1], frase)
    tempo2 = tempo_de_escrita(jogadores[i + 1][0], jogadores[i + 1][1], frase)

    if tempo1 <= tempo2:
        rank[jogadores[i + 1][2]] = fase
        jogadores[i + 1] = 0
    else:
        rank[jogadores[i][2]] = fase
        jogadores[i] = 0
    
    quantidade -= 1
    
    if i + 1 == len(jogadores) - 1:
        i = 0
        fase += 1
        frase += frase
        k = 0

        while k < len(jogadores):
            if jogadores[k] == 0:
                jogadores.pop(k)
            else:
                k += 1
    else:
        i += 2
    
rank[jogadores[0][2]] = fase

print(' '.join(str(x) for x in rank))

