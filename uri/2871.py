
while True:
    try:    
        linhas, colunas = map(int, input().split())
        quantidade = 0

        for i in range(linhas):
            colheita = list(map(int, input().split()))
            quantidade += sum(colheita)

        sacas = quantidade // 60
        litros = quantidade - (60 * sacas)

        print(f'{sacas} saca(s) e {litros} litro(s)')
    except EOFError:
        break
