
matriz = []
for i in range(12):
    linha = [0] * 12
    matriz.append(linha)

operacao = input()

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

soma = 0
fim = 1

for i in range(1, 12):
    for j in range(0, fim):
        soma += matriz[i][j]
    fim += 1

if operacao == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma / 66)) 
