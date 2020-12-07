
while True:
    grandes, pilotos = map(int, input().split())
    if grandes == 0 and pilotos == 0:
        break
    
    temp = pilotos  # <- Numero de pilotos
    grandes_premios = []
    
    for i in range(grandes):
        grandes_premios.append(list(map(int, input().split()))) # <- Cada corrida

    sistemas = int(input()) 

    for i in range(sistemas):
        pontuacao = list(map(int, input().split()))
        ultima_chegada = pontuacao[0]; pontuacao.pop(0)

        pilotos = [0] * temp # <- Identificador de cada piloto

        for j in range(len(grandes_premios)):
            for k in range(ultima_chegada):
                pilotos[grandes_premios[j].index(k + 1)] += pontuacao[k]
        
        vencedores = []
        maior = 0

        for j in range(len(pilotos)):
            if pilotos[j] > maior:
                vencedores.clear()
                maior = pilotos[j]
                vencedores.append(str(pilotos.index(pilotos[j]) + 1))
                pilotos[j] = ' '
            elif pilotos[j] == maior:
                vencedores.append(str(pilotos.index(pilotos[j]) + 1))
                pilotos[j] = ' '
        
        print(' '.join(vencedores))
