
while True:
    pontos = float(input())
    if pontos == 0:
        break

    aux = pontos + (pontos - 3)
    aux -= pontos

    print('{:.6f}'.format(aux / pontos ))
