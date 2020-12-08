
while True:
    n, m = map(int, input().split())
    if m == 0 and n == 0:
        break

    servidores = []

    for i in range(n):
        temp = input().split()
        servidores.append(temp[1:])

    conexoes = 0
    ja_conectado = set()

    for i in range(m):
        clientes = input().split()

        for j in range(1, int(clientes[0]) + 1):
            if j == 1:
                for k in range(n):
                    if clientes[j] in servidores[k]:
                        conexoes += 1
                        ja_conectado.add(k)
            else:
                for k in range(n):
                    if clientes[j] in servidores[k] and k not in ja_conectado:
                        conexoes += 1
                        ja_conectado.add(k)
        
        ja_conectado = set()

    print(conexoes)
