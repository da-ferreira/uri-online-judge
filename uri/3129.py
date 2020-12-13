
quantidades = int(input())

repetidas = diferentes = 0
figurinhas = set()

for i in range(quantidades):
    fig = int(input())

    if fig not in figurinhas:
        diferentes += 1
        figurinhas.add(fig)
    else:
        repetidas += 1

print(diferentes)
print(repetidas)
