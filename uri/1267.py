
while True:
    alunos, jantares = map(int, input().split())
    if alunos == 0 and jantares == 0:
        break

    verify = [0] * alunos

    for i in range(jantares):
        temp = list(map(int, input().split()))

        for j in range(alunos):
            verify[j] += temp[j]

    if jantares in verify:
        print('yes')
    else:
        print('no')
    