
while True:
    valor = int(input())
    if valor == 0:
        break

    gerados = {valor}

    while True:
        valor *= valor

        valor = str(valor)
        valor = valor.zfill(8)

        numero_aleatorio = int(valor[2:6])

        if numero_aleatorio not in gerados:
            gerados.add(numero_aleatorio)
        else:
            break
        
        valor = numero_aleatorio

    print(len(gerados))
