
while True:
    try:
        livros = []
        quantidade = int(input())

        for i in range(quantidade):
            livros.append(input())

        livros.sort()

        for j in livros:
            print(j)
    except EOFError:
        break
