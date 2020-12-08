
casos = int(input())

estudantes = []
for i in range(casos):
    turma = input().split()
    alunos = int(turma[0])
    for j in range(1, len(turma)):
        estudantes.append(int(turma[j]))
    
    acima_media = 0
    media = sum(estudantes) / alunos

    for j in range(len(estudantes)):
        if estudantes[j] > media:
            acima_media += 1

    percentual = '{:.3f}%'.format((100 * acima_media) / alunos)
    print(percentual)
    estudantes.clear()
