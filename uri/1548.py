
casos = int(input())

for i in range(casos):
    m = int(input())
    alunos = list(map(int, input().split()))
    temp = sorted(alunos, reverse=True)

    resultado = 0
    for i in range(m):
        if alunos[i] == temp[i]:
            resultado += 1
    print(resultado)

