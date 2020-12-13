
criancas = int(input())

carrinhos = bonecas = 0
for i in range(criancas):
    nome = input()
    if nome[-1] == 'M':
        carrinhos += 1
    else:
        bonecas += 1

print(f'{carrinhos} carrinhos')
print(f'{bonecas} bonecas')
