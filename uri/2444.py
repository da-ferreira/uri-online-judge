
volume, modificacoes = map(int, input().split())
trocas = list(map(int, input().split()))

for i in trocas:
    volume += i
    if volume > 100:
        volume = 100
    if volume < 0:
        volume = 0
print(volume)
