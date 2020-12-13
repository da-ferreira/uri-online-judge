
while True:
    try:
        qtd = int(input())

        alunos = []

        for i in range(qtd):
            nome, regiao, custo = input().split()

            alunos.append([nome, regiao, int(custo)])
        
        alunos = sorted(alunos, key=lambda k: k[0])
        alunos = sorted(alunos, key=lambda k: k[1])
        alunos = sorted(alunos, key=lambda k: k[2])

        for a, b, c in alunos:
            print(a)
    except EOFError:
        break
