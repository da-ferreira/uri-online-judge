
while True:
    qtd_temporadas, minutos_por_ep = map(int, input().split())
    if qtd_temporadas == -1:
        break

    temporadas = list(map(int, input().split()))
    minutos = temp = 0

    for i in range(qtd_temporadas):
        minutos += (temp + (temporadas[i] * minutos_por_ep))
        temp += temporadas[i] * minutos_por_ep
    
    print(minutos)
