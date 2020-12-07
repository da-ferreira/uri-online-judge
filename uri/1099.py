
casos = int(input())

for i in range(casos):
    valores = input().split()
    valores[0] = int(valores[0])
    valores[1] = int(valores[1])
    valores.sort()

    soma = 0
    for j in range(valores[0]+1, valores[1]):
        if j % 2 == 1:
            soma += j
    print(soma)
    soma = 0
