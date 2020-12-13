
qtd_produtos = int(input())

precos = {
    1001: 1.50, 1002: 2.50, 1003: 3.50, 1004: 4.50, 1005: 5.50 
}
comprados = []
soma = 0

for i in range(qtd_produtos):
    comprados.append(list(map(int, input().split())))

for j in range(qtd_produtos):
    soma += precos[comprados[j][0]] * comprados[j][1]

print('{:.2f}'.format(soma))
