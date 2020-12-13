
while True:
    try:
        habitantes, consultas = map(int, input().split())
        notas = []

        for i in range(habitantes):
            notas.append(int(input()))

        notas.sort(reverse=True)

        for i in range(consultas):
            query = int(input())
            print(notas[query - 1])
    except EOFError:
        break
