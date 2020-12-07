
while True:
    bancos, debentures = map(int, input().split())
    if bancos == 0 and debentures == 0:
        break

    reversas_bancos = list(map(int, input().split()))

    for i in range(debentures):
        devedor, credor, valor = map(int, input().split())

        reversas_bancos[credor - 1] += valor
        reversas_bancos[devedor - 1] -= valor

    if all(x >= 0 for x in reversas_bancos):
        print('S')
    else:
        print('N')
