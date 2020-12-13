
while True:
    n = int(input())
    if n == 0:
        break

    alunos = list(map(int, input().split()))
    comeco = int(input())

    i = 0

    while i < len(alunos):
        if alunos[comeco - 1] == comeco:
            print(comeco)
            break
        else:
            comeco = alunos[comeco - 1]

        i += 1
