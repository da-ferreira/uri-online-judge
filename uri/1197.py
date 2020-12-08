
while True:
    try:
        valor = input().split()
        velo = int(valor[0])
        acele = int(valor[1])
        print((velo * 2) * acele)
    except:
        break

