
while True:
    distancia, velocidade = map(int, input().split())
    if distancia == 0 and velocidade == 0:
        break

    eh_possivel = False

    while velocidade != 0:
        temp = velocidade
        soma = 0

        while temp != 0:
            for i in range(temp):
                soma += temp

                if distancia == soma:
                    eh_possivel = True
                    
            temp -= 1

        velocidade -= 1

    if eh_possivel:
        print('possivel')
    else:
        print('impossivel')
