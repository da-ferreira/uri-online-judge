
dia_inicial, preco, valor, dias = map(int, input().split())

ate = dia_inicial + dias

while dia_inicial < ate:
    dia_inicial += 1

    if dia_inicial % 2 == 0:
        preco += valor
    else:
        preco -= valor

print(preco)
