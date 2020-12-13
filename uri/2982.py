
valores = int(input())

governo = faculdade = 0

for i in range(valores):
    preco = input().split()

    if preco[0] == 'G':
        faculdade += int(preco[1])
    else:
        governo += int(preco[1])

if governo >= faculdade:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
