
quantidade = int(input())

for i in range(quantidade):
    nao_anunciou, anunciou, preco_publicidade = map(int, input().split())

    if (nao_anunciou == (anunciou - preco_publicidade)):
        print("does not matter")
    elif ((anunciou - preco_publicidade) > nao_anunciou):
        print("advertise")
    else:
        print("do not advertise")
