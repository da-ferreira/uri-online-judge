
competidores = int(input())

for i in range(competidores):
    nome = input()
    grau_dificuldade = float(input())
    notas = list(map(float, input().split()))

    notas.remove(max(notas)), notas.remove(min(notas))

    print('{} {:.2f}'.format(nome, (sum(notas) * grau_dificuldade)))
