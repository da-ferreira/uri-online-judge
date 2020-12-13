
nomes = []

alunos, sorteado = map(int, input().split())

for i in range(alunos):
    nomes.append(input())
nomes.sort()

print(nomes[sorteado - 1])
