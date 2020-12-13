
i = 1
while True:
    n = int(input())
    if n == 0:
        break

    maiores = []
    maior = 0

    for j in range(n):
        codigo, media = map(int, input().split())

        if media > maior:
            maiores.clear()
            maiores.append(codigo)
            maior = media


        elif media == maior:
            maiores.append(codigo)


    print(f'Turma {i}')
    for j in range(len(maiores)):
        print(maiores[j], end=' ')
    print()

    print()
    i += 1
