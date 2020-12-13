
valor_em_caixa, custo_diario = map(int, input().split())

dias = (valor_em_caixa // custo_diario) + 1

if dias > 10:
    dias -= 10
    print(f'A UFSC fecha dia {dias} de outubro.')
else:
    print(f'A UFSC fecha dia {20 + dias} de setembro.')
