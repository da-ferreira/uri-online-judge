
casos = int(input())

for i in range(casos):
    dias = 0
    kilos = float(input())
    while kilos > 1:
        kilos /= 2
        dias += 1
    print('{} dias'.format(dias))
 