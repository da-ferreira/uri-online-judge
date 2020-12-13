
casos = int(input())

for i in range(casos):
    primeiro = input()
    segundo = input()

    nome = ''

    j = 0
    k = 2
    while (len(primeiro) + len(segundo)) != len(nome):
        nome += primeiro[j:k]
        nome += segundo[j:k]

        j += 2
        k += 2
    print(nome)
