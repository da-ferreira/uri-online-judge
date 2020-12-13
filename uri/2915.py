
quantidade = int(input())
cartas = list(map(int, input().split()))
cartas = [[x] for x in cartas]

continuar = True

while continuar:
    continuar = False
    
    for i in range(len(cartas) - 2, -1, -1):
        if len(cartas[i]) == 1 and cartas[i][0] >= cartas[i + 1][-1]:
            cartas[i + 1].append(cartas[i].pop())
            cartas.pop(i)
            continuar = True

print(len(cartas))
