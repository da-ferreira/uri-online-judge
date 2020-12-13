
def atualizar_digitos(lista):
    dicionario = {}
    letras = 'ABCDE'
    j = 0

    for i in range(0, 10, 2):
        dicionario[letras[j]] = lista[i:i + 2]
        j += 1

    return dicionario

testes = 1

while True:
    quantidade = int(input())
    if quantidade == 0:
        break

    senha = [{} for x in range(6)]

    for i in range(quantidade):
        entrada = input().split()

        temp = atualizar_digitos(list(map(int, entrada[0:10])))
        del entrada[0:10]

        
        for j in range(6):
            if temp[entrada[j]][0] not in senha[j]:
                senha[j][temp[entrada[j]][0]] = 1
            else:
                senha[j][temp[entrada[j]][0]] += 1
        
            if temp[entrada[j]][1] not in senha[j]:
                senha[j][temp[entrada[j]][1]] = 1
            else:
                senha[j][temp[entrada[j]][1]] += 1
        
    senha_cliente = ''

    for i in range(6):
        maior = max(senha[i].values())

        for j in senha[i]:
            if senha[i][j] == maior:
                senha_cliente += f'{j} '
                break
    
    print(f'Teste {testes}')
    print(senha_cliente)
    print()
    testes += 1
