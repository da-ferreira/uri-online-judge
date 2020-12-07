
while True:
    valores = input().split()
    valores[0] = int(valores[0])
    valores[1] = int(valores[1])
    valores.sort()

    if valores[0] <= 0 or valores[1] <= 0:
        break

    soma = 0
    for i in range(valores[0], valores[1]+1):
        soma += i
        print(i, end=' ')
    print('Sum={}'.format(soma))
    soma = 0
