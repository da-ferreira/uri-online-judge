
n = int(input())
candidatos = []

for i in range(n):
    nome, poder, deuses_mortos, mortes = input().split()
    candidatos.append([nome, int(poder), int(deuses_mortos), int(mortes)])

candidatos.sort(key=lambda k: k[0])
candidatos.sort(key=lambda k: k[3])
candidatos.sort(key=lambda k: k[2], reverse=True)
candidatos.sort(key=lambda k: k[1], reverse=True)

print(candidatos[0][0])
