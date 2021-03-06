
oeste = []
norte = []
sul = []
leste = []

ponto_cardial = int(input())

while True:
    if ponto_cardial == 0:
        break

    elif ponto_cardial == -1:
        while True:
            aviao = input()

            if aviao[0] != 'A':
                ponto_cardial = int(aviao)
                break

            oeste.append(aviao)        

    elif ponto_cardial == -2:
        while True:
            aviao = input()

            if aviao[0] != 'A':
                ponto_cardial = int(aviao)
                break

            sul.append(aviao)

    elif ponto_cardial == -3:
        while True:
            aviao = input()

            if aviao[0] != 'A':
                ponto_cardial = int(aviao)
                break

            norte.append(aviao)

    elif ponto_cardial == -4:
        while True:
            aviao = input()

            if aviao[0] != 'A':
                ponto_cardial = int(aviao)
                break

            leste.append(aviao)

saida = []
tamanho = len(oeste) + len(norte) + len(sul) + len(leste)

while tamanho > 0:
    if len(oeste) > 0:
        saida.append(oeste.pop(0))
        tamanho -= 1

    if len(norte) > 0:
        saida.append(norte.pop(0))
        tamanho -= 1

    if len(sul) > 0:
        saida.append(sul.pop(0))
        tamanho -= 1
    
    if len(leste) > 0:
        saida.append(leste.pop(0))
        tamanho -= 1

print(' '.join(saida))
