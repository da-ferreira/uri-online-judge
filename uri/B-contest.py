
grupos = {
    'bonecos':     0,
    'arquitetos':  0,
    'musicos':     0,
    'desenhistas': 0
}

quantidade = int(input())

for i in range(quantidade):
    nome, group, horas = input().split()

    grupos[group] += int(horas)

soma = grupos['bonecos'] // 8
soma += grupos['arquitetos'] // 4
soma += grupos['musicos'] // 6
soma += grupos['desenhistas'] // 12

print(soma)
