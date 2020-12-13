
qtd_cartas, mesa, limite = map(int, input().split())

cartas = []

alice = bob = 0

for i in range(qtd_cartas - 1):
    cartas.append(int(input()))

alterna = True

for i in range(qtd_cartas - 1):
    if alterna:
        if abs(cartas[i] - mesa) <= limite:
            alice += abs(cartas[i] - mesa)
            mesa = cartas[i]
            
        alterna = False
    else:
        if abs(cartas[i] - mesa) <= limite:
            bob += abs(cartas[i] - mesa)
            mesa = cartas[i]

        alterna = True

print(alice, bob)
