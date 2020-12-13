
n = int(input())

funcionarios = {x: x for x in range(1, n + 1)}

q = int(input())

for i in range(q):
    operacao = list(map(int, input().split()))

    if operacao[0] == 1:
        funcionarios[operacao[1]], funcionarios[operacao[2]] = funcionarios[operacao[2]], funcionarios[operacao[1]]
    else:
        redirecionamentos = 0
        proximo = operacao[1]

        while funcionarios[proximo] != operacao[1]:
            proximo = funcionarios[proximo]
            redirecionamentos += 1

        print(redirecionamentos) 
