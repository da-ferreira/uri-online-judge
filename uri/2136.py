
maior = ''
pessoas = []

while True:
    nome = input().split()
    if nome[0] == 'FIM' and len(nome) == 1:
        break

    if nome not in pessoas:
        pessoas.append(nome)

    if nome[1] == 'YES':
        if len(nome[0]) > len(maior):
            maior = nome[0]

pessoas = sorted(pessoas, key=lambda k: k[0])
pessoas = sorted(pessoas, key=lambda k: k[1], reverse=True)

for i in range(len(pessoas)):
    print(pessoas[i][0])

print('\nAmigo do Habay:')
print(f'{maior}')
