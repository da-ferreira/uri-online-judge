
testes = 1

while True:
    qtd_jogadores = int(input())
    if qtd_jogadores == 0:
        break

    classificacao = []

    for i in range(qtd_jogadores):
        nome = input()
        pontos = list(map(int, input().split()))

        pontos.sort()
        pontos.pop(0)
        pontos.pop()

        classificacao.append([nome, sum(pontos)])

    classificacao.sort(key=lambda k: k[0])
    classificacao.sort(key=lambda k: k[1], reverse=True)

    print(f'Teste {testes}')

    j = 1
    for i in range(len(classificacao)):
        if i == 0:
            print(f'{j} {classificacao[i][1]} {classificacao[i][0]}')
        else:
            if classificacao[i][1] < classificacao[i - 1][1]:
                j = i + 1

                print(f'{i + 1} {classificacao[i][1]} {classificacao[i][0]}')
            else:
                print(f'{j} {classificacao[i][1]} {classificacao[i][0]}')

    print()

    testes += 1
