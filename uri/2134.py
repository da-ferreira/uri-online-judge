
instancias = 1
while True:
    try:
        n = int(input())
        alunos = []

        for i in range(n):
            nome, nota = input().split()

            alunos.append([nome, int(nota)])

        alunos = sorted(alunos, key=lambda k: k[0])
        alunos = sorted(alunos, key=lambda k: k[1], reverse=True)

        print(f'Instancia {instancias}')
        print(alunos[-1][0])
        print()

        instancias += 1
    except EOFError:
        break
