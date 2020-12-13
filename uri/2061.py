
numero_de_abas, acoes = map(int, input().split())

for i in range(acoes):
    acao = input()

    if acao == 'fechou':
        numero_de_abas += 1
    else:
        numero_de_abas -= 1
print(numero_de_abas) 
