
n = int(input())

marcados = []
sequencia = []

for i in range(n):
    sequencia.append(input())

for i in range(n):
    if i == 0:
        marcados.append(sequencia[i])
    else:
        if sequencia[i] != marcados[-1]:
            marcados.append(sequencia[i])

print(len(marcados))
