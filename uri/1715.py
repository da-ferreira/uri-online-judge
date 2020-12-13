

jogadores, partidas = map(int, input().split())

resultado = 0

for i in range(jogadores):
    gols = list(map(int, input().split()))

    veracidade = 0

    for j in gols:
        if j > 0:  
            veracidade += 1
    if veracidade == partidas:
        resultado += 1

print(resultado)
    