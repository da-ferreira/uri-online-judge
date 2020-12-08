
matriz = []
for i in range(12):
    linha = [0] * 12
    matriz.append(linha)

operacao = input()

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

soma = 0
comeco = 1
fim = 11

for i in range(0, 5):
    for j in range(comeco, fim):
        soma += matriz[j][i]
    comeco += 1
    fim -= 1

if operacao == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma / 30)) 
