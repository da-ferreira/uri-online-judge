
criancas = int(input())

nomes = []
comportadas = nao_comportadas = 0

for i in range(criancas):
    condicao, name = input().split()
    nomes.append(name)

    if condicao == '+':
        comportadas += 1
    else:
        nao_comportadas += 1

nomes.sort()

for kid in nomes:
    print(kid)

print('Se comportaram: {} | Nao se comportaram: {}'.format(comportadas, nao_comportadas))
