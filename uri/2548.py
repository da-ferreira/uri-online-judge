
while True:
    try:
        n, m = map(int, input().split())
        
        itens = list(map(int, input().split()))
        itens.sort(reverse=True)

        soma = sum(itens[0:m])
        print(soma)

    except EOFError:
        break
