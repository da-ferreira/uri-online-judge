
pular_linha = 1
while True:
    n = int(input())
    if n == 0:
        break

    if pular_linha != 1:
        print()
    
    camisetas = []

    for i in range(n):
        nome = input()
        cor, tamanho = input().split()

        camisetas.append([cor, tamanho, nome])

    camisetas = sorted(camisetas, key=lambda k: k[2])  # Ordenando por nome
    camisetas = sorted(camisetas, key=lambda k: k[1], reverse=True)  # Por tamanho
    camisetas = sorted(camisetas, key=lambda k: k[0])  # Por cor

    for a1, a2, a3 in camisetas:
        print(a1, a2, a3)

    pular_linha += 1
