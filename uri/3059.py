
quantidade, minimo, maximo = map(int, input().split())
numeros = list(map(int, input().split()))

resultado = 0

for i in range(quantidade):
    numeros.insert(0, numeros.pop(i))

    for j in range(1, quantidade):
        if minimo <= (numeros[j] + numeros[0]) <= maximo:
            resultado += 1

print(resultado // 2)
