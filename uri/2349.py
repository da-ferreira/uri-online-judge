
qtd_estacoes, commands, devastada = map(int, input().split())

comandos = list(map(int, input().split()))
vezes = 0
robo = 1

for i in range(commands):
    if robo == devastada:
        vezes += 1

    if comandos[i] == 1:
        if robo < qtd_estacoes:
            robo += 1
        else:
            robo = 1
    
    else:
        if robo == 1:
            robo = qtd_estacoes
        else:
            robo -= 1

if robo == devastada:
    vezes += 1   

print(vezes)
