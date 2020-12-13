
casos = int(input())

for i in range(casos):
    altura, diametro, galhos = map(int, input().split())

    if (altura >= 200 and altura <= 300) and (diametro >= 50) and (galhos >= 150):
        print('Sim')
    else:
        print('Nao')
