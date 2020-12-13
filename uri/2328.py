
cortes = int(input())
pedacos = list(map(int, input().split()))

armazenados = 0

for i in range(cortes):
    armazenados += (pedacos[i] - 1)

print(armazenados)
