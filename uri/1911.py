
while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    alunos = {}

    for i in range(quantidade):
        entrada = input().split()

        alunos[entrada[0]] = entrada[1]
    
    comparecidos = int(input())

    falsas = 0

    for i in range(comparecidos):
        entrada2 = input().split(' ')

        erros = 0

        for i in range(len(entrada2[1])):
            if entrada2[1][i] != alunos[entrada2[0]][i]:
                erros += 1
        if erros > 1:
            falsas += 1
                    
    print(falsas)
