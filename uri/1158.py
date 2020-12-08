
casos = int(input())
soma = 0

for i in range(casos):
    valores = input().split()
    x = int(valores[0])
    y = int(valores[1])

    if x % 2 == 1:
        soma = x
        for j in range(1, y):
            x += 2
            soma += x
    else:
        soma = x + 1
        x += 1
        for k in range(1, y):
            x += 2
            soma += x
    print(soma)
    soma = 0
