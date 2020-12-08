
casos = int(input())

for i in range(casos):
    valor = input().split()
    a = valor[0]
    b = valor[1]
    if b in a[-len(b):]:
        print('encaixa')
    else:
        print('nao encaixa')
