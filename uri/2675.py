
while True:
    try:
        quantidade = int(input())
        cartas = list(map(int, input().split()))
        soma = 0
        pilha = [cartas.pop(0)]
        
        while len(cartas) != 0:
            if cartas[0] > pilha[-1]:
                pilha.append(cartas.pop(0))
            else:
                soma += pilha.pop()

                if len(pilha) == 0:
                    pilha.append(cartas.pop(0))
            
        print(soma)
    except EOFError:
        break
