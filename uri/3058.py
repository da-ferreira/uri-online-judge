
supermercados = int(input())
precos = []

for i in range(supermercados):
    preco_carne, gramas = input().split()
    preco_carne = float(preco_carne)
    gramas = int(gramas)

    total = (1000 / gramas) * preco_carne
    precos.append(total)

print(f'{min(precos) :.2f}')
