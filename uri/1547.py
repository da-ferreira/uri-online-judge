
casos = int(input())

for i in range(casos):
    qt, numero = map(int, input().split())

    alunos = list(map(int, input().split()))

    if numero in alunos:
        print(alunos.index(numero) + 1)
    else:
        diferenca = [float('inf'), 0]

        for i in range(qt):
            if abs(numero - alunos[i]) < diferenca[0]:
                diferenca[0] = abs(numero - alunos[i])
                diferenca[1] = alunos[i]

        print(alunos.index(diferenca[1]) + 1)
