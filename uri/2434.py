
dias, saldo = map(int, input().split())

for i in range(dias):
    if i == 0:
        menor = saldo

    movimentacao = int(input())
    saldo += movimentacao

    if saldo < menor:
        menor = saldo

print(menor)
