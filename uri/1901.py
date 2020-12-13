
tamanho = int(input())

floresta = []
especies = []

for i in range(tamanho):
    floresta.append(input().split())

for i in range(tamanho * 2):
    x, y = map(int, input().split())

    if floresta[x - 1][y - 1] not in especies:
        especies.append(floresta[x - 1][y - 1])

print(len(especies))
