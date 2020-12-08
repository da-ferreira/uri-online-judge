
casos = int(input())

for i in range(casos):
    casas = int(input())

    graos = 1

    for j in range(casas):
        graos *= 2
    
    graos //= 12
    graos //= 1000

    print(graos, 'kg')
