
casos = int(input())

for i in range(casos):
    inicio, fim = map(int, input().split())

    numeros = []
    invertidos = []

    for j in range(inicio, fim+1):
        numeros.append(str(j))

    for j in range(len(numeros) -1, -1, -1):
        invertidos.append(str(numeros[j][-1::-1]))

    resultado = ''.join(numeros)
    resultado += ''.join(invertidos)
    print(resultado)
