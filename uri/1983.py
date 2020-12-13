
notas = []
alunos = {}

quantidade_alunos = int(input())
for i in range(quantidade_alunos):
    entrada = input().split()

    alunos[float(entrada[1])] = int(entrada[0])
    notas.append(float(entrada[1]))

if max(notas) < 8:
    print('Minimum note not reached')
else:
    print(alunos[max(notas)])
    