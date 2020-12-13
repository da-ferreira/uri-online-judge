
casos = int(input())

for i in range(casos):
    linhas = int(input())
    soma = 0

    for j in range(linhas):
        soma += 2 ** j

    print(soma)
