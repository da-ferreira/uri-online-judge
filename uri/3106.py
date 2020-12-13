
qtd_alunos = int(input())

alunos = list(map(int, input().split()))

soma = sum(alunos)

for i in range(qtd_alunos):
    soma -= alunos[i] % 3

print(soma)
