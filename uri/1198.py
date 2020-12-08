
while True:
    try:
        soldados = input().split()
        hashmat = int(soldados[0])
        oponente = int(soldados[1])
        print(abs(oponente - hashmat))
    except:
        break
